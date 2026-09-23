"""
cards.py — Reusable card components: metric, info, feature, model, preprocessing, insight.
"""
import streamlit as st
from utils.constants import COLORS


def metric_card(icon: str, label: str, value: str, delta: str = "", delta_type: str = "positive",
                bg_color: str = "#EFF6FF") -> None:
    """Render a KPI metric card."""
    delta_html = ""
    if delta:
        arrow = "↑" if delta_type == "positive" else "↓"
        delta_html = f'<div class="metric-delta {delta_type}">{arrow} {delta}</div>'
    st.markdown(
        f"""
        <div class="metric-card fade-in">
            <div class="metric-icon" style="background:{bg_color};">{icon}</div>
            <p class="metric-label">{label}</p>
            <p class="metric-value">{value}</p>
            {delta_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def info_card(icon: str, title: str, description: str) -> None:
    """Render a project overview / info card."""
    st.markdown(
        f"""
        <div class="info-card fade-in">
            <span class="info-card-icon">{icon}</span>
            <h4 class="info-card-title">{title}</h4>
            <p class="info-card-desc">{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def feature_card(feature: dict) -> None:
    """Render a dataset feature card."""
    st.markdown(
        f"""
        <div class="feature-card fade-in">
            <div class="feature-icon-wrap">{feature['icon']}</div>
            <div>
                <p class="feature-name">{feature['name']}</p>
                <span class="feature-type">{feature['dtype']}</span>
                <p class="feature-desc">{feature['description']}</p>
                <p class="feature-example">Example: {feature['example']}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def model_card(model: dict) -> None:
    """Render a machine learning model card."""
    advantages_html = "".join(f"<li>{a}</li>" for a in model["advantages"])
    disadvantages_html = "".join(f"<li>{d}</li>" for d in model["disadvantages"])

    diff_colors = {"Beginner": "#F0FDF4;color:#16A34A", "Intermediate": "#FFFBEB;color:#B45309",
                   "Advanced": "#FEF2F2;color:#DC2626"}
    diff_bg = diff_colors.get(model["difficulty"], "#F3F4F6;color:#6B7280")

    st.markdown(
        f"""
        <div class="model-card fade-in">
            <div class="model-header">
                <span class="model-icon">{model['icon']}</span>
                <h4 class="model-name">{model['name']}</h4>
            </div>
            <p class="model-desc">{model['description']}</p>
            <div class="model-tags">
                <span class="badge" style="background:{diff_bg};">{model['difficulty']}</span>
                <span class="badge badge-primary">⚡ {model['speed']}</span>
            </div>
            <div style="margin-bottom:14px;">
                <span class="model-accuracy">{model['accuracy']}%</span>
                <span style="font-size:13px;color:#6B7280;margin-left:4px;">accuracy</span>
            </div>
            <details style="margin-bottom:8px;">
                <summary style="font-size:13px;font-weight:600;color:#16A34A;cursor:pointer;">✅ Advantages</summary>
                <ul style="font-size:13px;color:#6B7280;margin:8px 0 0 16px;line-height:1.8;">{advantages_html}</ul>
            </details>
            <details>
                <summary style="font-size:13px;font-weight:600;color:#DC2626;cursor:pointer;">⚠️ Disadvantages</summary>
                <ul style="font-size:13px;color:#6B7280;margin:8px 0 0 16px;line-height:1.8;">{disadvantages_html}</ul>
            </details>
        </div>
        """,
        unsafe_allow_html=True,
    )


def preprocess_card(step: dict) -> None:
    """Render a preprocessing step card."""
    st.markdown(
        f"""
        <div class="preprocess-card fade-in">
            <div class="preprocess-header">
                <span class="preprocess-icon">{step['icon']}</span>
                <h4 class="preprocess-title">{step['title']}</h4>
            </div>
            <p class="preprocess-desc">{step['description']}</p>
            <div class="preprocess-meta">
                <span class="preprocess-tag tag-before">Before: {step['before']}</span>
                <span class="preprocess-tag tag-after">After: {step['after']}</span>
                <span class="preprocess-tag tag-method">{step['method']}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def insight_box(icon: str, text: str) -> None:
    """Render a business insight / Did You Know box."""
    st.markdown(
        f"""
        <div style="background:#FFFBEB;border:1px solid #FDE68A;border-radius:10px;padding:14px 18px;
            display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;" class="fade-in">
            <span style="font-size:20px;flex-shrink:0;">{icon}</span>
            <span style="font-size:14px;color:#92400E;line-height:1.5;">{text}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
