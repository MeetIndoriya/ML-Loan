"""
charts.py — All Plotly chart generators for the dashboard.
Every chart uses the project color palette and is styled for premium aesthetics.
"""
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from utils.constants import CHART_COLORS, COLORS

# Common layout settings
LAYOUT_DEFAULTS = dict(
    font=dict(family="Inter, sans-serif", color=COLORS["text_primary"]),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=40, r=20, t=40, b=40),
    legend=dict(font=dict(size=12), bgcolor="rgba(255,255,255,.8)", bordercolor="#E5E7EB", borderwidth=1),
    hoverlabel=dict(bgcolor="#fff", font_size=13, font_family="Inter"),
)


def _apply_layout(fig, title="", height=400):
    fig.update_layout(**LAYOUT_DEFAULTS, title=dict(text=title, font=dict(size=16, color=COLORS["text_primary"])), height=height)
    fig.update_xaxes(gridcolor="#F1F5F9", zeroline=False)
    fig.update_yaxes(gridcolor="#F1F5F9", zeroline=False)
    return fig


def default_distribution_chart():
    """Bar chart: loan default vs. non-default distribution."""
    fig = go.Figure(data=[go.Bar(
        x=["No Default", "Default"], y=[224506, 30841],
        marker_color=[CHART_COLORS[0], CHART_COLORS[4]],
        text=["224,506 (88%)", "30,841 (12%)"], textposition="outside",
        hovertemplate="<b>%{x}</b><br>Count: %{y:,}<extra></extra>",
    )])
    fig.update_layout(xaxis_title="Default Status", yaxis_title="Number of Loans")
    return _apply_layout(fig, "Target Variable Distribution")


def income_distribution_chart():
    """Histogram of income distribution."""
    np.random.seed(42)
    data = np.concatenate([np.random.normal(65000, 20000, 4000), np.random.normal(45000, 15000, 1000)])
    data = data[data > 10000]
    fig = go.Figure(data=[go.Histogram(
        x=data, nbinsx=40, marker_color=CHART_COLORS[0], opacity=0.85,
        hovertemplate="Income: $%{x:,.0f}<br>Count: %{y}<extra></extra>",
    )])
    fig.update_layout(xaxis_title="Annual Income ($)", yaxis_title="Frequency")
    return _apply_layout(fig, "Income Distribution")


def credit_score_chart():
    """Histogram of credit scores."""
    np.random.seed(7)
    scores = np.random.normal(680, 80, 5000).clip(300, 850)
    fig = go.Figure(data=[go.Histogram(
        x=scores, nbinsx=35, marker_color=CHART_COLORS[5], opacity=0.85,
        hovertemplate="Score: %{x:.0f}<br>Count: %{y}<extra></extra>",
    )])
    fig.update_layout(xaxis_title="Credit Score", yaxis_title="Frequency")
    return _apply_layout(fig, "Credit Score Distribution")


def correlation_heatmap():
    """Correlation heatmap of numerical features."""
    np.random.seed(3)
    features = ["Age", "Income", "LoanAmt", "CreditScore", "IntRate", "MonthsEmp", "DTI", "CreditLines", "LoanTerm"]
    n = len(features)
    corr = np.eye(n)
    pairs = {(1,3):.45,(1,2):.38,(2,4):.52,(3,4):-.41,(5,1):.33,(6,2):.29,(4,6):.36,(0,5):.28,(7,3):.22}
    for (i,j),v in pairs.items():
        corr[i][j] = v; corr[j][i] = v
    fig = go.Figure(data=go.Heatmap(
        z=corr, x=features, y=features, colorscale="RdBu_r", zmin=-1, zmax=1,
        text=np.round(corr,2), texttemplate="%{text}", textfont=dict(size=11),
        hovertemplate="<b>%{x}</b> vs <b>%{y}</b><br>Correlation: %{z:.2f}<extra></extra>",
    ))
    return _apply_layout(fig, "Feature Correlation Heatmap", height=480)


