# app.py
import streamlit as st

from services.registry_app import run as run_registry   # 등기부등본용(너가 다음에 넣을 파일)
from services.card_app import run as run_card           # 관리카드용(아래 제공)

APP_TITLE = "(주)건화 업무자동화 포털"
PASSWORD = "126791"

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 공통 테마(여기서만)
st.markdown("""
<style>
html, body, [class*="css"] { font-size: 16px; }
h1 { font-size: 2.2rem !important; font-weight: 800 !important; }
h3 { font-size: 1.25rem !important; font-weight: 800 !important; margin-top: 1.2rem; }
p, li { line-height: 1.6; }
hr { margin: 0.8rem 0; }
</style>
""", unsafe_allow_html=True)

# 비번: 세션 저장(페이지 전환해도 유지)
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    pw = st.text_input("비밀번호를 입력하세요", type="password")
    if pw == PASSWORD:
        st.session_state.auth = True
        st.rerun()
    else:
        st.warning("올바른 비밀번호를 입력하세요.")
        st.stop()

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

st.title("🏢 (주)건화 업무자동화 포털")

if service == "등기부등본 통합분석기":
    run_registry()
else:
    run_card()
