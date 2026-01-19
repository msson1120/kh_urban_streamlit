# pages/0_home.py
import streamlit as st
from datetime import datetime

PORTAL_TITLE = "(주)건화 업무자동화 포털"

def badge(text: str):
    st.markdown(
        f"""
        <span style="
            display:inline-block;
            padding:4px 10px;
            border-radius:999px;
            background:#F3F4F6;
            border:1px solid #E5E7EB;
            font-size:0.9rem;
            font-weight:700;
        ">{text}</span>
        """,
        unsafe_allow_html=True
    )

def service_card(title, icon, desc, bullets, page_path, button_label):
    with st.container(border=True):
        st.markdown(f"### {icon} {title}")
        st.caption(desc)
        st.markdown("\n".join([f"- {b}" for b in bullets]))
        st.page_link(page_path, label=button_label, use_container_width=True)

# ============================
# 메인 헤더
# ============================
st.title(f"🏢 {PORTAL_TITLE}")

cols = st.columns([1, 1, 1, 2])
with cols[0]:
    badge("INTERNAL")
with cols[1]:
    badge("STREAMLIT")
with cols[2]:
    badge("v1.0")
with cols[3]:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    st.caption(f"업데이트: {now} (로컬 기준)")

st.markdown("""
### 오늘 할 일
좌측 **서비스 메뉴**에서 프로그램을 선택하거나, 아래 **바로가기** 버튼을 누르세요.
""")

# ============================
# 바로가기 (핵심 CTA)
# ============================
cta1, cta2, cta3 = st.columns([1, 1, 1])

with cta1:
    st.page_link("pages/1_registry.py", label="🧾 등기부등본 통합분석기 바로가기", use_container_width=True)
with cta2:
    st.page_link("pages/2_card.py", label="📄 관리카드 자동작성 바로가기", use_container_width=True)
with cta3:
    st.info("※ 파일 업로드 전, 양식/매뉴얼 먼저 확인")

st.divider()

# ============================
# 서비스 요약 카드 (포털 느낌)
# ============================
left, right = st.columns([1, 1])

with left:
    service_card(
        title="등기부등본 통합분석기",
        icon="🧾",
        desc="Excel.zip + PDF.zip 업로드 → 통합 결과 ZIP 다운로드",
        bullets=[
            "등기사항전부증명서(열람용) Excel 변환본만 지원",
            "주요 등기사항 요약 페이지 포함 필수",
            "PDF는 주소 기반 파일명 일괄 변경 포함"
        ],
        page_path="pages/1_registry.py",
        button_label="🧾 실행하기"
    )

with right:
    service_card(
        title="관리카드 자동작성",
        icon="📄",
        desc="매뉴얼/매크로/결합용 엑셀 양식 다운로드",
        bullets=[
            "PowerPoint는 실행 전 반드시 종료",
            "결합용 엑셀 양식만 지원",
            "결과물은 최종 검토/수정 필요"
        ],
        page_path="pages/2_card.py",
        button_label="📄 실행하기"
    )

st.divider()

# ============================
# 운영/품질 체크리스트
# ============================
with st.expander("✅ 운영 체크리스트", expanded=False):
    st.markdown("""
- **업로드 파일명/확장자** 확인 (zip 내부에 xlsx / pdf가 들어있는지)
- 분석 결과는 **원본대조 검토** (등기부 특성상 누락 가능)
- 오류 발생 시: Streamlit Cloud → **Manage app → Logs** 확인 후 공유
- 배포 파일 교체 시: `assets/` 폴더 파일만 교체
""")

# ============================
# 공지/문의
# ============================
with st.expander("📌 공지 / 문의", expanded=False):
    st.markdown("""
- 본 포털은 **사내 업무 목적**으로만 사용합니다. 외부 배포 금지.
- 개선 요청/버그 제보는 **오류 화면 캡처 + Logs**와 함께 남겨주세요.
""")
