"""
helpers.py — Reusable utility functions for the Loan Default Prediction Dashboard.
Handles CSS loading, HTML rendering, and common UI patterns.
"""

import streamlit as st
import os
from datetime import datetime


def load_css(file_path: str) -> None:
    """Load and inject an external CSS file into the Streamlit app."""
    css_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), file_path)
    if os.path.exists(css_path):
        with open(css_path, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def inject_google_fonts() -> None:
    """Inject Inter font from Google Fonts."""
    st.markdown(
        """
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
        """,
        unsafe_allow_html=True,
    )


def get_current_date() -> str:
    """Return formatted current date."""
    return datetime.now().strftime("%B %d, %Y")


def spacer(height: int = 16) -> None:
    """Add vertical spacing using an invisible div."""
    st.markdown(f'<div style="height: {height}px;"></div>', unsafe_allow_html=True)


def section_header(title: str, subtitle: str = "", icon: str = "") -> None:
    """Render a styled section header with optional subtitle."""
    icon_html = f'<span class="section-icon">{icon}</span> ' if icon else ""
    subtitle_html = f'<p class="section-subtitle">{subtitle}</p>' if subtitle else ""
    st.markdown(
        f"""
        <div class="section-header fade-in">
            <h2 class="section-title">{icon_html}{title}</h2>
            {subtitle_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def divider() -> None:
    """Render a styled horizontal divider."""
    st.markdown('<hr class="styled-divider">', unsafe_allow_html=True)


def badge(text: str, variant: str = "primary") -> str:
    """Return HTML for a styled badge. Variants: primary, success, warning, danger, neutral."""
    return f'<span class="badge badge-{variant}">{text}</span>'


def status_chip(text: str, status: str = "active") -> str:
    """Return HTML for a status chip. Status: active, inactive, pending."""
    return f'<span class="status-chip status-{status}">{text}</span>'


def render_back_to_top() -> None:
    """Render a floating back-to-top button."""
    st.markdown(
        """
        <a href="#loan-default-prediction" class="back-to-top" title="Back to Top">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="18 15 12 9 6 15"></polyline>
            </svg>
        </a>
        """,
        unsafe_allow_html=True,
    )


def render_empty_state(message: str = "No data available", icon: str = "📭") -> None:
    """Render a styled empty state placeholder."""
    st.markdown(
        f"""
        <div class="empty-state fade-in">
            <div class="empty-state-icon">{icon}</div>
            <p class="empty-state-text">{message}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def format_number(num: float, decimals: int = 1) -> str:
    """Format large numbers with K/M suffixes."""
    if num >= 1_000_000:
        return f"{num / 1_000_000:.{decimals}f}M"
    elif num >= 1_000:
        return f"{num / 1_000:.{decimals}f}K"
    return str(num)


def chart_explanation_panel(explanation: dict) -> None:
    """
    Render a chart explanation panel below a visualization.
    Expects a dict with keys: what, observe, insight, conclusion.
    """
    st.markdown(
        f"""
        <div class="chart-explanation-panel fade-in">
            <div class="explanation-item">
                <div class="explanation-label">📖 What does this graph show?</div>
                <div class="explanation-text">{explanation.get('what', '')}</div>
            </div>
            <div class="explanation-item">
                <div class="explanation-label">👁️ What should we observe?</div>
                <div class="explanation-text">{explanation.get('observe', '')}</div>
            </div>
            <div class="explanation-item">
                <div class="explanation-label">💡 Business Insight</div>
                <div class="explanation-text">{explanation.get('insight', '')}</div>
            </div>
            <div class="explanation-item">
                <div class="explanation-label">✅ Possible Conclusion</div>
                <div class="explanation-text">{explanation.get('conclusion', '')}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def chart_toolbar(chart_id: str = "chart") -> None:
    """Render export/fullscreen/download buttons above a chart."""
    st.markdown(
        f"""
        <div class="chart-toolbar">
            <button class="chart-btn" title="Fullscreen">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg>
            </button>
            <button class="chart-btn" title="Download PNG">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            </button>
            <button class="chart-btn" title="Refresh">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg>
            </button>
            <button class="chart-btn" title="Export CSV">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
            </button>
        </div>
        """,
        unsafe_allow_html=True,
    )


def force_scroll_to_top() -> None:
    """Inject a JavaScript snippet to scroll the main Streamlit container to the top."""
    st.iframe(
        """
        <script>
            const main = window.parent.document.querySelector('.main');
            if (main) {
                main.scrollTop = 0;
            }
        </script>
        """,
        height="content",
    )
