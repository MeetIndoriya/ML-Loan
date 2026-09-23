"""
footer.py — Dashboard footer with social links and copyright.
"""
import streamlit as st
from utils.constants import PROJECT_NAME, PROJECT_VERSION, PROJECT_AUTHOR


def render_footer() -> None:
    """Render the dashboard footer."""
    st.markdown(
        f"""
        <div class="dashboard-footer fade-in">
            <div class="footer-links">
                <a href="#" class="footer-link">Documentation</a>
                <a href="#" class="footer-link">GitHub</a>
                <a href="#" class="footer-link">LinkedIn</a>
                <a href="#" class="footer-link">Contact</a>
            </div>
            <p class="footer-copy">
                © 2024 {PROJECT_NAME} • v{PROJECT_VERSION} • Built by {PROJECT_AUTHOR}<br/>
                <span style="font-size:11px;color:#475569;">Built with Streamlit & Plotly • Designed for enterprise-grade analytics</span>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
