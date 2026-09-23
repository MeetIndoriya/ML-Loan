"""
eda.py — Exploratory Data Analysis page with 12 chart types and explanation panels.
"""
import streamlit as st
from utils.helpers import section_header, spacer, chart_toolbar, chart_explanation_panel
from utils.constants import CHART_EXPLANATIONS
from components.charts import (
    default_distribution_chart, income_distribution_chart, credit_score_chart,
    correlation_heatmap, loan_purpose_pie, interest_rate_trend,
    age_boxplot, scatter_income_loan, education_bar,
    violin_dti, area_trend, radar_chart, treemap_chart,
)


def _render_chart_section(title, subtitle, chart_fn, explanation_key, source="Loan Default Dataset"):
    """Helper to render a chart with toolbar and explanation panel."""
    st.markdown(
        f"""
        <div class="chart-container">
            <div class="chart-header">
                <div>
                    <p class="chart-title">{title}</p>
                    <p class="chart-subtitle">{subtitle}</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    chart_toolbar(explanation_key)
    st.plotly_chart(chart_fn(), use_container_width=True, config={"displayModeBar": False})

    st.markdown(
        f'<div style="font-size:12px;color:#9CA3AF;margin:-8px 0 8px;">📁 Data Source: {source}</div>',
        unsafe_allow_html=True,
    )

    if explanation_key in CHART_EXPLANATIONS:
        chart_explanation_panel(CHART_EXPLANATIONS[explanation_key])
    spacer(24)


def render_eda():
    """Render the EDA page with all visualizations."""
    section_header(
        "Exploratory Data Analysis",
        "Visual exploration of patterns, distributions, and relationships in the loan dataset",
        "📈",
    )
    spacer(8)

    # Tab navigation for chart categories
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Distributions", "🔗 Relationships", "📈 Trends", "🗂️ Advanced"])

    with tab1:
        spacer(16)
        _render_chart_section(
            "Target Variable Distribution",
            "Default vs. Non-Default loan distribution",
            default_distribution_chart, "default_distribution",
        )
        c1, c2 = st.columns(2)
        with c1:
            _render_chart_section(
                "Income Distribution", "Annual income across applicants",
                income_distribution_chart, "income_distribution",
            )
        with c2:
            _render_chart_section(
                "Credit Score Distribution", "Credit scores across applicants",
                credit_score_chart, "credit_score",
            )
        _render_chart_section(
            "DTI Ratio by Default Status", "Violin plot comparison",
            violin_dti, "age_vs_default",
        )

    with tab2:
        spacer(16)
        _render_chart_section(
            "Feature Correlation Heatmap", "Pearson correlation between numerical features",
            correlation_heatmap, "correlation_heatmap",
        )
        c1, c2 = st.columns(2)
        with c1:
            _render_chart_section(
                "Income vs. Loan Amount", "Scatter plot colored by default status",
                scatter_income_loan, "scatter_income_loan",
            )
        with c2:
            _render_chart_section(
                "Age by Default Status", "Box plot comparison",
                age_boxplot, "age_vs_default",
            )
        _render_chart_section(
            "Default Rate by Education", "Stacked bar chart by education level",
            education_bar, "education_default",
        )

    with tab3:
        spacer(16)
        _render_chart_section(
            "Default Rate by Interest Rate", "How interest rate affects default probability",
            interest_rate_trend, "interest_rate",
        )
        _render_chart_section(
            "Monthly Applications vs. Defaults", "12-month trend analysis",
            area_trend, "interest_rate",
        )

    with tab4:
        spacer(16)
        c1, c2 = st.columns(2)
        with c1:
            _render_chart_section(
                "Loan Purpose Distribution", "Donut chart breakdown",
                loan_purpose_pie, "loan_purpose",
            )
        with c2:
            _render_chart_section(
                "Model Performance Radar", "Multi-model comparison",
                radar_chart, "roc_curve",
            )
        _render_chart_section(
            "Feature Category Treemap", "Hierarchical view of features by category",
            treemap_chart, "feature_importance",
        )
