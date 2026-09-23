"""
prediction.py — Dynamic prediction demo page connected to the trained ML model.
"""
import streamlit as st
import pandas as pd
import pickle
import os
from utils.helpers import section_header, spacer


@st.cache_resource
def load_model():
    """Load the trained machine learning model pipeline."""
    model_path = "models/loan_model.pkl"
    if not os.path.exists(model_path):
        return None
    try:
        with open(model_path, "rb") as f:
            return pickle.load(f)
    except Exception as e:
        st.error(f"Error loading prediction model: {e}")
        return None


# ── Callbacks ──
def handle_reset():
    """Clear all prediction state keys so widgets reset to default values."""
    for key in list(st.session_state.keys()):
        if key.startswith("pred_"):
            del st.session_state[key]


def handle_random_sample():
    """Fetch a random sample from the dataset and set session state keys before widget rendering."""
    try:
        df = pd.read_csv("Loan_default.csv")
        sample = df.sample(n=1).iloc[0]
        st.session_state["pred_age"] = int(sample["Age"])
        st.session_state["pred_edu"] = str(sample["Education"])
        st.session_state["pred_marital"] = str(sample["MaritalStatus"])
        st.session_state["pred_emp"] = str(sample["EmploymentType"])
        st.session_state["pred_months_employed"] = int(sample["MonthsEmployed"])
        st.session_state["pred_credit_lines"] = int(sample["NumCreditLines"])
        st.session_state["pred_income"] = int(sample["Income"])
        st.session_state["pred_credit"] = int(sample["CreditScore"])
        st.session_state["pred_dti"] = float(sample["DTIRatio"])
        st.session_state["pred_loan"] = int(sample["LoanAmount"])
        st.session_state["pred_int"] = float(sample["InterestRate"])
        st.session_state["pred_term"] = int(sample["LoanTerm"])
        st.session_state["pred_purpose"] = str(sample["LoanPurpose"])
        st.session_state["pred_cosigner"] = str(sample["HasCoSigner"])
    except Exception as e:
        st.session_state["pred_error"] = f"Error loading sample from dataset: {e}"


