import streamlit as st
import pandas as pd
import tempfile
import zipfile
import os
import re
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.styles import Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from PyPDF2 import PdfReader

# ============================
# 기본 화면
# ============================
st.title("🧾 (주)건화 등기부등본 통합분석기")

# ============================
# 경로 정의 (pages 기준 repo root)
# pages/*.py 파일은 pages 폴더 안에 있으므로 상위 1단계가 repo root
# ============================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
MANUAL_PDF = os.path.join(ASSETS_DIR, "manual.pdf")

# ============================
# 공통 다운로드 유틸 (bytes로 처리)
# ============================
def download_button(label, file_path, mime, download_name=None):
    if not os.path.exists(file_path):
        st.error(f"파일이 없습니다: {os.path.basename(file_path)}")
        st.caption(f"확인 경로: {file_path}")
        return

    with open(file_path, "rb") as f:
        data = f.read()

    st.download_button(
        label=label,
        data=data,
        file_name=download_name or os.path.basename(file_path),
        mime=mime,
        use_container_width=True
    )

# ============================
# PDF 매뉴얼 (다운로드 전용)
# ============================
with st.expander("📖 매뉴얼 보기", expanded=False):
    if os.path.exists(MANUAL_PDF):
        download_button(
            label="📄 PDF 매뉴얼 다운로드",
            file_path=MANUAL_PDF,
            mime="application/pdf",
            download_name="등기부등본_자동정리프로그램_Manual.pdf"
        )
        st.caption("※ 다운로드 후 브라우저 또는 PDF 뷰어에서 열어주세요.")
    else:
        st.warning("assets/manual.pdf 파일을 찾을 수 없습니다.")

st.markdown("""
### 서비스 이용 안내
- **등기사항전부증명서(열람용)** Excel 파일만 지원됩니다.
- Acrobat Pro를 이용해 등기부등본 PDF를 Excel로 변환한 후, 해당 파일들을 **ZIP**으로 압축해 업로드하세요.
- 반드시 정식 발급된 열람용 문서를 사용해 주세요.
- 발급 시 **주요 등기사항 요약 페이지**를 반드시 포함해야 합니다.
- 등기부 특성상 통합 과정에서 일부 주요 내용이 누락될 수 있으므로, **원본대조 검토**가 필요합니다.
""")

# ============================
# 업로드 UI
# ============================
uploaded_zip = st.file_uploader("📈 EXCEL.zip 파일을 업로드하세요 (내부에 .xlsx 파일 포함)", type=["zip"])
uploaded_pdf_zip = st.file_uploader("📄 PDF.zip 파일을 업로드하세요 (내부에 .pdf 파일 포함)", type=["zip"], key="pdf_zip")
run_button = st.button("분석 시작")

# ============================
# (중략) ---- 아래는 너 기존 함수/로직 그대로 ----
# ============================

# 주소 추출 정규표현식 패턴
pattern_specific = re.compile(r'\[토지\]\s*(충청남도\s*서산시\s*대산읍\s*[가-힣]+리)\s*(산?\d+(?:-\d+)?)')
pattern_dong_ri = re.compile(r'\[토지\]\s*([가-힣]+[도시군구광역]\s*[가-힣]+[시군구]\s*[가-힣]+[읍면동리])\s*(산?\d+(?:-\d+)?)')
pattern_gwangyeoksi = re.compile(r'\[토지\]\s*([가-힣]+광역시\s*[가-힣]+구\s*[가-힣]+동)\s*(산?\d+(?:-\d+)?)')
pattern_si_gu_dong = re.compile(r'\[토지\]\s*([가-힣]+시\s*[가-힣]+구\s*[가-힣]+동)\s*(산?\d+(?:-\d+)?)')
pattern_gun_eup_ri = re.compile(r'\[토지\]\s*([가-힣]+[도]\s*[가-힣]+[군]\s*[가-힣]+[읍면]\s*[가-힣]+리)\s*(산?\d+(?:-\d+)?)')
pattern_flexible = re.compile(r'\[토지\][\s]*([가-힣\s]+[도시군구광역][\s]*[가-힣\s]+[시군구][\s]*[가-힣\s]+[읍면동리])[\s]*(산?\d+(?:-\d+)?)')
pattern_san_specific = re.compile(r'\[토지\]\s*([가-힣]+[도시군구광역]\s*[가-힣]+[시군구]\s*[가-힣]+[읍면동리])\s*산\s*(\d+(?:-\d+)?)')
pattern_san_flexible = re.compile(r'\[토지\][\s]*([가-힣\s]+[도시군구광역][\s]*[가-힣\s]+[시군구][\s]*[가-힣\s]+[읍면동리])[\s]*산[\s]*(\d+(?:-\d+)?)')

