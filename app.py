import streamlit as st

APP_TITLE = "(주)건화 AI Assistant HUB"
PASSWORD = "126791"

# ============================
# 기본 설정
# ============================
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================
# PRO DESIGN SYSTEM (Light / Dark Auto)
# ============================
st.markdown("""
<style>
:root {
  --bg-main: #ffffff;
  --bg-soft: #f7f8fa;
  --border: rgba(0,0,0,.08);
  --text-main: rgba(0,0,0,.88);
  --text-sub: rgba(0,0,0,.55);
  --accent: #2563eb;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg-main: #0e1117;
    --bg-soft: #161b22;
    --border: rgba(255,255,255,.12);
    --text-main: rgba(255,255,255,.92);
    --text-sub: rgba(255,255,255,.55);
    --accent: #60a5fa;
  }
}

/* ---- Base ---- */
html, body, [class*="css"] {
  font-size: 16px;
  color: var(--text-main);
}
.block-container {
  max-width: 1200px;
  padding-top: 2rem;
  padding-bottom: 2.5rem;
}
hr { opacity:.3; }

/* ---- Typography ---- */
h1 { font-size: 2.25rem !important; font-weight: 900 !important; }
h3 { font-size: 1.15rem !important; font-weight: 800 !important; }
.small { color: var(--text-sub); font-size: .92rem; }

/* ---- Hero ---- */
.hero {
  background:
    radial-gradient(1200px 200px at 20% -10%, rgba(37,99,235,.12), transparent),
    var(--bg-soft);
  border: 1px solid var(--border);
  border-radius: 22px;
  padding: 26px 26px 22px 26px;
  margin-bottom: 18px;
}
.hero-row {
  display:flex;
  justify-content: space-between;
  gap: 20px;
}
.hero-left {
  display:flex;
  gap:14px;
}
.hero-icon {
  width: 48px; height: 48px;
  border-radius: 16px;
  background: var(--bg-main);
  border: 1px solid var(--border);
  display:flex;
  align-items:center;
  justify-content:center;
  font-size: 1.3rem;
}
.badges {
  display:flex;
  gap:10px;
  margin-top:10px;
}
.badge {
  padding:6px 12px;
  border-radius:999px;
  border:1px solid var(--border);
  background: var(--bg-main);
  font-size:.85rem;
  font-weight:800;
}

/* ---- Notice ---- */
.notice {
  background: linear-gradient(180deg, rgba(37,99,235,.10), transparent);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 16px 18px;
  margin-bottom: 20px;
}

/* ---- Service Cards ---- */
.grid {
  display:grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 16px;
}
.card {
  background: var(--bg-main);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 18px;
  transition: all .2s ease;
}
.card:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 28px rgba(0,0,0,.15);
}
.card-title {
  font-weight:900;
  margin-bottom:4px;
}
.card-desc {
  font-size:.9rem;
  color: var(--text-sub);
  line-height:1.5;
}

/* ---- Sidebar ---- */
section[data-testid="stSidebar"] {
  background: var(--bg-soft);
  border-right: 1px solid var(--border);
}
.sidebar-title {
  font-weight:900;
  margin-bottom:10px;
}
.sidebar-meta {
  font-size:.8rem;
  color: var(--text-sub);
  margin-bottom:12px;
}

/* ---- Alerts / Inputs ---- */
div[data-testid="stAlert"] {
  border-radius: 16px;
}
</style>
""", unsafe_allow_html=True)

# ============================
# 인증 (유지)
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
# Sidebar (기능 동일)
# ============================
with st.sidebar:
    st.markdown('<div class="sidebar-title">🏢 Geonhwa Automation</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-meta">INTERNAL SYSTEM · v1.0</div>', unsafe_allow_html=True)

    st.page_link("pages/0_home.py", label="🏠 HOME", icon="🏠")
    st.page_link("pages/1_registry.py", label="🧾 등기부등본 통합분석기", icon="🧾")
    st.page_link("pages/2_card.py", label="📄 관리카드 자동작성", icon="📄")

    st.divider()
    st.caption("※ 좌측 메뉴에서 서비스 선택")

# ============================
# Main Entry (Dashboard Style)
# ============================
st.markdown("""
<div class="hero">
  <div class="hero-row">
    <div class="hero-left">
      <div class="hero-icon">🏢</div>
      <div>
        <h1>(주)건화 업무자동화 포털</h1>
        <div class="small">사내 반복업무 제거 · 산출물 품질 표준화 · 실무 중심 AI 자동화</div>
        <div class="badges">
          <div class="badge">AUTOMATION</div>
          <div class="badge">ENGINEERING</div>
          <div class="badge">PRODUCTION</div>
        </div>
      </div>
    </div>
    <div class="small" style="text-align:right;">
      SYSTEM ENTRY<br/>LEFT MENU →
    </div>
  </div>
</div>

<div class="notice">
  <b>안내</b><br/>
  본 화면은 시스템 진입용 대시보드입니다.<br/>
  실제 업무는 좌측 메뉴 또는 각 서비스 페이지에서 수행합니다.
</div>

<div class="grid">
  <div class="card">
    <div class="card-title">🧾 등기부등본 통합분석기</div>
    <div class="card-desc">
      다수 PDF 등기부등본을 자동 분석하여<br/>
      표준 Excel 산출물로 일괄 정리합니다.
    </div>
  </div>
  <div class="card">
    <div class="card-title">📄 관리카드 자동작성</div>
    <div class="card-desc">
      엑셀 입력값을 기반으로<br/>
      PowerPoint 관리카드를 자동 생성합니다.
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
