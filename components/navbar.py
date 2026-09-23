"""
navbar.py — Top navigation bar with search, notifications, profile, and date.
"""
import streamlit as st
from utils.helpers import get_current_date
from utils.constants import PROJECT_NAME


def render_navbar() -> None:
    """Render the top navigation bar."""
    date_str = get_current_date()
    st.markdown(
        f"""
        <div class="top-navbar fade-in">
            <div class="navbar-brand">
                <div class="logo-icon">LP</div>
                {PROJECT_NAME}
            </div>
            <div class="navbar-actions">
                <input type="text" class="nav-search" placeholder="🔍  Search anything..." disabled />
                <div class="nav-date">{date_str}</div>
                <div class="nav-icon-btn" title="Toggle Theme">🌙</div>
                <div class="nav-icon-btn" title="Notifications" style="position:relative;">
                    🔔
                    <span style="position:absolute;top:2px;right:2px;width:8px;height:8px;
                        background:#DC2626;border-radius:50%;border:2px solid #fff;"></span>
                </div>
                <div class="nav-avatar" title="Profile">MT</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
