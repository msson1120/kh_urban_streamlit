import streamlit as st

APP_TITLE = "KH-Urban AI Assistant HUB"
PASSWORD = "126791"

# ============================
# 기본 설정 (엔트리 전용)
# ============================
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="assets/kunhwa_icon_512.png",
    layout="wide"
)

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
# HOME으로 1회 강제 이동
# ============================
if "did_redirect_home" not in st.session_state:
    st.session_state.did_redirect_home = True
    st.switch_page("pages/0_home.py")

# ============================
# (의도적으로 아무 UI도 두지 않음)
# 이 파일은 '게이트' 역할만 수행
# ============================
st.stop()
