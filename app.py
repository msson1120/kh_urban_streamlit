import streamlit as st

APP_TITLE = "(주)건화 AI Assistant HUB"
PASSWORD = "126791"

# ============================
# 기본 설정 (엔트리 전용)
# ============================
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================
# 공통 UI 스타일
# ============================
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
# 인증 (세션 유지)
# ============================
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

# ============================
# 첫 진입을 HOME으로 강제 (핵심)
# - 인증 후 1회만 리다이렉트
# ============================
if "did_redirect_home" not in st.session_state:
    st.session_state.did_redirect_home = True
    st.switch_page("pages/0_home.py")

# ============================
# 사이드바: 서비스 메뉴 (공식 네비)
# (혹시 리다이렉트가 막히는 환경 대비해 유지)
# ============================
with st.sidebar:
    st.page_link("pages/0_home.py", label="🏠 HOME", icon="🏠")
    st.page_link("pages/1_registry.py", label="🧾 등기부등본 통합분석기", icon="🧾")
    st.page_link("pages/2_card.py", label="📄 관리카드 자동작성", icon="📄")

    st.divider()
    st.caption("※ 메뉴가 접혀 있으면 좌상단 ☰ 버튼을 누르세요.")

# ============================
# 본문: app 페이지는 '안내 전용'
# (리다이렉트 실패 시에만 보이게 되는 백업 화면)
# ============================
st.title("🏢 (주)건화 업무자동화 포털")

st.info(
    "좌측 **서비스 메뉴**에서 프로그램을 선택하세요.\n\n"
    "이 화면(app)은 시스템 엔트리 페이지이며,\n"
    "실제 작업은 **메인화면 또는 각 서비스 페이지**에서 진행합니다."
)