def extract_address_from_pdf_text(text):
    patterns = [
        (pattern_san_specific, "산지번 특정패턴"),
        (pattern_san_flexible, "산지번 유연패턴"),
        (pattern_specific, "특정패턴(서산)"),
        (pattern_gwangyeoksi, "광역시패턴"),
        (pattern_si_gu_dong, "시구동패턴"),
        (pattern_gun_eup_ri, "군읍리패턴"),
        (pattern_dong_ri, "동리패턴"),
        (pattern_flexible, "유연패턴")
    ]
    for pattern, pattern_type in patterns:
        match = pattern.search(text)
        if match:
            address = re.sub(r'\s+', ' ', match.group(1))
            lot_no = match.group(2)
            if "산지번" in pattern_type:
                lot_no = f"산{lot_no}"
            return address, lot_no, pattern_type
    return None, None, None

def process_pdf_files(folder_path):
    success_count = 0
    failure_count = 0
    error_summary = {}
    successful_samples = []
    failed_samples = []

    pdfs = [f for f in os.listdir(folder_path) if f.lower().endswith(".pdf")]
    total_files = len(pdfs)

    progress_bar = st.progress(0)
    status_text = st.empty()

    for i, filename in enumerate(pdfs):
        progress = (i + 1) / total_files if total_files else 1.0
        progress_bar.progress(progress)
        status_text.text(f"처리 중... {i + 1}/{total_files} ({progress:.1%})")

        full_path = os.path.join(folder_path, filename)
        try:
            reader = PdfReader(full_path)
            if len(reader.pages) == 0:
                error_type = "PDF 페이지 없음"
                error_summary[error_type] = error_summary.get(error_type, 0) + 1
                if len(failed_samples) < 5:
                    failed_samples.append(f"{filename} - {error_type}")
                failure_count += 1
                continue

            first_page_text = reader.pages[0].extract_text()
            if not first_page_text or first_page_text.strip() == "":
                error_type = "텍스트 추출 실패"
                error_summary[error_type] = error_summary.get(error_type, 0) + 1
                if len(failed_samples) < 5:
                    failed_samples.append(f"{filename} - {error_type}")
                failure_count += 1
                continue

            address, lot_no, pattern_type = extract_address_from_pdf_text(first_page_text)

            if address and lot_no:
                new_filename = f"{address}_{lot_no}.pdf"
                new_path = os.path.join(folder_path, new_filename)

                if not os.path.exists(new_path):
                    os.rename(full_path, new_path)
                    success_count += 1
                    if len(successful_samples) < 5:
                        successful_samples.append(f"{filename} → {new_filename} ({pattern_type})")
                else:
                    error_type = "파일명 중복"
                    error_summary[error_type] = error_summary.get(error_type, 0) + 1
                    if len(failed_samples) < 5:
                        failed_samples.append(f"{filename} - {error_type}")
                    failure_count += 1
            else:
                error_type = "주소 패턴 미발견"
                error_summary[error_type] = error_summary.get(error_type, 0) + 1
                if len(failed_samples) < 5:
                    failed_samples.append(f"{filename} - {error_type}")
                failure_count += 1

        except Exception as e:
            error_type = f"처리 오류: {type(e).__name__}"
            error_summary[error_type] = error_summary.get(error_type, 0) + 1
            if len(failed_samples) < 5:
                failed_samples.append(f"{filename} - {str(e)[:50]}...")
            failure_count += 1

    progress_bar.progress(1.0)
    status_text.text("처리 완료!")

    st.write("---")
    st.write("## 📊 PDF 파일명 변경 결과")

    c1, c2, c3 = st.columns(3)
    with c1: st.metric("✅ 성공", success_count)
    with c2: st.metric("❌ 실패", failure_count)
    with c3: st.metric("📁 전체", total_files)

    success_rate = (success_count / total_files * 100) if total_files > 0 else 0
    st.write(f"**성공률: {success_rate:.1f}%**")

    if successful_samples:
        st.write("### ✅ 성공 사례 (샘플)")
        for s in successful_samples:
            st.write(f"- {s}")

    if error_summary:
        st.write("### ❌ 실패 유형별 통계")
        for et, cnt in error_summary.items():
            pct = (cnt / failure_count * 100) if failure_count > 0 else 0
            st.write(f"- **{et}**: {cnt}개 ({pct:.1f}%)")
        if failed_samples:
            st.write("### 🔍 실패 사례 (샘플)")
            for s in failed_samples:
                st.write(f"- {s}")

    return success_count, failure_count

