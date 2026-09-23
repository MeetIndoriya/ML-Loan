"""
preprocessing.py — Data Preprocessing page with step cards and visualizations.
"""
import streamlit as st
from utils.constants import PREPROCESSING_STEPS
from utils.helpers import section_header, spacer
from components.cards import preprocess_card


def render_preprocessing():
    """Render the Data Preprocessing page."""
    section_header(
        "Data Preprocessing",
        "Step-by-step data cleaning and transformation pipeline",
        "🧹",
    )
    spacer(8)

    # ── Pipeline Overview ──
    st.markdown(
        """
        <div class="metric-card fade-in" style="margin-bottom:24px;">
            <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">
                <span style="font-size:24px;">⚙️</span>
                <div>
                    <p style="font-size:16px;font-weight:700;color:#111827;margin:0;">Preprocessing Pipeline</p>
                    <p style="font-size:13px;color:#6B7280;margin:0;">6 steps completed successfully</p>
                </div>
            </div>
            <div class="progress-bar-container" style="height:10px;">
                <div class="progress-bar-fill" style="width:100%;background:linear-gradient(90deg,#16A34A,#22C55E);"></div>
            </div>
            <div style="display:flex;justify-content:space-between;margin-top:8px;">
                <span style="font-size:12px;color:#16A34A;font-weight:600;">✅ All steps completed</span>
                <span style="font-size:12px;color:#6B7280;">6 / 6</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Step Cards ──
    cols = st.columns(2)
    for i, step in enumerate(PREPROCESSING_STEPS):
        with cols[i % 2]:
            preprocess_card(step)
            spacer(12)

    spacer(24)

    # ── Before/After Summary ──
    section_header("Before vs. After", "Impact of preprocessing on data quality", "📊")

    st.markdown(
        """
        <div class="metric-card fade-in">
            <table class="comparison-table">
                <thead>
                    <tr><th>Metric</th><th>Before</th><th>After</th><th>Change</th></tr>
                </thead>
                <tbody>
                    <tr><td>Missing Values</td><td>2.3%</td><td class="best-value">0%</td><td class="best-value">-2.3%</td></tr>
                    <tr><td>Outliers</td><td>847</td><td class="best-value">0</td><td class="best-value">-847</td></tr>
                    <tr><td>Features</td><td>18</td><td>24</td><td>+6 encoded</td></tr>
                    <tr><td>Class Balance</td><td>88:12</td><td class="best-value">50:50</td><td class="best-value">Balanced</td></tr>
                    <tr><td>Feature Scale</td><td>Varied</td><td class="best-value">Standardized</td><td class="best-value">Uniform</td></tr>
                </tbody>
            </table>
        </div>
        """,
        unsafe_allow_html=True,
    )