def render_prediction():
    """Render the interactive loan default prediction form."""
    section_header(
        "Prediction Demo",
        "Enter applicant details to predict loan default risk in real-time",
        "🎯",
    )
    spacer(8)

    # Inform the user about the live inference status
    st.markdown(
        """
        <div style="background:#EFF6FF;border:1px solid #BFDBFE;border-radius:10px;padding:14px 18px;
            font-size:14px;color:#1E40AF;display:flex;gap:8px;margin-bottom:24px;" class="fade-in">
            <span>ℹ️</span>
            <span><strong>Live Inference Active:</strong> Predictions are computed in real-time using a gradient boosted model trained on the Loan Default dataset.</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Display error if any occurred in the callback
    if "pred_error" in st.session_state:
        st.error(st.session_state["pred_error"])
        del st.session_state["pred_error"]

    # Load trained model
    model = load_model()

    # Initialize session state keys for form inputs if not already present
    if "pred_age" not in st.session_state:
        st.session_state["pred_age"] = 35
        st.session_state["pred_edu"] = "Bachelor's"
        st.session_state["pred_marital"] = "Single"
        st.session_state["pred_emp"] = "Full-time"
        st.session_state["pred_months_employed"] = 24
        st.session_state["pred_credit_lines"] = 2
        st.session_state["pred_income"] = 72500
        st.session_state["pred_credit"] = 720
        st.session_state["pred_dti"] = 0.35
        st.session_state["pred_loan"] = 15000
        st.session_state["pred_int"] = 12.5
        st.session_state["pred_term"] = 36
        st.session_state["pred_purpose"] = "Home"
        st.session_state["pred_cosigner"] = "No"

    # Define option lists
    edu_options = ["High School", "Bachelor's", "Master's", "PhD"]
    marital_options = ["Single", "Married", "Divorced"]
    emp_options = ["Full-time", "Part-time", "Self-employed", "Unemployed"]
    purpose_options = ["Home", "Auto", "Education", "Business", "Other"]
    cosigner_options = ["Yes", "No"]

    # Render prediction form
    with st.form("prediction_form"):
        st.markdown("##### 👤 Applicant Information")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.number_input("Age", min_value=18, max_value=80, key="pred_age")
        with c2:
            st.selectbox("Education", edu_options, key="pred_edu")
        with c3:
            st.selectbox("Marital Status", marital_options, key="pred_marital")

        c4, c5, c6 = st.columns(3)
        with c4:
            st.selectbox("Employment Type", emp_options, key="pred_emp")
        with c5:
            st.number_input("Months Employed", min_value=0, max_value=120, key="pred_months_employed")
        with c6:
            st.number_input("Number of Credit Lines", min_value=1, max_value=10, key="pred_credit_lines")

        st.markdown("---")
        st.markdown("##### 💰 Financial Details")
        c7, c8, c9 = st.columns(3)
        with c7:
            st.number_input("Annual Income ($)", min_value=10000, max_value=500000, step=1000, key="pred_income")
        with c8:
            st.number_input("Credit Score", min_value=300, max_value=850, key="pred_credit")
        with c9:
            st.number_input("DTI Ratio", min_value=0.0, max_value=1.0, step=0.01, key="pred_dti")

        st.markdown("---")
        st.markdown("##### 🏦 Loan Details")
        c10, c11, c12 = st.columns(3)
        with c10:
            st.number_input("Loan Amount ($)", min_value=1000, max_value=200000, step=500, key="pred_loan")
        with c11:
            st.number_input("Interest Rate (%)", min_value=1.0, max_value=30.0, step=0.1, key="pred_int")
        with c12:
            st.number_input("Loan Term (Months)", min_value=12, max_value=60, step=6, key="pred_term")

        c13, c14, _ = st.columns(3)
        with c13:
            st.selectbox("Loan Purpose", purpose_options, key="pred_purpose")
        with c14:
            st.selectbox("Has Co-Signer", cosigner_options, key="pred_cosigner")

        st.markdown("")
        fc1, fc2, fc3 = st.columns(3)
        with fc1:
            submitted = st.form_submit_button("🔮  Predict", use_container_width=True, type="primary")
        with fc2:
            st.form_submit_button("🔄  Reset", use_container_width=True, on_click=handle_reset)
        with fc3:
            st.form_submit_button("🎲  Random Sample", use_container_width=True, on_click=handle_random_sample)

    # ── Inference Result Rendering ──
    if submitted:
        if model is None:
            st.error("Prediction model not found. Please train the model using train_model.py first.")
            return

        # Prepare inputs exactly mapping to columns expected by the model pipeline
        input_data = pd.DataFrame([{
            "Age": st.session_state["pred_age"],
            "Income": st.session_state["pred_income"],
            "LoanAmount": st.session_state["pred_loan"],
            "CreditScore": st.session_state["pred_credit"],
            "MonthsEmployed": st.session_state["pred_months_employed"],
            "NumCreditLines": st.session_state["pred_credit_lines"],
            "InterestRate": st.session_state["pred_int"],
            "LoanTerm": st.session_state["pred_term"],
            "DTIRatio": st.session_state["pred_dti"],
            "Education": st.session_state["pred_edu"],
            "EmploymentType": st.session_state["pred_emp"],
            "MaritalStatus": st.session_state["pred_marital"],
            "LoanPurpose": st.session_state["pred_purpose"],
            "HasCoSigner": st.session_state["pred_cosigner"]
        }])

        try:
            # Predict probability and class label
            prob_default = model.predict_proba(input_data)[0][1]
            pred_default = model.predict(input_data)[0]

            spacer(16)

            if pred_default == 1:
                # High Risk - red card
                risk_percentage = prob_default * 100
                st.markdown(
                    f"""
                    <div class="metric-card fade-in" style="border-left:4px solid #DC2626; background: #FEF2F2; border-radius: 12px; padding: 20px;">
                        <div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap;">
                            <div style="width:56px;height:56px;background:#FEE2E2;border-radius:12px;
                                display:flex;align-items:center;justify-content:center;font-size:28px;">❌</div>
                            <div style="flex:1;">
                                <p style="font-size:12px;text-transform:uppercase;letter-spacing:1px;color:#991B1B;
                                    font-weight:600;margin:0 0 4px;">Prediction Result</p>
                                <p style="font-size:22px;font-weight:800;color:#DC2626;margin:0;">High Risk — Likely to Default</p>
                                <p style="font-size:14px;color:#7F1D1D;margin:4px 0 0;">
                                    Confidence: {risk_percentage:.1f}% • Risk Score: {prob_default:.3f} • Category: Danger
                                </p>
                            </div>
                            <div style="text-align:center;">
                                <p style="font-size:32px;font-weight:800;color:#DC2626;margin:0;">{risk_percentage:.1f}%</p>
                                <p style="font-size:11px;color:#991B1B;margin:0;">Confidence</p>
                            </div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            else:
                # Low Risk - green card
                safe_percentage = (1 - prob_default) * 100
                st.markdown(
                    f"""
                    <div class="metric-card fade-in" style="border-left:4px solid #16A34A; background: #F0FDF4; border-radius: 12px; padding: 20px;">
                        <div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap;">
                            <div style="width:56px;height:56px;background:#DCFCE7;border-radius:12px;
                                display:flex;align-items:center;justify-content:center;font-size:28px;">✅</div>
                            <div style="flex:1;">
                                <p style="font-size:12px;text-transform:uppercase;letter-spacing:1px;color:#166534;
                                    font-weight:600;margin:0 0 4px;">Prediction Result</p>
                                <p style="font-size:22px;font-weight:800;color:#16A34A;margin:0;">Low Risk — Safe to Approve</p>
                                <p style="font-size:14px;color:#166534;margin:4px 0 0;">
                                    Confidence: {safe_percentage:.1f}% • Risk Score: {prob_default:.3f} • Category: Safe
                                </p>
                            </div>
                            <div style="text-align:center;">
                                <p style="font-size:32px;font-weight:800;color:#16A34A;margin:0;">{safe_percentage:.1f}%</p>
                                <p style="font-size:11px;color:#166534;margin:0;">Confidence</p>
                            </div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        except Exception as e:
            st.error(f"Error during model prediction: {e}")
