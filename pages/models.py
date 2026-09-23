"""
models.py — Machine Learning Models page with model cards and comparison table.
"""
import streamlit as st
from utils.constants import MODELS
from utils.helpers import section_header, spacer
from components.cards import model_card
from components.tables import render_model_comparison_table


def render_models():
    """Render the ML Models page."""
    section_header(
        "Machine Learning Models",
        "Compare 6 algorithms trained on the loan default dataset",
        "🤖",
    )
    spacer(8)

    # ── Model Cards ──
    cols = st.columns(2)
    for i, model in enumerate(MODELS):
        with cols[i % 2]:
            model_card(model)
            spacer(16)

    spacer(24)

    # ── Comparison Table ──
    section_header("Model Comparison", "Side-by-side performance metrics (best values highlighted in green)", "📊")
    render_model_comparison_table()

    spacer(24)

    # ── Best Model Highlight ──
    st.markdown(
        """
        <div class="metric-card fade-in" style="border-left:4px solid #2563EB;">
            <div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap;">
                <div style="width:56px;height:56px;background:linear-gradient(135deg,#2563EB,#7C3AED);
                    border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:28px;">🏆</div>
                <div style="flex:1;min-width:200px;">
                    <p style="font-size:12px;text-transform:uppercase;letter-spacing:1px;color:#6B7280;
                        font-weight:600;margin:0 0 4px;">Best Performing Model</p>
                    <p style="font-size:22px;font-weight:800;color:#111827;margin:0;">XGBoost</p>
                    <p style="font-size:14px;color:#6B7280;margin:4px 0 0;">
                        89.3% accuracy • 0.938 ROC-AUC • Best overall balance of precision and recall
                    </p>
                </div>
                <div style="display:flex;gap:16px;flex-wrap:wrap;">
                    <div style="text-align:center;">
                        <p style="font-size:24px;font-weight:800;color:#2563EB;margin:0;">89.3%</p>
                        <p style="font-size:11px;color:#6B7280;margin:0;">Accuracy</p>
                    </div>
                    <div style="text-align:center;">
                        <p style="font-size:24px;font-weight:800;color:#7C3AED;margin:0;">0.938</p>
                        <p style="font-size:11px;color:#6B7280;margin:0;">ROC AUC</p>
                    </div>
                    <div style="text-align:center;">
                        <p style="font-size:24px;font-weight:800;color:#16A34A;margin:0;">87.4%</p>
                        <p style="font-size:11px;color:#6B7280;margin:0;">F1 Score</p>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