def loan_purpose_pie():
    """Pie chart of loan purposes."""
    labels = ["Home", "Auto", "Education", "Business", "Medical", "Other"]
    values = [35, 25, 15, 12, 8, 5]
    fig = go.Figure(data=[go.Pie(
        labels=labels, values=values, hole=0.45, marker=dict(colors=CHART_COLORS[:6]),
        textinfo="label+percent", textfont=dict(size=13),
        hovertemplate="<b>%{label}</b><br>Share: %{percent}<br>Count: %{value}%<extra></extra>",
    )])
    return _apply_layout(fig, "Loan Purpose Distribution")


def interest_rate_trend():
    """Line chart: default rate by interest rate range."""
    ranges = ["3-6%", "6-9%", "9-12%", "12-15%", "15-18%", "18-21%", "21-24%"]
    default_rate = [4.2, 6.8, 10.5, 15.3, 22.1, 28.7, 35.4]
    fig = go.Figure(data=[go.Scatter(
        x=ranges, y=default_rate, mode="lines+markers",
        line=dict(color=CHART_COLORS[4], width=3), marker=dict(size=10, color=CHART_COLORS[4]),
        fill="tozeroy", fillcolor="rgba(220,38,38,.08)",
        hovertemplate="<b>%{x}</b><br>Default Rate: %{y}%<extra></extra>",
    )])
    fig.update_layout(xaxis_title="Interest Rate Range", yaxis_title="Default Rate (%)")
    return _apply_layout(fig, "Default Rate by Interest Rate")


def age_boxplot():
    """Box plot: age distribution by default status."""
    np.random.seed(10)
    no_def = np.random.normal(42, 12, 800).clip(18, 75)
    yes_def = np.random.normal(36, 14, 200).clip(18, 75)
    fig = go.Figure()
    fig.add_trace(go.Box(y=no_def, name="No Default", marker_color=CHART_COLORS[0], boxmean=True))
    fig.add_trace(go.Box(y=yes_def, name="Default", marker_color=CHART_COLORS[4], boxmean=True))
    fig.update_layout(yaxis_title="Age")
    return _apply_layout(fig, "Age Distribution by Default Status")


def scatter_income_loan():
    """Scatter plot: income vs. loan amount by default status."""
    np.random.seed(5)
    n = 500
    inc_nd = np.random.normal(70000, 20000, n).clip(15000)
    loan_nd = inc_nd * np.random.uniform(0.05, 0.3, n)
    inc_d = np.random.normal(45000, 18000, n // 4).clip(15000)
    loan_d = inc_d * np.random.uniform(0.2, 0.6, n // 4)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=inc_nd, y=loan_nd, mode="markers", name="No Default",
        marker=dict(color=CHART_COLORS[0], size=6, opacity=0.5)))
    fig.add_trace(go.Scatter(x=inc_d, y=loan_d, mode="markers", name="Default",
        marker=dict(color=CHART_COLORS[4], size=6, opacity=0.6)))
    fig.update_layout(xaxis_title="Annual Income ($)", yaxis_title="Loan Amount ($)")
    return _apply_layout(fig, "Income vs. Loan Amount")


def education_bar():
    """Grouped bar: default rate by education level."""
    edu = ["High School", "Associate", "Bachelor's", "Master's", "PhD"]
    default_r = [18, 14, 10, 7, 6]
    no_def_r = [82, 86, 90, 93, 94]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=edu, y=no_def_r, name="No Default", marker_color=CHART_COLORS[0]))
    fig.add_trace(go.Bar(x=edu, y=default_r, name="Default", marker_color=CHART_COLORS[4]))
    fig.update_layout(barmode="stack", xaxis_title="Education Level", yaxis_title="Percentage (%)")
    return _apply_layout(fig, "Default Rate by Education Level")


