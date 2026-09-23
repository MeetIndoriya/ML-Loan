"""
workflow.py — Project Workflow page with timeline and flowchart.
"""
import streamlit as st
from utils.helpers import section_header, spacer
from components.timeline import render_workflow_timeline, render_project_flowchart


def render_workflow():
    """Render the Project Workflow page."""
    section_header(
        "Project Workflow",
        "End-to-end machine learning pipeline from data collection to deployment",
        "📚",
    )
    spacer(8)

    # ── Horizontal Timeline ──
    st.markdown("### 🔄 ML Pipeline Timeline")
    render_workflow_timeline()

    spacer(32)

    # ── Vertical Flowchart ──
    st.markdown("### 📐 Project Flowchart")
    st.markdown(
        """
        <p style="font-size:14px;color:#6B7280;margin-bottom:16px;">
            Visual representation of the complete ML workflow from dataset collection to model deployment.
        </p>
        """,
        unsafe_allow_html=True,
    )
    render_project_flowchart()

    spacer(24)

    # ── Phase Details ──
    section_header("Phase Details", "Detailed description of each pipeline stage", "📋")

    phases = [
        ("📦", "Data Collection", "Gathered 255,347 loan records from multiple financial institutions spanning 2018–2024. Data includes demographics, financials, and loan characteristics.", "Week 1"),
        ("🧹", "Data Cleaning", "Handled 2.3% missing values, removed 127 duplicate records, corrected data type inconsistencies, and validated data integrity.", "Week 2"),
        ("📊", "Exploratory Data Analysis", "Performed univariate, bivariate, and multivariate analysis. Created 15+ visualizations to understand distributions, correlations, and patterns.", "Week 2–3"),
        ("⚙️", "Preprocessing", "Applied encoding (Label + One-Hot), scaling (StandardScaler), outlier capping (IQR), and SMOTE oversampling for class balance.", "Week 3"),
        ("🔧", "Feature Engineering", "Created 6 new features (ratios, bins, interactions). Selected top 15 features using mutual information and RFE.", "Week 4"),
        ("📈", "Polynomial Regression (Week-05 Task)", "Implemented Polynomial Regression (Degree = 2) on Income vs. Loan Amount using Scikit-Learn to model non-linear relationships.", "Week 5"),
        ("🤖", "Model Training", "Trained 6 models (LR, DT, RF, XGBoost, LightGBM, CatBoost) with 5-fold cross-validation and hyperparameter tuning.", "Week 4–5"),
        ("📉", "Evaluation", "Compared models using Accuracy, Precision, Recall, F1, ROC-AUC. Selected XGBoost (89.3% accuracy) as the best model.", "Week 5"),
        ("🚀", "Deployment", "Built Streamlit dashboard for interactive exploration and deployed model via REST API for real-time predictions.", "Week 6"),
    ]

    for icon, title, desc, timeline in phases:
        st.markdown(
            f"""
            <div class="metric-card fade-in" style="margin-bottom:12px;">
                <div style="display:flex;align-items:flex-start;gap:14px;">
                    <div style="width:44px;height:44px;background:#EFF6FF;border-radius:10px;
                        display:flex;align-items:center;justify-content:center;font-size:22px;flex-shrink:0;">{icon}</div>
                    <div style="flex:1;">
                        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;">
                            <h4 style="font-size:16px;font-weight:600;color:#111827;margin:0;">{title}</h4>
                            <span class="badge badge-primary">{timeline}</span>
                        </div>
                        <p style="font-size:14px;color:#6B7280;margin:6px 0 0;line-height:1.5;">{desc}</p>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
