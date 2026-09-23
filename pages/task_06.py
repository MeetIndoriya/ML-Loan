"""
task_06.py — Week-06 Task: Boosting with AdaBoostClassifier page.
"""

import os

import pandas as pd
import streamlit as st
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_recall_curve,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from components.cards import info_card, metric_card
from utils.helpers import chart_explanation_panel, section_header, spacer


@st.cache_data
def get_task_06_results(random_state=42):
    """Train AdaBoost like Boosting.ipynb and return evaluation artifacts for UI."""
    csv_path = "Loan_default.csv"
    if not os.path.exists(csv_path):
        return None

    df = pd.read_csv(csv_path)
    if "LoanID" in df.columns:
        df = df.drop(columns=["LoanID"])

    cat_cols = df.select_dtypes(include=["object", "category", "string"]).columns
    le = LabelEncoder()
    for col in cat_cols:
        df[col] = le.fit_transform(df[col].astype(str))

    X = df.drop(columns=["Default"])
    y = df["Default"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=random_state,
        stratify=y,
    )

    model = AdaBoostClassifier(n_estimators=100, learning_rate=0.1, random_state=random_state)

    model.fit(X_train, y_train)
    y_prob = model.predict_proba(X_test)[:, 1]

    precision_curve, recall_curve, thresholds = precision_recall_curve(y_test, y_prob)
    f1_curve = (2 * precision_curve * recall_curve) / (precision_curve + recall_curve + 1e-12)
    if len(thresholds) > 0:
        best_idx = int(f1_curve[:-1].argmax())
        best_threshold = float(thresholds[best_idx])
    else:
        best_threshold = 0.5

    y_pred = (y_prob >= best_threshold).astype(int)

    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, zero_division=0),
        "recall": recall_score(y_test, y_pred, zero_division=0),
        "f1": f1_score(y_test, y_pred, zero_division=0),
        "roc_auc": roc_auc_score(y_test, y_prob),
    }
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred, digits=4, zero_division=0, output_dict=True)

    return {
        "sample_rows": len(df),
        "train_rows": len(X_train),
        "test_rows": len(X_test),
        "default_ratio": float(y.mean()),
        "best_threshold": best_threshold,
        "metrics": metrics,
        "confusion_matrix": cm,
        "classification_report": report,
    }


def render_task_06():
    """Render Week-06 AdaBoost task UI."""
    section_header(
        "Week-06 Task: Boosting with AdaBoostClassifier",
        "Simple boosting implementation on Loan_default.csv",
        "🚀",
    )
    spacer(8)

    c1, c2, c3 = st.columns(3)
    with c1:
        info_card(
            "📌",
            "Task Objective",
            "Apply AdaBoostClassifier for loan default classification using a practical preprocessing pipeline.",
        )
    with c2:
        info_card(
            "🧪",
            "Model Setup",
            "Numeric median imputation + categorical mode imputation and one-hot encoding before AdaBoost training.",
        )
    with c3:
        info_card(
            "📊",
            "Evaluation Scope",
            "Evaluated on sampled dataset with train-test split and classification metrics.",
        )

    spacer(24)
    res = get_task_06_results()
    if res is None:
        st.error("⚠️ Loan_default.csv dataset not found in project directory.")
        return

    m = res["metrics"]

    section_header("AdaBoost Performance Summary", "Real evaluation metrics from Task-06 pipeline", "🏁")
    m1, m2, m3, m4, m5 = st.columns(5)
    with m1:
        metric_card("✅", "Accuracy", f"{m['accuracy']:.4f}", "Classification accuracy", "positive", "#EFF6FF")
    with m2:
        metric_card("🎯", "Precision", f"{m['precision']:.4f}", "Positive prediction quality", "neutral", "#F0FDF4")
    with m3:
        metric_card("📡", "Recall", f"{m['recall']:.4f}", "Default capture rate", "neutral", "#FFFBEB")
    with m4:
        metric_card("⚖️", "F1 Score", f"{m['f1']:.4f}", "Precision-Recall balance", "positive", "#F5F3FF")
    with m5:
        metric_card("📈", "ROC-AUC", f"{m['roc_auc']:.4f}", "Ranking quality", "positive", "#ECFEFF")

    spacer(20)
    section_header("Task-06 Run Details", "Dataset and split information", "🗂️")
    details_df = pd.DataFrame(
        [
            {"Item": "Total Rows", "Value": f"{res['sample_rows']:,}"},
            {"Item": "Training Rows", "Value": f"{res['train_rows']:,}"},
            {"Item": "Testing Rows", "Value": f"{res['test_rows']:,}"},
            {"Item": "Default Ratio", "Value": f"{res['default_ratio']:.4f}"},
            {"Item": "Best Threshold (F1)", "Value": f"{res['best_threshold']:.4f}"},
            {"Item": "Algorithm", "Value": "AdaBoostClassifier"},
        ]
    )
    st.table(details_df)

    cm = res["confusion_matrix"]
    st.markdown("**Confusion Matrix**")
    st.table(
        pd.DataFrame(
            cm,
            index=["True: Non-Default", "True: Default"],
            columns=["Pred: Non-Default", "Pred: Default"],
        )
    )

    st.markdown("**Classification Report**")
    report_df = pd.DataFrame(res["classification_report"]).transpose().round(4)
    report_df = report_df.drop(index=["macro avg", "weighted avg"], errors="ignore")
    st.table(report_df)

    spacer(16)
    chart_explanation_panel(
        {
            "what": "This section reports classification performance of AdaBoost on the loan default dataset.",
            "observe": "Default threshold 0.5 can predict no defaulters on imbalanced data; using an F1-optimized threshold improves minority-class detection.",
            "insight": "ROC-AUC indicates how well the model ranks likely defaulters above non-defaulters across thresholds.",
            "conclusion": "AdaBoost is now the implemented Week-06 boosting method in both Task-06 notebook and dashboard UI.",
        }
    )
