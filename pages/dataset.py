"""
dataset.py — Dataset overview page with statistics cards and feature explorer.
"""
import streamlit as st
from utils.constants import DATASET_STATS, FEATURES
from utils.helpers import section_header, spacer, badge
from components.cards import metric_card, feature_card


def render_dataset():
    """Render the Dataset Overview page."""
    section_header("Dataset Overview", "Explore the structure and statistics of the loan default dataset", "📊")
    spacer(8)

    # ── Summary Stats ──
    r1c1, r1c2, r1c3, r1c4 = st.columns(4)
    with r1c1:
        metric_card("📦", "Total Rows", f"{DATASET_STATS['total_rows']:,}", bg_color="#EFF6FF")
    with r1c2:
        metric_card("📊", "Total Columns", str(DATASET_STATS['total_columns']), bg_color="#F0FDF4")
    with r1c3:
        metric_card("🔢", "Numerical", str(DATASET_STATS['numerical_features']), bg_color="#FFFBEB")
    with r1c4:
        metric_card("🏷️", "Categorical", str(DATASET_STATS['categorical_features']), bg_color="#FEF2F2")

    spacer(16)

    r2c1, r2c2, r2c3, r2c4 = st.columns(4)
    with r2c1:
        metric_card("🎯", "Target Variable", DATASET_STATS['target_variable'], bg_color="#F5F3FF")
    with r2c2:
        metric_card("💾", "Dataset Size", f"{DATASET_STATS['dataset_size_mb']} MB", bg_color="#ECFDF5")
    with r2c3:
        metric_card("✅", "Completion", f"{DATASET_STATS['completion_rate']}%", bg_color="#EFF6FF")
    with r2c4:
        metric_card("⚠️", "Missing Data", f"{DATASET_STATS['missing_percentage']}%", bg_color="#FFFBEB")

    spacer(24)

    # ── Completion Progress ──
    st.markdown(
        f"""
        <div class="metric-card fade-in" style="margin-bottom:24px;">
            <p class="metric-label">Data Completion Status</p>
            <div style="display:flex;align-items:center;gap:12px;margin-top:8px;">
                <div class="progress-bar-container" style="flex:1;">
                    <div class="progress-bar-fill" style="width:{DATASET_STATS['completion_rate']}%;
                        background:linear-gradient(90deg,#2563EB,#7C3AED);"></div>
                </div>
                <span style="font-size:14px;font-weight:700;color:#111827;">{DATASET_STATS['completion_rate']}%</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Feature Explorer ──
    section_header("Feature Explorer", "Browse all 18 features in the dataset", "🔍")

    # Category filter
    categories = sorted(set(f["category"] for f in FEATURES))
    selected_cat = st.selectbox("Filter by Category", ["All"] + categories, key="feat_filter")

    filtered = FEATURES if selected_cat == "All" else [f for f in FEATURES if f["category"] == selected_cat]

    cols = st.columns(2)
    for i, feat in enumerate(filtered):
        with cols[i % 2]:
            feature_card(feat)
            spacer(8)

    spacer(16)

    # ── Schema Table ──
    section_header("Dataset Schema", "Quick reference of all columns", "📋")
    schema_rows = ""
    for f in FEATURES:
        cat_badge = badge(f["category"], "primary")
        schema_rows += f"""
        <tr>
            <td>{f['icon']} {f['name']}</td>
            <td><code style="background:#F1F5F9;padding:2px 6px;border-radius:4px;font-size:12px;">{f['dtype']}</code></td>
            <td>{f['example']}</td>
            <td>{cat_badge}</td>
        </tr>
        """
    st.markdown(
        f"""
        <div style="overflow-x:auto;">
            <table class="comparison-table">
                <thead><tr><th>Feature</th><th>Data Type</th><th>Example</th><th>Category</th></tr></thead>
                <tbody>{schema_rows}</tbody>
            </table>
        </div>
        """,
        unsafe_allow_html=True,
    )
