import streamlit as st
from datetime import datetime

# ===== HOME 기본 설정 =====
st.set_page_config(
    page_title="(주)건화 업무자동화 포털 - HOME",
    page_icon="🏢",
    layout="wide"
)

# ===== PRO UI (Light/Dark Auto) =====
st.markdown("""
<style>
:root{
  --bg: #ffffff;
  --soft: #f7f8fa;
  --card: #ffffff;
  --bd: rgba(0,0,0,.08);
  --txt: rgba(0,0,0,.88);
  --sub: rgba(0,0,0,.55);
  --blue: #2563eb;
  --blue2: rgba(37,99,235,.10);
  --shadow: 0 10px 26px rgba(0,0,0,.10);
}
@media (prefers-color-scheme: dark){
  :root{
    --bg:#0e1117;
    --soft:#161b22;
    --card:#0e1117;
    --bd: rgba(255,255,255,.12);
    --txt: rgba(255,255,255,.92);
    --sub: rgba(255,255,255,.55);
    --blue:#60a5fa;
    --blue2: rgba(96,165,250,.12);
    --shadow: 0 14px 30px rgba(0,0,0,.45);
  }
}

/* Layout */
.block-container{ max-width: 1180px; padding-top: 2rem; padding-bottom: 2.2rem; }
hr{ opacity:.28; }

/* Typography */
html, body, [class*="css"]{ font-size: 16px; color: var(--txt); }
h1{ font-size: 2.2rem !important; font-weight: 900 !important; margin: 0 !important; letter-spacing: -0.4px; }
h2{ font-size: 1.3rem !important; font-weight: 900 !important; letter-spacing: -0.2px; margin-top: 1.0rem; }
.small{ color: var(--sub); font-size: .92rem; }

/* Hero */
.hero{
  background:
    radial-gradient(1100px 220px at 18% -10%, var(--blue2), transparent),
    linear-gradient(180deg, rgba(0,0,0,.02), transparent),
    var(--soft);
  border: 1px solid var(--bd);
  border-radius: 22px;
  padding: 22px 22px 18px 22px;
  margin-bottom: 14px;
}
.hero-row{ display:flex; align-items:flex-start; justify-content:space-between; gap: 14px; }
.hero-left{ display:flex; gap: 14px; align-items:flex-start; }
.hero-icon{
  width: 48px; height: 48px;
  border-radius: 16px;
  background: var(--card);
  border: 1px solid var(--bd);
  display:flex; align-items:center; justify-content:center;
  font-size: 1.35rem;
}
.badges{ display:flex; gap:10px; flex-wrap:wrap; margin-top: 10px; }
.badge{
  display:inline-flex; align-items:center; gap:8px;
  padding: 6px 12px;
  border-radius: 999px;
  border: 1px solid var(--bd);
  background: var(--card);
  font-size: .85rem;
  font-weight: 900;
}
.dot{ width:8px; height:8px; border-radius:999px; background: var(--blue); opacity:.9; }

/* Notice */
.notice{
  border: 1px solid var(--bd);
  background: linear-gradient(180deg, var(--blue2), transparent);
  border-radius: 18px;
  padding: 14px 16px;
  margin: 12px 0 18px 0;
}
.notice-title{ font-weight: 900; margin-bottom: 6px; }
.notice-body{ color: var(--txt); opacity:.9; line-height: 1.65; }

/* Cards */
.cards-wrap{
  display:grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 16px;
  margin-top: 8px;
}
.card{
  border: 1px solid var(--bd);
  background: var(--card);
  border-radius: 20px;
  padding: 18px;
  transition: all .18s ease;
}
.card:hover{
  transform: translateY(-3px);
  box-shadow: var(--shadow);
}
.card-top{ display:flex; justify-content:space-between; gap: 10px; align-items:flex-start; }
.card-title{ font-size: 1.35rem; font-weight: 950; letter-spacing: -0.3px; margin: 0; }
.card-desc{ color: var(--sub); font-size: .92rem; line-height: 1.55; margin-top: 8px; }
.bullets{ margin: 10px 0 0 0; padding-left: 18px; color: var(--txt); opacity:.9; line-height: 1.6; }
.kicker{
  font-size: .82rem;
  font-weight: 900;
  color: var(--sub);
  border: 1px solid var(--bd);
  background: var(--soft);
  padding: 6px 10px;
  border-radius: 999px;
  height: fit-content;
}

/* Streamlit link button polish */
div[data-testid="stPageLink"] a{
  display:inline-flex !important;
  align-items:center !important;
  gap:8px !important;
  padding: 10px 14px !important;
  border-radius: 14px !important;
  border: 1px solid var(--bd) !important;
  background: var(--soft) !important;
  font-weight: 900 !important;
  text-decoration: none !important;
}
div[data-testid="stPageLink"] a:hover{
  border-color: rgba(37,99,235,.35) !important;
}
</style>
""", unsafe_allow_html=True)

