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

# 공통 테마
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
# 비밀번호: 세션 저장(페이지 이동해도 유지)
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
# 사이드바 안내 (pages 메뉴는 Streamlit이 자동 생성)
# ============================
with st.sidebar:
    st.header("📂 서비스 메뉴")
    st.caption("아래 'Pages' 목록에서 서비스를 클릭하세요.")
    st.divider()
    st.caption("※ 메뉴가 접혀 있으면 좌상단 ☰ 버튼을 누르세요.")

# ============================
# 메인 랜딩
# ============================
st.title("🏢 (주)건화 업무자동화 포털")

st.markdown("""
### 서비스 선택
왼쪽 사이드바의 **Pages 메뉴**에서 서비스를 선택하세요.

- **등기부등본_통합분석기**  
  Excel.zip + PDF.zip 업로드 → 통합 결과 ZIP 다운로드

- **관리카드_자동작성**  
  매뉴얼 / PPT 매크로 / 결합용 엑셀 양식 다운로드
""")

st.info("Pages 메뉴가 안 보이면, 좌상단 ☰ 버튼으로 사이드바를 펼치세요.")
