"""
streamlit_app.py — Main entry point for the Loan Default Prediction Dashboard.

A premium, static Streamlit dashboard showcasing how a professional ML project
UI should look before backend integration. All data is placeholder/dummy.

Run: streamlit run streamlit_app.py
"""

import streamlit as st

# ── Page Configuration (must be first Streamlit call) ──
st.set_page_config(
    page_title="Loan Default Prediction — ML Dashboard",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://github.com",
        "Report a bug": "https://github.com",
        "About": "Loan Default Prediction using Machine Learning — A premium static dashboard prototype.",
    },
)

# ── Load CSS & Fonts ──
from utils.helpers import load_css, inject_google_fonts, render_back_to_top, force_scroll_to_top

inject_google_fonts()
load_css("styles/style.css")

# ── Components ──
from components.sidebar import render_sidebar

# ── Pages ──
from pages.home import render_home
from pages.dataset import render_dataset
from pages.eda import render_eda
from pages.preprocessing import render_preprocessing
from pages.task_05 import render_task_05
from pages.task_06 import render_task_06
from pages.prediction import render_prediction

# ── Render Sidebar & Get Selected Page ──
selected_page = render_sidebar()

# ── Page Router ──
PAGE_MAP = {
    "Home": render_home,
    "Dataset": render_dataset,
    "EDA": render_eda,
    "Preprocessing": render_preprocessing,
    "Week-05 Task": render_task_05,
    "Boosting": render_task_06,
    "Project Demo": render_prediction,
}

# Render the selected page
page_fn = PAGE_MAP.get(selected_page, render_home)
page_fn()

# Force scroll to top to prevent page cutoff
force_scroll_to_top()

# ── Back to Top Button ──
render_back_to_top()