# ===== 데이터(표시용) =====
updated = datetime.now().strftime("%Y-%m-%d %H:%M")

# ===== HERO =====
st.markdown(f"""
<div class="hero">
  <div class="hero-row">
    <div class="hero-left">
      <div class="hero-icon">🏢</div>
      <div>
        <h1>(주)건화 업무자동화 포털</h1>
        <div class="small">필요한 서비스를 선택하고, 표준 산출물로 빠르게 마무리합니다.</div>
        <div class="badges">
          <span class="badge"><span class="dot"></span>AUTOMATION</span>
          <span class="badge"><span class="dot"></span>ENGINEERING</span>
          <span class="badge"><span class="dot"></span>v1.0</span>
        </div>
      </div>
    </div>
    <div class="small" style="text-align:right;">
      업데이트: <b>{updated}</b><br/>
      HOME
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ===== SERVICE (기존 내용 유지) =====
st.markdown("<h2>SERVICE</h2>", unsafe_allow_html=True)
st.markdown("<div class='small' style='margin-top:4px;'>필요한 서비스 메뉴의 <b>실행하기</b> 버튼을 누르세요.</div>", unsafe_allow_html=True)

# 기존 안내 문구 유지
st.markdown("""
<div class="notice">
  <div class="notice-title">※ 파일 업로드 전, 양식/매뉴얼 먼저 확인</div>
  <div class="notice-body">
    좌측 <b>서비스 메뉴</b>에서 프로그램을 선택하세요.<br/>
    실제 작업은 <b>각 서비스 페이지</b>에서 진행합니다.
  </div>
</div>
""", unsafe_allow_html=True)

# ===== 카드 영역 (기존 내용 유지) =====
st.markdown("""
<div class="cards-wrap">
  <div class="card">
    <div class="card-top">
      <div>
        <div class="card-title">🧾 등기부등본 통합분석기</div>
        <div class="card-desc">Excel.zip + PDF.zip 업로드 → 통합 결과 ZIP 다운로드</div>
      </div>
      <div class="kicker">BATCH · PDF→EXCEL</div>
    </div>
    <ul class="bullets">
      <li>등기사항전부증명서(열람용) Excel 변환본만 지원</li>
      <li>주요 등기사항 요약 페이지 포함 필수</li>
      <li>PDF는 주소 기반 파일명 일괄 변경 포함</li>
    </ul>
  </div>

  <div class="card">
    <div class="card-top">
      <div>
        <div class="card-title">📄 관리카드 자동작성</div>
        <div class="card-desc">매뉴얼/매크로/결합용 엑셀 양식 다운로드</div>
      </div>
      <div class="kicker">PPT · TEMPLATE</div>
    </div>
    <ul class="bullets">
      <li>PowerPoint는 실행 전 반드시 종료</li>
      <li>결합용 엑셀 양식만 지원</li>
      <li>결과물은 최종 검토/수정 필요</li>
    </ul>
  </div>
</div>
""", unsafe_allow_html=True)

# 버튼(페이지 이동) - 기능상 동일: 각 페이지로 가는 실행 트리거
c1, c2 = st.columns(2)
with c1:
    st.page_link("pages/1_registry.py", label="▷ 실행하기", use_container_width=False)
with c2:
    st.page_link("pages/2_card.py", label="▷ 실행하기", use_container_width=False)

st.markdown("<hr/>", unsafe_allow_html=True)

with st.expander("📌 문의 · 운영 안내", expanded=False):
    st.markdown("""
    <div style="
        border:1px solid rgba(0,0,0,.08);
        border-radius:16px;
        padding:16px;
        background: rgba(0,0,0,.02);
        line-height:1.65;
    ">
        <b>문의</b><br/>
        · 오류 발생 시: 담당자에게 화면 캡처 전달<br/>
        · 파일 업로드 오류: 파일명/확장자/압축 구조 확인<br/><br/>

        <b>운영 리스트</b><br/>
        · 본 포털은 내부 업무 자동화 용도로만 사용<br/>
        · 결과물은 반드시 최종 검토 후 사용<br/>
        · 매뉴얼/양식 미준수 시 오류 발생 가능
    </div>
    """, unsafe_allow_html=True)
