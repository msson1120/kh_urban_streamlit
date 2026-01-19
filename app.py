# app.py
import streamlit as st

APP_TITLE = "(주)건화 업무자동화 포털"
PASSWORD = "126791"

st.set_page_config(page_title=APP_TITLE, page_icon="🏢", layout="wide")

# 공통 테마(앞에서 맞춘 톤)
st.markdown("""
<style>
html, body, [class*="css"] { font-size: 16px; }
h1 { font-size: 2.2rem !important; font-weight: 800 !important; }
h3 { font-size: 1.25rem !important; font-weight: 800 !important; margin-top: 1.2rem; }
p, li { line-height: 1.6; }
hr { margin: 0.8rem 0; }
</style>
""", unsafe_allow_html=True)

# 비밀번호(공통 게이트)
pw = st.text_input("비밀번호를 입력하세요", type="password")
if pw != PASSWORD:
    st.warning("올바른 비밀번호를 입력하세요.")
    st.stop()

st.title("🏢 (주)건화 업무자동화 포털")
st.markdown("""
### 서비스 선택
왼쪽 사이드바에서 서비스를 선택하세요.
- **등기부등본 통합분석기**: Excel.zip + PDF.zip 업로드 → 통합 결과 ZIP 다운로드
- **관리카드 자동작성**: 매뉴얼/매크로/양식 다운로드
""")

st.info("좌측 메뉴가 안 보이면, 좌상단 ‘☰’ 버튼을 눌러 펼치세요.")
