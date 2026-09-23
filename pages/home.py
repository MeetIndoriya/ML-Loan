"""
home.py — Dashboard home page with hero section, project overview, and facts.
"""
import streamlit as st
import random
from utils.constants import PROJECT_NAME, PROJECT_SUBTITLE, OVERVIEW_CARDS, DID_YOU_KNOW_FACTS, DATASET_STATS
from utils.helpers import section_header, spacer
from components.cards import metric_card, info_card, insight_box


def render_home():
    """Render the Dashboard home page."""
    # ── Hero Section ──
    st.markdown(
        f"""
        <div class="hero-section slide-up">
            <h1 class="hero-title">{PROJECT_NAME}</h1>
            <p class="hero-subtitle">{PROJECT_SUBTITLE}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    spacer(24)

    # ── Quick Stats ──
    section_header("Key Metrics", "Essential summary of the loan dataset", "📊")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("📦", "Total Records", f"{DATASET_STATS['total_rows']:,}", "255K+ Applicants", "positive", "#EFF6FF")
    with c2:
        metric_card("📊", "Features", str(DATASET_STATS['total_columns']), "18 Financial Variables", "positive", "#F0FDF4")
    with c3:
        metric_card("🎯", "Model Accuracy", "89.3%", "Trained ML Model", "positive", "#FFFBEB")
    with c4:
        metric_card("⚡", "Default Rate", "12.1%", "Historical Avg", "positive", "#FEF2F2")

    spacer(32)

    # ── Project Overview ──
    section_header("Project Overview", "Key information about this machine learning project", "🎯")
    cols = st.columns(2)
    for i, card in enumerate(OVERVIEW_CARDS):
        with cols[i % 2]:
            info_card(card["icon"], card["title"], card["description"])
            spacer(16)
