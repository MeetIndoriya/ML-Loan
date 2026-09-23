"""
feature_engineering.py — Feature engineering and importance page.
"""
import streamlit as st
from utils.constants import FEATURE_IMPORTANCE, CHART_EXPLANATIONS
from utils.helpers import section_header, spacer, chart_explanation_panel


def render_feature_engineering():
    """Render the Feature Engineering page."""
    section_header(
        "Feature Engineering",
        "Creating, selecting, and ranking the most predictive features",
        "⚙",
    )
    spacer(8)

    # ── Engineering Techniques ──
    techniques = [
        ("🔄", "Polynomial Features", "Created interaction terms between top correlated features (Income × CreditScore, LoanAmount × InterestRate)."),
        ("📊", "Binning", "Converted continuous Age and Income into categorical bins for better pattern capture."),
        ("➗", "Ratio Features", "Created Loan-to-Income ratio and Debt-to-Credit ratio as derived features."),
        ("📈", "Log Transform", "Applied log transformation to skewed features (Income, LoanAmount) for normality."),
        ("🏷️", "Target Encoding", "Replaced categorical values with their mean target value for high-cardinality features."),
        ("✂️", "Feature Selection", "Used mutual information and recursive feature elimination to select top 15 features."),
    ]
    cols = st.columns(3)
    for i, (icon, title, desc) in enumerate(techniques):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div class="info-card fade-in">
                    <span class="info-card-icon">{icon}</span>
                    <h4 class="info-card-title">{title}</h4>
                    <p class="info-card-desc">{desc}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            spacer(12)

    spacer(24)

    # ── Feature Importance Ranking ──
    section_header("Feature Importance", "Ranked by XGBoost model importance score", "🏆")

    max_val = max(v for _, v in FEATURE_IMPORTANCE)
    bars_html = ""
    for rank, (name, value) in enumerate(FEATURE_IMPORTANCE, 1):
        pct = (value / max_val) * 100
        bars_html += f"""
        <div class="importance-bar-wrap fade-in" style="animation-delay: {rank * 0.05}s;">
            <div class="importance-bar-header">
                <span class="importance-bar-name">#{rank} {name}</span>
                <span class="importance-bar-value">{value:.1%}</span>
            </div>
            <div class="importance-bar-track">
                <div class="importance-bar-fill" style="width: {pct}%;"></div>
            </div>
        </div>
        """

    st.markdown(
        f'<div class="metric-card fade-in" style="padding:28px;">{bars_html}</div>',
        unsafe_allow_html=True,
    )

    spacer(16)
    chart_explanation_panel(CHART_EXPLANATIONS["feature_importance"])

    spacer(24)

    # ── Key Takeaways ──
    section_header("Key Takeaways", icon="📌")
    takeaways = [
        "Income and Credit Score together account for 35% of the model's decision-making.",
        "Financial features dominate the top 5 positions — demographic features are less predictive alone.",
        "The Loan-to-Income ratio (engineered feature) ranks higher than raw Age.",
        "Feature engineering improved model accuracy from 85.1% to 89.3% (+4.2%).",
    ]
    for t in takeaways:
        st.markdown(
            f"""
            <div style="background:#F0FDF4;border:1px solid #BBF7D0;border-radius:10px;padding:12px 16px;
                margin-bottom:8px;font-size:14px;color:#166534;display:flex;gap:8px;" class="fade-in">
                <span>✅</span><span>{t}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