def extract_and_process_pdf_zip(zip_file_path, extract_to, output_zip_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    process_pdf_files(extract_to)
    with zipfile.ZipFile(output_zip_path, 'w') as zip_out:
        for root, _, files in os.walk(extract_to):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, extract_to)
                zip_out.write(full_path, arcname)

# ============================
# 여기부터: 너 기존 “분석 실행” 블록
# 핵심: final 다운로드는 bytes로
# ============================
if run_button and uploaded_zip:
    temp_dir = tempfile.mkdtemp()
    szj_list, syg_list, djg_list = [], [], []

    # ✅ UploadedFile을 zipfile이 안정적으로 읽도록 bytes로 저장 후 처리
    uploaded_zip_path = os.path.join(temp_dir, "input_excel.zip")
    with open(uploaded_zip_path, "wb") as f:
        f.write(uploaded_zip.getbuffer())

    with zipfile.ZipFile(uploaded_zip_path, "r") as z:
        z.extractall(temp_dir)

    # ---- (이하 너 기존 엑셀 파싱/정리 로직 그대로 두면 됨) ----
    # ⚠️ 너가 올린 코드가 너무 길어서 여기서부터 아래쪽은 “기존 그대로” 유지해도 되는데,
    #     꼭 아래 2가지만 반영해:
    #     - pdf zip도 bytes로 저장 후 처리
    #     - 최종 download_button에서 f.read()로 bytes 넣기

    # ====== 너 기존 로직 계속 ======
    # (중략: 너 코드 그대로)

    # 2. PDF ZIP 처리 (있을 때만) - ✅ bytes로 저장 후 처리
    pdf_result_path = None
    if uploaded_pdf_zip:
        temp_pdf_dir = tempfile.mkdtemp()
        temp_pdf_zip_path = os.path.join(temp_pdf_dir, "input_pdf.zip")
        with open(temp_pdf_zip_path, "wb") as f:
            f.write(uploaded_pdf_zip.getbuffer())

        extract_folder = os.path.join(temp_pdf_dir, "extracted")
        os.makedirs(extract_folder, exist_ok=True)

        pdf_result_path = os.path.join(temp_pdf_dir, "processed_result_pdf.zip")
        extract_and_process_pdf_zip(temp_pdf_zip_path, extract_folder, pdf_result_path)

    # 3. 통합 결과 ZIP 생성 및 다운로드 버튼 (✅ bytes로)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".zip") as final_zip:
        with zipfile.ZipFile(final_zip.name, 'w') as z:
            z.write(excel_result_path, arcname="등기사항_통합_시트별구성.xlsx")
            if pdf_result_path and os.path.exists(pdf_result_path):
                z.write(pdf_result_path, arcname="PDF_파일명_일괄변경_결과.zip")

        st.success("✅ 분석 완료! 아래에서 통합 결과 파일을 다운로드하세요.")
        with open(final_zip.name, "rb") as f:
            st.download_button(
                "📥 통합 결과 ZIP 다운로드 (엑셀+PDF)",
                data=f.read(),
                file_name="통합_결과.zip",
                mime="application/zip",
                use_container_width=True
            )

elif run_button and (not uploaded_zip):
    st.warning("엑셀 ZIP 파일을 업로드해야 분석이 가능합니다.")
