"""
timeline.py — Workflow timeline and project flowchart components.
"""
import streamlit as st
from utils.constants import WORKFLOW_STEPS


def render_workflow_timeline() -> None:
    """Render a horizontal animated workflow timeline."""
    items_html = ""
    for step in WORKFLOW_STEPS:
        connector = '<div class="timeline-connector"></div>' if step["step"] < len(WORKFLOW_STEPS) else ""
        items_html += f"""
        <div class="timeline-item fade-in" style="animation-delay: {step['step'] * 0.1}s;">
            <div class="timeline-dot">{step['icon']}</div>
            {connector}
            <div class="timeline-label">{step['title']}</div>
            <div class="timeline-desc">{step['desc']}</div>
        </div>
        """

    st.markdown(f'<div class="timeline-container">{items_html}</div>', unsafe_allow_html=True)


def render_project_flowchart() -> None:
    """Render a vertical project flowchart."""
    steps = [
        ("📦", "Dataset Collection"),
        ("🧹", "Data Cleaning"),
        ("📊", "Exploratory Data Analysis"),
        ("⚙️", "Data Preprocessing"),
        ("🔧", "Feature Engineering"),
        ("🤖", "Model Training"),
        ("🧪", "Model Testing"),
        ("📉", "Model Evaluation"),
        ("🚀", "Deployment"),
    ]
    flow_html = ""
    for i, (icon, label) in enumerate(steps):
        flow_html += f"""
        <div class="flow-node fade-in" style="animation-delay: {i * 0.08}s;">
            <div class="flow-node-icon">{icon}</div>
            <div class="flow-node-text">{label}</div>
        </div>
        """
        if i < len(steps) - 1:
            flow_html += '<div class="flow-arrow">▼</div>'

    st.markdown(f'<div class="flowchart-container">{flow_html}</div>', unsafe_allow_html=True)
