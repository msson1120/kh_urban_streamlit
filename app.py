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
# 비밀번호(세션 유지)
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
# 사이드바: 서비스 메뉴(프로그램 목록)
# ============================
with st.sidebar:
    st.markdown("## 📂 서비스 메뉴")
    st.caption("아래에서 프로그램을 선택하세요.")

    # ✅ 핵심: pages 파일로 이동하는 네비 버튼
    # 페이지 파일명과 정확히 맞춰야 함
    st.page_link("pages/0_메인화면.py", label="🏠 메인화면", icon="🏠")
    st.page_link("pages/1_등기부등본_통합분석기.py", label="🧾 등기부등본 통합분석기", icon="🧾")
    st.page_link("pages/2_관리카드_자동작성.py", label="📄 관리카드 자동작성", icon="📄")

    st.divider()
    st.caption("※ 메뉴가 접혀 있으면 좌상단 ☰ 버튼을 누르세요.")

# ============================
# 본문(랜딩)
# ============================
st.title("🏢 (주)건화 업무자동화 포털")
st.markdown("""
### 사용 방법
좌측 **서비스 메뉴**에서 프로그램을 선택하세요.

- **등기부등본 통합분석기**: Excel.zip + PDF.zip 업로드 → 통합 결과 ZIP 다운로드  
- **관리카드 자동작성**: 매뉴얼 / 매크로 / 엑셀 양식 다운로드
""")
