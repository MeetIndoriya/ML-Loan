"""
about.py — About page with team info, FAQ accordion, ML glossary, and tech stack.
"""
import streamlit as st
from utils.constants import FAQ_ITEMS, GLOSSARY
from utils.helpers import section_header, spacer


def render_about():
    """Render the About page."""
    section_header("About This Project", "Learn more about the Loan Default Prediction dashboard", "ℹ️")
    spacer(8)

    # ── Project Summary ──
    st.markdown(
        """
        <div class="metric-card fade-in" style="border-left:4px solid #2563EB;">
            <h4 style="font-size:18px;font-weight:700;color:#111827;margin:0 0 12px;">Loan Default Prediction using Machine Learning</h4>
            <p style="font-size:14px;color:#6B7280;line-height:1.7;margin:0;">
                This project demonstrates a complete end-to-end machine learning pipeline for predicting loan defaults.
                Using a dataset of 255,347 loan records, we trained and compared 6 models to identify the best predictor.
                XGBoost emerged as the top performer with 89.3% accuracy and 0.938 ROC-AUC score. The dashboard
                serves as a production-quality UI prototype for enterprise deployment.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    spacer(24)

    # ── Tech Stack ──
    section_header("Technology Stack", icon="🛠️")
    techs = [
        ("🐍", "Python 3.11", "Core programming language"),
        ("📊", "Streamlit", "Dashboard framework"),
        ("📈", "Plotly", "Interactive visualizations"),
        ("🤖", "Scikit-learn", "ML algorithms"),
        ("🚀", "XGBoost", "Gradient boosting"),
        ("🐼", "Pandas", "Data manipulation"),
        ("🔢", "NumPy", "Numerical computing"),
        ("🎨", "Custom CSS", "Premium styling"),
    ]
    cols = st.columns(4)
    for i, (icon, name, desc) in enumerate(techs):
        with cols[i % 4]:
            st.markdown(
                f"""
                <div class="metric-card fade-in" style="text-align:center;padding:20px 12px;">
                    <span style="font-size:28px;">{icon}</span>
                    <p style="font-size:14px;font-weight:600;color:#111827;margin:8px 0 2px;">{name}</p>
                    <p style="font-size:12px;color:#6B7280;margin:0;">{desc}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            spacer(8)

    spacer(24)

    # ── FAQ ──
    section_header("Frequently Asked Questions", icon="❓")
    for question, answer in FAQ_ITEMS:
        with st.expander(question):
            st.markdown(f'<p style="font-size:14px;color:#6B7280;line-height:1.6;">{answer}</p>', unsafe_allow_html=True)

    spacer(24)

    # ── ML Glossary ──
    section_header("ML Glossary", "Key machine learning terms explained for beginners", "📖")
    glossary_html = ""
    for term, definition in sorted(GLOSSARY.items()):
        glossary_html += f"""
        <div class="glossary-item">
            <div class="glossary-term">{term}</div>
            <div class="glossary-def">{definition}</div>
        </div>
        """
    st.markdown(
        f'<div class="metric-card fade-in" style="padding:0;overflow:hidden;">{glossary_html}</div>',
        unsafe_allow_html=True,
    )

    spacer(24)

    # ── Keyboard Shortcuts ──
    section_header("Keyboard Shortcuts", icon="⌨️")
    shortcuts = [("Ctrl + /", "Toggle sidebar"), ("Ctrl + F", "Search"), ("Ctrl + P", "Print dashboard"),
                 ("↑ / ↓", "Navigate sections"), ("Esc", "Close dialogs")]
    for key, desc in shortcuts:
        st.markdown(
            f"""
            <div style="display:flex;justify-content:space-between;padding:10px 16px;border-bottom:1px solid #F1F5F9;">
                <code style="background:#F1F5F9;padding:3px 10px;border-radius:6px;font-size:13px;font-weight:600;">{key}</code>
                <span style="font-size:14px;color:#6B7280;">{desc}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
