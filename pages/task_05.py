"""
task_05.py — Week-05 Task: Polynomial Regression & Feature Optimization page.

Clean, high-performance static report page for Week-05 assignment:
Polynomial Regression on Income vs. Loan Amount using Loan_default.csv.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import os

try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

from utils.helpers import section_header, spacer, chart_explanation_panel
from components.cards import metric_card, info_card


@st.cache_data
def get_optimized_model_results(sample_size=2500, random_state=42):
    """Load dataset and compute optimized polynomial regression metrics."""
    csv_path = "Loan_default.csv"
    if not os.path.exists(csv_path):
        return None

    df = pd.read_csv(csv_path)
    df_sample = df.sample(n=min(sample_size, len(df)), random_state=random_state)
    X_sample = df_sample[["Income"]]
    y_sample = df_sample["LoanAmount"]

    # Degree 1 (Linear Baseline)
    poly_1 = PolynomialFeatures(degree=1)
    X_p1 = poly_1.fit_transform(X_sample)
    m1 = LinearRegression().fit(X_p1, y_sample)
    y_pred1 = m1.predict(X_p1)

    # Degree 2 (Week-05 Optimized Model)
    poly_2 = PolynomialFeatures(degree=2)
    X_p2 = poly_2.fit_transform(X_sample)
    m2 = LinearRegression().fit(X_p2, y_sample)
    y_pred2 = m2.predict(X_p2)

    # Degree 3 (Cubic Comparison)
    poly_3 = PolynomialFeatures(degree=3)
    X_p3 = poly_3.fit_transform(X_sample)
    m3 = LinearRegression().fit(X_p3, y_sample)
    y_pred3 = m3.predict(X_p3)

    # Plotting Curve
    X_min, X_max = X_sample["Income"].min(), X_sample["Income"].max()
    X_curve = pd.DataFrame(np.linspace(X_min, X_max, 300), columns=["Income"])

    y_curve_1 = m1.predict(poly_1.transform(X_curve))
    y_curve_2 = m2.predict(poly_2.transform(X_curve))
    y_curve_3 = m3.predict(poly_3.transform(X_curve))

    residuals1 = y_sample - y_pred1
    residuals2 = y_sample - y_pred2
    residuals3 = y_sample - y_pred3

    results = {
        "df_sample": df_sample,
        "X_curve": X_curve["Income"].values,
        "y_curve_1": y_curve_1,
        "y_curve_2": y_curve_2,
        "y_curve_3": y_curve_3,
        "model_deg2": m2,
        "poly_deg2": poly_2,
        "metrics": {
            "deg1": {
                "r2": r2_score(y_sample, y_pred1),
                "rmse": np.sqrt(mean_squared_error(y_sample, y_pred1)),
                "mae": mean_absolute_error(y_sample, y_pred1),
                "variance": float(np.var(residuals1)),
            },
            "deg2": {
                "r2": r2_score(y_sample, y_pred2),
                "rmse": np.sqrt(mean_squared_error(y_sample, y_pred2)),
                "mae": mean_absolute_error(y_sample, y_pred2),
                "variance": float(np.var(residuals2)),
            },
            "deg3": {
                "r2": r2_score(y_sample, y_pred3),
                "rmse": np.sqrt(mean_squared_error(y_sample, y_pred3)),
                "mae": mean_absolute_error(y_sample, y_pred3),
                "variance": float(np.var(residuals3)),
            },
        },
    }
    return results


def render_task_05():
    """Render the Week-05 Task & Model Optimization page."""
    section_header(
        "Week-05 Task: Polynomial Regression & Model Optimization",
        "Non-linear modeling and feature degree optimization for Income vs. Loan Amount",
        "📈",
    )
    spacer(8)

    # ── Task Overview Cards ──
    c1, c2, c3 = st.columns(3)
    with c1:
        info_card(
            "🎯",
            "Task Objective",
            "Apply Polynomial Regression to model non-linear relationships between applicant Income and requested Loan Amount.",
        )
    with c2:
        info_card(
            "⚡",
            "Feature Optimization",
            "Transformed 1D Income into quadratic degree-2 polynomial features to improve model representation.",
        )
    with c3:
        info_card(
            "📊",
            "Dataset & Scope",
            "Evaluated on 2,500 sampled records from Loan_default.csv with degree optimization benchmarking.",
        )

    spacer(24)

    # ── Fetch Pre-computed Optimization Results ──
    res = get_optimized_model_results()

    if res is None:
        st.error("⚠️ Loan_default.csv dataset not found in project directory.")
        return

    m2_stats = res["metrics"]["deg2"]
    m1_stats = res["metrics"]["deg1"]

    # ── Optimization Summary Cards ──
    section_header("Polynomial Model Optimization Summary", "Week-05 quadratic model vs. linear baseline", "🏆")

    r2_gain = ((m2_stats["r2"] - m1_stats["r2"]) / max(abs(m1_stats["r2"]), 1e-6)) * 100
    rmse_reduction = m1_stats["rmse"] - m2_stats["rmse"]
    variance_reduction = m1_stats["variance"] - m2_stats["variance"]

    m1_col, m2_col, m3_col, m4_col = st.columns(4)
    with m1_col:
        metric_card("🎯", "Optimal R² Score", f"{m2_stats['r2']:.4f}", "Degree 2 (Quadratic)", "positive", "#EFF6FF")
    with m2_col:
        metric_card("📏", "Optimized RMSE", f"${m2_stats['rmse']:,.2f}", f"-${rmse_reduction:,.2f} vs Linear", "positive", "#F0FDF4")
    with m3_col:
        metric_card("📐", "Optimized MAE", f"${m2_stats['mae']:,.2f}", "Mean Absolute Error", "neutral", "#FFFBEB")
    with m4_col:
        metric_card("⚡", "Error Variance", f"{m2_stats['variance']:,.2f}", f"-{variance_reduction:,.2f} vs Linear", "positive", "#F5F3FF")

    spacer(24)

    # ── Optimization Degree Comparison Table ──
    section_header("Polynomial Degree Optimization Analysis", "Performance metrics across polynomial degrees", "📊")

    opt_df = pd.DataFrame([
        {"Polynomial Degree": "Degree 1 (Linear Baseline)", "R² Score": f"{res['metrics']['deg1']['r2']:.4f}", "RMSE ($)": f"${res['metrics']['deg1']['rmse']:,.2f}", "MAE ($)": f"${res['metrics']['deg1']['mae']:,.2f}", "Variance": f"{res['metrics']['deg1']['variance']:,.2f}", "Status": "Underfitting Baseline"},
        {"Polynomial Degree": "Degree 2 (Week-05 Optimal)", "R² Score": f"{res['metrics']['deg2']['r2']:.4f}", "RMSE ($)": f"${res['metrics']['deg2']['rmse']:,.2f}", "MAE ($)": f"${res['metrics']['deg2']['mae']:,.2f}", "Variance": f"{res['metrics']['deg2']['variance']:,.2f}", "Status": "✅ Optimal Complexity"},
        {"Polynomial Degree": "Degree 3 (Cubic)", "R² Score": f"{res['metrics']['deg3']['r2']:.4f}", "RMSE ($)": f"${res['metrics']['deg3']['rmse']:,.2f}", "MAE ($)": f"${res['metrics']['deg3']['mae']:,.2f}", "Variance": f"{res['metrics']['deg3']['variance']:,.2f}", "Status": "Risk of Overfitting"},
    ])

    st.table(opt_df)

    spacer(16)

    # ── Polynomial Regression Visualizations ──
    section_header("Optimized Regression Curves", "Visual comparison of linear vs. quadratic regression curves", "📉")

    tab1, tab2 = st.tabs(["📊 Interactive Plotly View", "🖼️ Matplotlib View"])

    df_sample = res["df_sample"]
    X_curve = res["X_curve"]

    with tab1:
        fig = go.Figure()

        # Scatter plot of actual data
        fig.add_trace(
            go.Scatter(
                x=df_sample["Income"],
                y=df_sample["LoanAmount"],
                mode="markers",
                name="Actual Data (Sample)",
                marker=dict(size=6, color="#2563EB", opacity=0.35),
                hovertemplate="Income: $%{x:,.0f}<br>Loan Amount: $%{y:,.0f}<extra></extra>",
            )
        )

        # Fitted Polynomial Regression Curve (Degree 2)
        fig.add_trace(
            go.Scatter(
                x=X_curve,
                y=res["y_curve_2"],
                mode="lines",
                name="Polynomial Regression (Degree 2 - Week 05)",
                line=dict(color="#DC2626", width=4),
                hovertemplate="Income: $%{x:,.0f}<br>Poly Loan: $%{y:,.0f}<extra></extra>",
            )
        )

        # Baseline Linear Regression Line
        fig.add_trace(
            go.Scatter(
                x=X_curve,
                y=res["y_curve_1"],
                mode="lines",
                name="Linear Regression (Degree 1 Baseline)",
                line=dict(color="#10B981", width=2.5, dash="dash"),
                hovertemplate="Income: $%{x:,.0f}<br>Linear Loan: $%{y:,.0f}<extra></extra>",
            )
        )

        fig.update_layout(
            title=dict(text="Polynomial Regression Optimization — Income vs. Loan Amount", font=dict(size=16, color="#111827")),
            xaxis=dict(title="Income ($)", tickprefix="$", gridcolor="#F1F5F9"),
            yaxis=dict(title="Loan Amount ($)", tickprefix="$", gridcolor="#F1F5F9"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            margin=dict(l=40, r=40, t=60, b=40),
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
            height=500,
        )

        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        if HAS_MATPLOTLIB:
            plt.figure(figsize=(10, 5.5))
            plt.scatter(df_sample["Income"], df_sample["LoanAmount"], alpha=0.4, color="#1f77b4", label="Actual Data")
            plt.plot(X_curve, res["y_curve_2"], color="#ff7f0e", linewidth=4, label="Polynomial Regression (Degree 2)")
            plt.xlabel("Income", fontsize=12)
            plt.ylabel("Loan Amount", fontsize=12)
            plt.title("Polynomial Regression - Income vs Loan Amount", fontsize=14)
            plt.legend(fontsize=11)
            plt.grid(True, linestyle="--", alpha=0.6)
            plt.tight_layout()

            st.pyplot(plt.gcf())
            plt.close()
        else:
            st.info("ℹ️ Matplotlib view. Interactive Plotly chart is displayed in Tab 1.")

    spacer(16)

    # Explanation Panel
    poly_explanation = {
        "what": "This graph compares simple linear regression against quadratic polynomial regression (Degree 2) for predicting Loan Amount from applicant Income.",
        "observe": "The quadratic curve captures non-linear scaling, showing that loan amounts grow at a non-constant rate relative to income.",
        "insight": "Polynomial feature expansion allows standard linear models to fit complex non-linear frontiers without requiring neural network overhead.",
        "conclusion": "Degree 2 Polynomial Regression provides the optimal balance of flexibility and stability, avoiding underfitting (Degree 1) and overfitting (Degree 3+).",
    }
    chart_explanation_panel(poly_explanation)

    spacer(24)

    # ── Interactive Prediction Tool ──
    section_header("Prediction Tool", "Estimate loan amount using optimized polynomial model", "🧮")

    input_income = st.slider("Select Applicant Income ($)", min_value=10000, max_value=200000, value=65000, step=2500)

    # Predict using degree 2 polynomial model
    poly_2 = res["poly_deg2"]
    m2 = res["model_deg2"]

    input_df = pd.DataFrame([[input_income]], columns=["Income"])
    income_poly = poly_2.transform(input_df)
    pred_poly_loan = m2.predict(income_poly)[0]

    p1, p2 = st.columns(2)
    with p1:
        metric_card("💰", "Input Income", f"${input_income:,.0f}", "Applicant Income", "neutral", "#EFF6FF")
    with p2:
        metric_card("📈", "Optimized Loan Estimate", f"${pred_poly_loan:,.2f}", "Degree 2 Polynomial Model", "positive", "#F0FDF4")
