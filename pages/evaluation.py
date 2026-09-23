"""
evaluation.py — Model Evaluation page with ROC, confusion matrix, PR curve, and learning curves.
"""
import streamlit as st
from utils.helpers import section_header, spacer, chart_toolbar, chart_explanation_panel
from utils.constants import CHART_EXPLANATIONS
from components.charts import roc_curve_chart, confusion_matrix_chart, precision_recall_chart, learning_curves_chart


def render_evaluation():
    """Render the Model Evaluation page."""
    section_header(
        "Model Evaluation",
        "In-depth analysis of model performance using multiple evaluation metrics",
        "📉",
    )
    spacer(8)

    # ── Summary Metrics ──
    c1, c2, c3, c4 = st.columns(4)
    metrics = [
        ("🎯", "Accuracy", "89.3%", "#EFF6FF"),
        ("📊", "Precision", "88.1%", "#F0FDF4"),
        ("🔍", "Recall", "86.8%", "#FFFBEB"),
        ("📈", "ROC AUC", "0.938", "#FEF2F2"),
    ]
    for col, (icon, label, value, bg) in zip([c1, c2, c3, c4], metrics):
        with col:
            st.markdown(
                f"""
                <div class="metric-card fade-in">
                    <div class="metric-icon" style="background:{bg};">{icon}</div>
                    <p class="metric-label">{label}</p>
                    <p class="metric-value">{value}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    spacer(24)

    # ── ROC Curves ──
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    chart_toolbar("roc")
    st.plotly_chart(roc_curve_chart(), use_container_width=True, config={"displayModeBar": False})
    st.markdown('</div>', unsafe_allow_html=True)
    chart_explanation_panel(CHART_EXPLANATIONS["roc_curve"])

    spacer(24)

    # ── Confusion Matrix & PR Curve ──
    c1, c2 = st.columns(2)
    with c1:
        chart_toolbar("cm")
        st.plotly_chart(confusion_matrix_chart(), use_container_width=True, config={"displayModeBar": False})
        chart_explanation_panel(CHART_EXPLANATIONS["confusion_matrix"])
    with c2:
        chart_toolbar("pr")
        st.plotly_chart(precision_recall_chart(), use_container_width=True, config={"displayModeBar": False})

    spacer(24)

    # ── Learning Curves ──
    section_header("Learning Curves", "How model performance improves with more training data", "📈")
    chart_toolbar("lc")
    st.plotly_chart(learning_curves_chart(), use_container_width=True, config={"displayModeBar": False})

    spacer(16)
    st.markdown(
        """
        <div style="background:#EFF6FF;border:1px solid #BFDBFE;border-radius:10px;padding:14px 18px;
            font-size:14px;color:#1E40AF;display:flex;gap:8px;" class="fade-in">
            <span>ℹ️</span>
            <span>The learning curves converge around 150K samples, indicating the model benefits from large datasets
            and is not significantly overfitting. Adding more data beyond 200K samples yields diminishing returns.</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
