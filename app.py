import streamlit as st
import streamlit.components.v1 as components
from pipeline import run_research_pipeline

st.set_page_config(
    page_title="InsightFlow Research",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

PAGE_STYLE = """
<style>
:root {
    --bg: #081b2b;
    --card: rgba(255,255,255,0.08);
    --text: #f8fafc;
    --muted: #a6b8cf;
    --accent: #56ccf2;
    --accent2: #2f80ed;
}

body, .block-container {
    background: radial-gradient(circle at top left, rgba(48, 146, 255, 0.16), transparent 25%),
                radial-gradient(circle at bottom right, rgba(119, 99, 255, 0.16), transparent 30%),
                linear-gradient(135deg, #0c2034 0%, #081b2b 100%);
    color: var(--text);
}

.stButton>button {
    background: linear-gradient(90deg, #2f80ed 0%, #56ccf2 100%);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 0.8rem 1.75rem;
    font-weight: 600;
    transition: transform 0.24s ease, box-shadow 0.24s ease;
}

.stButton>button:hover {
    transform: translateY(-1px) scale(1.01);
    box-shadow: 0 18px 40px rgba(40, 116, 255, 0.28);
}

.hero-card, .result-card, .small-card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 26px;
    padding: 2rem;
    box-shadow: 0 20px 80px rgba(0, 0, 0, 0.24);
    backdrop-filter: blur(18px);
}

.hero-card {
    animation: float 10s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-14px); }
}

.interactive-panel {
    border-radius: 26px;
    position: relative;
    overflow: hidden;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.16);
}

.interactive-panel::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at center, rgba(86, 204, 242, 0.28), transparent 32%);
    opacity: 0.6;
    pointer-events: none;
}

.interactive-card {
    width: 100%;
    min-height: 240px;
    border-radius: 26px;
    background: linear-gradient(180deg, rgba(16, 56, 100, 0.96), rgba(8, 19, 43, 0.88));
    padding: 1.75rem;
    color: #e9f4ff;
    transition: transform 0.22s ease, box-shadow 0.22s ease;
    transform-style: preserve-3d;
}

.interactive-card:hover {
    transform: translateY(-12px) rotateX(2deg) rotateY(6deg);
    box-shadow: 0 28px 80px rgba(16, 70, 140, 0.35);
}

.card-title {
    font-size: 2rem;
    margin-bottom: 0.75rem;
}

.card-copy {
    color: #c8d9ee;
    line-height: 1.75;
}

.highlight {
    color: #56ccf2;
    font-weight: 700;
}

.report-block {
    border-radius: 24px;
    padding: 1.5rem;
    background: rgba(7, 17, 32, 0.92);
    border: 1px solid rgba(255,255,255,0.08);
}

.result-heading {
    color: #f7fbff;
    margin-bottom: 0.8rem;
    letter-spacing: 0.03em;
}

.code-highlight {
    color: #56ccf2;
}
</style>
"""

st.markdown(PAGE_STYLE, unsafe_allow_html=True)

st.markdown("""
<div class="hero-card">
    <div style="display:flex; justify-content:space-between; align-items:center; gap:2rem; flex-wrap:wrap;">
        <div style="max-width:600px;">
            <h1 style="font-size:3.5rem; margin:0;">InsightFlow Research</h1>
            <p class="card-copy" style="font-size:1.15rem; margin-top:1rem;">
                A modern research dashboard for exploring topics, summarizing key insights, and generating elegant reports in one smooth flow.
            </p>
            <div style="display:flex; gap:1rem; flex-wrap:wrap; margin-top:1.75rem;">
                <span style="background: rgba(86,204,242,0.12); color: #56ccf2; padding:0.7rem 1rem; border-radius:999px; font-weight:600;">Animated experience</span>
                <span style="background: rgba(127, 91, 255, 0.12); color: #8b7cff; padding:0.7rem 1rem; border-radius:999px; font-weight:600;">Interactive insights</span>
            </div>
        </div>
        <div style="min-width:280px; max-width:380px;">
            <div class="interactive-card">
                <h3 class="card-title">Bring research to life</h3>
                <p class="card-copy">Hover over the panel below and watch the interface respond with smooth motion and subtle depth.</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

with st.container():
    left, right = st.columns([3, 2])
    with left:
        st.markdown("### Start your research journey")
        topic = st.text_input("Enter your research topic", "Artificial Intelligence", help="Type the topic you want to research.")
        run_button = st.button("Generate Report")
        if run_button and topic:
            st.session_state.topic = topic
            st.session_state.loading = True
            st.session_state.result = None

    with right:
        st.markdown("### Why InsightFlow")
        st.markdown("""
        - **Fast reports** with clear structure and source-aware summaries.
        - **Modern interface** with motion, hover, and layered cards.
        - **Intuitive flow** for both experts and non-technical users.
        """)

if "topic" not in st.session_state:
    st.session_state.topic = None

if "result" not in st.session_state:
    st.session_state.result = None

if run_button and topic:
    with st.spinner("Gathering insights and drafting your report..."):
        result = run_research_pipeline(topic)
        st.session_state.result = result
        st.session_state.loading = False
        st.balloons()

if st.session_state.result:
    result = st.session_state.result
    st.markdown("<div class='report-block'>", unsafe_allow_html=True)
    st.markdown(f"<h2 class='result-heading'>Research Summary for <span class='highlight'>{st.session_state.topic}</span></h2>", unsafe_allow_html=True)
    with st.expander("Search Results", expanded=False):
        st.write(result.get("search_results", "No search results available."))
    with st.expander("Scraped Content", expanded=False):
        st.write(result.get("scraped_content", "No scraped content available."))
    with st.expander("Final Report", expanded=True):
        st.write(result.get("report", "No report generated."))
    with st.expander("Critic Feedback", expanded=False):
        st.write(result.get("feedback", "No critic feedback available."))
    st.markdown("</div>", unsafe_allow_html=True)

components.html(
    """
    <div class='interactive-panel' style='padding: 24px; margin-top: 32px;'>
      <div id='hover-card' style='width:100%; height:260px; border-radius:24px; background: linear-gradient(135deg, rgba(86,204,242,0.18), rgba(79,70,229,0.16)); display:flex; align-items:center; justify-content:center; color:#eaf4ff; font-size:1.15rem; transition: transform 0.2s ease, box-shadow 0.2s ease;'>
        Move your cursor over this card to see motion in action.
      </div>
    </div>
    <script>
      const card = document.getElementById('hover-card');
      card.addEventListener('mousemove', (event) => {
        const rect = card.getBoundingClientRect();
        const x = event.clientX - rect.left - rect.width / 2;
        const y = event.clientY - rect.top - rect.height / 2;
        card.style.transform = `perspective(800px) rotateX(${(-y / 18).toFixed(2)}deg) rotateY(${(x / 18).toFixed(2)}deg)`;
        card.style.boxShadow = `${-x / 15}px ${y / 15}px 40px rgba(22, 116, 229, 0.28)`;
      });
      card.addEventListener('mouseleave', () => {
        card.style.transform = 'perspective(800px) rotateX(0deg) rotateY(0deg)';
        card.style.boxShadow = '0 24px 80px rgba(0, 0, 0, 0.18)';
      });
    </script>
    """,
    height=340,
    scrolling=False,
)

st.markdown("""
<div style='display:flex; gap:1rem; flex-wrap:wrap; margin-top:2rem;'>
  <div class='small-card' style='flex:1 1 240px;'>
    <h4>Interactive Design</h4>
    <p class='card-copy'>Motion and hover cues help the interface feel responsive, not robotic.</p>
  </div>
  <div class='small-card' style='flex:1 1 240px;'>
    <h4>Readable Results</h4>
    <p class='card-copy'>Structured output sections make it easy to scan research and validate sources.</p>
  </div>
  <div class='small-card' style='flex:1 1 240px;'>
    <h4>Smart Workflow</h4>
    <p class='card-copy'>Search, scrape, write, and critique — all from one elegant dashboard.</p>
  </div>
</div>
""", unsafe_allow_html=True)
