# services/card_app.py
import os
import streamlit as st

APP_TITLE = "(주)건화 관리카드 자동작성 프로그램"

def run():
    # ✅ set_page_config 금지 (app.py에서 1번만)
    # ✅ 비밀번호 금지 (app.py에서 공통 게이트)

    # ============================
    # 경로 설정 (repo root 기준)
    # services/card_app.py 기준으로 상위 1단계가 repo root
    # ============================
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ASSETS_DIR = os.path.join(BASE_DIR, "assets")

    MANUAL_PDF = os.path.join(ASSETS_DIR, "manual.pdf")
    MACRO_PACK = os.path.join(ASSETS_DIR, "관리카드자동작성.zip")
    EXCEL_TEMPLATE = os.path.join(ASSETS_DIR, "결합용엑셀.xlsx")

    # ============================
    # 다운로드 유틸
    # ============================
    def download_button(label: str, file_path: str, mime: str, download_name: str | None = None):
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
    # 헤더
    # ============================
    st.markdown(f"### 📄 {APP_TITLE}")
    st.caption("매뉴얼 / PPT 매크로 / 결합용 엑셀 양식 다운로드")

    # ============================
    # PDF 매뉴얼
    # ============================
    with st.expander("📖 매뉴얼 보기", expanded=False):
        if os.path.exists(MANUAL_PDF):
            download_button(
                label="📄 PDF 매뉴얼 다운로드",
                file_path=MANUAL_PDF,
                mime="application/pdf",
                download_name="관리카드_자동작성_매뉴얼.pdf"
            )
            st.caption("※ 다운로드 후 브라우저 또는 PDF 뷰어에서 열어주세요.")
        else:
            st.warning("assets/manual.pdf 파일을 찾을 수 없습니다.")

    # ============================
    # 서비스 이용 안내
    # ============================
    st.markdown("""
### 서비스 이용 안내
- 본 서비스는 **관리카드 자동 작성을 위한 사내 업무 지원 도구**입니다.
- 입력 데이터는 **지정된 결합용 Excel 양식**만 지원합니다.
- 매크로 설치 및 실행 전 **PowerPoint는 반드시 종료**되어 있어야 합니다.
- 템플릿 버전, 폰트 설치 여부, 사용자 환경에 따라 **결과 레이아웃이 달라질 수 있습니다**.
- 자동 생성 결과물에 대해서는 **최종 검토 및 수정이 필요합니다**.
- 본 도구는 **사내 업무 목적에 한해 사용**하며, 외부 배포를 금합니다.
""")

    # ============================
    # 다운로드
    # ============================
    st.markdown("### 다운로드")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**PPT 매크로**")
        download_button(
            label="PPT 매크로 다운로드",
            file_path=MACRO_PACK,
            mime="application/zip",
            download_name="관리카드자동작성.zip"
        )

    with col2:
        st.markdown("**결합용 엑셀 양식**")
        download_button(
            label="엑셀 양식 다운로드",
            file_path=EXCEL_TEMPLATE,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            download_name="결합용엑셀.xlsx"
        )

    st.caption("※ 배포 파일 교체 시 assets 폴더의 파일만 교체하면 됩니다.")
