import streamlit as st
from datetime import datetime
import base64
import os

# ===== 유틸: 이미지 -> base64 (Streamlit HTML에서 깨짐 방지) =====
def img_to_base64(path: str) -> str:
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

# 로고 base64 준비 (HERO에서 사용)
LOGO_PATH = "assets/kunhwa_icon_512.png"
logo_base64 = img_to_base64(LOGO_PATH)
logo_data_uri = f"data:image/png;base64,{logo_base64}" if logo_base64 else ""

# ===== HOME 기본 설정 =====
st.set_page_config(
    page_title="KH-Urban AI Assistant - HOME",
    page_icon=LOGO_PATH,  # 탭 아이콘은 PNG 경로 그대로 OK
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
}
.hero-logo{
  width: 34px;
  height: 34px;
  object-fit: contain;
  display:block;
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

/* 실행하기 버튼 영역 간격 */
.actions{ margin-top: 14px; }

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
from zoneinfo import ZoneInfo
updated = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")


# ===== HERO =====
# logo_data_uri가 비어있으면(파일없음) 깨진 이미지 대신 fallback 이모지 표시
hero_icon_html = (
    f'<img src="{logo_data_uri}" class="hero-logo" />'
    if logo_data_uri
    else '<span style="font-size:1.35rem;">🏢</span>'
)

st.markdown(f"""
<div class="hero">
  <div class="hero-row">
    <div class="hero-left">
      <div class="hero-icon">
        {hero_icon_html}
      </div>
      <div>
        <h1>KH-Urban AI Assistant HUB</h1>
        <div class="small">made by 손명선</div>
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
    하단 <b>서비스 메뉴</b>에서 프로그램을 선택하세요.<br/>
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
        <div class="card-title">🧾 등기부등본 통합분석</div>
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

# 버튼(페이지 이동) - 기능상 동일
st.markdown('<div class="actions">', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    st.page_link("pages/1_registry.py", label="▷ 실행하기", use_container_width=False)
with c2:
    st.page_link("pages/2_card.py", label="▷ 실행하기", use_container_width=False)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<hr/>", unsafe_allow_html=True)

with st.expander("📌 문의", expanded=False):
    st.markdown("""
    <div style="
        border:1px solid rgba(0,0,0,.08);
        border-radius:16px;
        padding:16px;
        margin-bottom:12px; 
        background: rgba(0,0,0,.02);
        line-height:1.65;
    ">
        <b>문의</b><br/>
        · 개선 요청 / 버그 제보는 오류 화면 캡쳐 후 <b>손명선 사원</b>에게 화면 캡처 전달<br/>
        · 문의 : msson2802@kunhwaeng.co.kr / 010-7178-6098
    </div>
    """, unsafe_allow_html=True)

with st.expander("📢 공지", expanded=False):
    st.markdown("""
    <div style="
        border:1px solid rgba(0,0,0,.08);
        border-radius:16px;
        padding:16px;
        margin-bottom:12px; 
        background: rgba(0,0,0,.02);
        line-height:1.65;
    ">
        <b>공지</b><br/>
        · 본 포털은 <b>사내 업무 목적으로만</b> 사용<br/>
        · 업로드 파일명 / 확장자 사전 확인<br/>
        · 결과물은 반드시 최종 검토 후 사용<br/>
        · 매뉴얼 / 양식 미준수 시 오류 발생 가능
    </div>
    """, unsafe_allow_html=True)