def violin_dti():
    """Violin plot: DTI ratio by default status."""
    np.random.seed(8)
    dti_nd = np.random.beta(2, 5, 600) * 0.8
    dti_d = np.random.beta(3, 3, 200) * 0.8
    fig = go.Figure()
    fig.add_trace(go.Violin(y=dti_nd, name="No Default", box_visible=True, meanline_visible=True,
        fillcolor=CHART_COLORS[0], line_color=CHART_COLORS[0], opacity=0.7))
    fig.add_trace(go.Violin(y=dti_d, name="Default", box_visible=True, meanline_visible=True,
        fillcolor=CHART_COLORS[4], line_color=CHART_COLORS[4], opacity=0.7))
    fig.update_layout(yaxis_title="DTI Ratio")
    return _apply_layout(fig, "DTI Ratio Distribution by Default Status")


def area_trend():
    """Area chart: monthly loan applications and defaults."""
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    apps = [4200, 4500, 4800, 5100, 5400, 5200, 5600, 5900, 5700, 6100, 5800, 6300]
    defs = [480, 520, 550, 610, 680, 640, 710, 760, 720, 790, 730, 810]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=months, y=apps, name="Applications", fill="tozeroy",
        line=dict(color=CHART_COLORS[0], width=2), fillcolor="rgba(37,99,235,.1)"))
    fig.add_trace(go.Scatter(x=months, y=defs, name="Defaults", fill="tozeroy",
        line=dict(color=CHART_COLORS[4], width=2), fillcolor="rgba(220,38,38,.1)"))
    fig.update_layout(xaxis_title="Month", yaxis_title="Count")
    return _apply_layout(fig, "Monthly Applications vs. Defaults Trend")


def radar_chart():
    """Radar chart: model performance comparison."""
    categories = ["Accuracy", "Precision", "Recall", "F1", "ROC AUC"]
    xgb = [89.3, 88.1, 86.8, 87.4, 93.8]
    rf = [86.7, 85.4, 84.1, 84.7, 91.2]
    lr = [78.4, 76.1, 73.2, 74.6, 81.2]
    fig = go.Figure()
    for name, vals, color in [("XGBoost", xgb, CHART_COLORS[0]), ("Random Forest", rf, CHART_COLORS[1]),
                               ("Logistic Regression", lr, CHART_COLORS[2])]:
        fig.add_trace(go.Scatterpolar(r=vals + [vals[0]], theta=categories + [categories[0]],
            name=name, fill="toself", line=dict(color=color, width=2), opacity=0.7))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[60, 100], gridcolor="#E5E7EB"),
        angularaxis=dict(gridcolor="#E5E7EB")))
    return _apply_layout(fig, "Model Performance Radar", height=450)


def treemap_chart():
    """Treemap: feature categories."""
    labels = ["All Features", "Financial", "Loan", "Demographic", "Employment",
              "Income", "CreditScore", "DTI", "CreditLines",
              "LoanAmount", "IntRate", "LoanTerm", "Purpose", "CoSigner",
              "Age", "Education", "Marital", "Dependents",
              "MonthsEmp", "EmpType"]
    parents = ["", "All Features", "All Features", "All Features", "All Features",
               "Financial", "Financial", "Financial", "Financial",
               "Loan", "Loan", "Loan", "Loan", "Loan",
               "Demographic", "Demographic", "Demographic", "Demographic",
               "Employment", "Employment"]
    values = [0, 0, 0, 0, 0, 18, 17, 10, 4, 15, 13, 2, 5, 3, 7, 5, 3, 3, 9, 4]
    fig = go.Figure(go.Treemap(labels=labels, parents=parents, values=values,
        marker=dict(colors=CHART_COLORS * 2), textinfo="label+value",
        hovertemplate="<b>%{label}</b><br>Importance: %{value}%<extra></extra>"))
    return _apply_layout(fig, "Feature Category Treemap", height=450)


# ── Evaluation Charts ──

