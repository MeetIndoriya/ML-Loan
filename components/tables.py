"""
tables.py — Model comparison table with highlighted best values.
"""
import streamlit as st
from utils.constants import MODEL_COMPARISON


def render_model_comparison_table() -> None:
    """Render a styled model comparison table with best values highlighted."""
    # Find best values for each metric
    metrics = ["Accuracy", "Precision", "Recall", "F1", "ROC AUC"]
    best = {}
    for m in metrics:
        best[m] = max(row[m] for row in MODEL_COMPARISON)

    rows_html = ""
    for row in MODEL_COMPARISON:
        cells = f'<td style="font-weight:600;">{row["Model"]}</td>'
        for m in metrics:
            val = row[m]
            cls = ' class="best-value"' if val == best[m] else ""
            cells += f"<td{cls}>{val:.3f}</td>"
        cells += f"<td>{row['Train Time']}</td>"
        cells += f"<td>{row['Pred Speed']}</td>"
        rows_html += f"<tr>{cells}</tr>"

    st.markdown(
        f"""
        <div style="overflow-x:auto;">
            <table class="comparison-table">
                <thead>
                    <tr>
                        <th>Model</th><th>Accuracy</th><th>Precision</th>
                        <th>Recall</th><th>F1 Score</th><th>ROC AUC</th>
                        <th>Train Time</th><th>Pred Speed</th>
                    </tr>
                </thead>
                <tbody>{rows_html}</tbody>
            </table>
        </div>
        """,
        unsafe_allow_html=True,
    )
