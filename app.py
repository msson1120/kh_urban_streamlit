# app.py
import streamlit as st

APP_TITLE = "(주)건화 업무자동화 포털"
PASSWORD = "126791"

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
html, body, [class*="css"] { font-size: 16px; }
h1 { font-size: 2.2rem !important; font-weight: 800 !important; }
h3 { font-size: 1.25rem !important; font-weight: 800 !important; margin-top: 1.2rem; }
p, li { line-height: 1.6; }
hr { margin: 0.8rem 0; }
</style>
""", unsafe_allow_html=True)

# ============================
# 비밀번호 게이트
# ============================
pw = st.text_input("비밀번호를 입력하세요", type="password")
if pw != PASSWORD:
    st.warning("올바른 비밀번호를 입력하세요.")
    st.stop()

# ============================
# 서비스 UI 함수 (여기에 각 코드 본문을 넣을 자리)
# ============================
def service_registry_merge():
    st.subheader("🧾 등기부등본 통합분석기")
    st.caption("Excel.zip + PDF.zip 업로드 → 통합 결과 ZIP 다운로드")
    st.info("여기에 '등기부등본 통합분석기' 본문 코드를 그대로 넣으면 됩니다.")

def service_management_card():
    st.subheader("📄 관리카드 자동작성")
    st.caption("매뉴얼/매크로/양식 다운로드")
    st.info("여기에 '관리카드 자동작성' 본문 코드를 그대로 넣으면 됩니다.")

# ============================
# 사이드바: 선택 가능한 메뉴(라디오)
# ============================
with st.sidebar:
    st.header("📂 서비스 메뉴")
    service = st.radio(
        "서비스 선택",
        ["등기부등본 통합분석기", "관리카드 자동작성"],
        index=0,
        label_visibility="collapsed"
    )
    st.divider()
    st.caption("서비스를 선택하면 본문이 전환됩니다.")

# ============================
# 메인: 선택값에 따라 라우팅
# ============================
st.title("🏢 (주)건화 업무자동화 포털")

if service == "등기부등본 통합분석기":
    service_registry_merge()
else:
    service_management_card()