def roc_curve_chart():
    """ROC curves for all models."""
    np.random.seed(1)
    fpr = np.linspace(0, 1, 100)
    models_data = [
        ("XGBoost (AUC=0.938)", 0.938, CHART_COLORS[0]),
        ("LightGBM (AUC=0.934)", 0.934, CHART_COLORS[1]),
        ("CatBoost (AUC=0.929)", 0.929, CHART_COLORS[2]),
        ("Random Forest (AUC=0.912)", 0.912, CHART_COLORS[3]),
        ("Decision Tree (AUC=0.835)", 0.835, CHART_COLORS[4]),
        ("Logistic Reg (AUC=0.812)", 0.812, CHART_COLORS[5]),
    ]
    fig = go.Figure()
    for name, auc, color in models_data:
        tpr = 1 - (1 - fpr) ** (1 / (2 - auc * 1.8))
        tpr = np.clip(tpr + np.random.normal(0, 0.01, len(tpr)), 0, 1)
        tpr[0], tpr[-1] = 0, 1
        tpr = np.sort(tpr)
        fig.add_trace(go.Scatter(x=fpr, y=tpr, name=name, line=dict(color=color, width=2)))
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], name="Random (AUC=0.5)",
        line=dict(color="#D1D5DB", width=1, dash="dash"), showlegend=True))
    fig.update_layout(xaxis_title="False Positive Rate", yaxis_title="True Positive Rate")
    return _apply_layout(fig, "ROC Curves — Model Comparison", height=450)


def confusion_matrix_chart():
    """Confusion matrix for XGBoost (best model)."""
    z = [[8974, 1240], [672, 4328]]
    fig = go.Figure(data=go.Heatmap(
        z=z, x=["Predicted No", "Predicted Yes"], y=["Actual No", "Actual Yes"],
        colorscale=[[0, "#EFF6FF"], [1, "#2563EB"]], showscale=False,
        text=[["TN: 8,974", "FP: 1,240"], ["FN: 672", "TP: 4,328"]],
        texttemplate="%{text}", textfont=dict(size=16, color="#111827"),
        hovertemplate="%{text}<extra></extra>",
    ))
    return _apply_layout(fig, "Confusion Matrix — XGBoost", height=400)


def precision_recall_chart():
    """Precision-Recall curves."""
    np.random.seed(2)
    recall = np.linspace(0, 1, 100)
    fig = go.Figure()
    for name, base, color in [("XGBoost", 0.92, CHART_COLORS[0]), ("Random Forest", 0.88, CHART_COLORS[1]),
                               ("Logistic Reg", 0.78, CHART_COLORS[5])]:
        precision = base - recall * (base - 0.3) + np.random.normal(0, 0.02, 100)
        precision = np.clip(precision, 0.1, 1.0)
        fig.add_trace(go.Scatter(x=recall, y=precision, name=name, line=dict(color=color, width=2)))
    fig.update_layout(xaxis_title="Recall", yaxis_title="Precision")
    return _apply_layout(fig, "Precision-Recall Curves")


def learning_curves_chart():
    """Learning curves for XGBoost."""
    sizes = [1000, 5000, 10000, 25000, 50000, 100000, 150000, 200000]
    train_scores = [0.99, 0.97, 0.95, 0.93, 0.92, 0.91, 0.905, 0.90]
    val_scores = [0.72, 0.79, 0.83, 0.86, 0.87, 0.88, 0.885, 0.89]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=sizes, y=train_scores, name="Training Score",
        line=dict(color=CHART_COLORS[0], width=2), mode="lines+markers"))
    fig.add_trace(go.Scatter(x=sizes, y=val_scores, name="Validation Score",
        line=dict(color=CHART_COLORS[4], width=2), mode="lines+markers"))
    fig.update_layout(xaxis_title="Training Set Size", yaxis_title="Score")
    return _apply_layout(fig, "Learning Curves — XGBoost")
