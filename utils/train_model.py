import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

def main():
    # 1. Load data
    print("Loading dataset...")
    df = pd.read_csv("Loan_default.csv")
    print(f"Dataset shape: {df.shape}")

    # Drop unused columns (including HasMortgage and HasDependents as requested)
    X = df.drop(columns=["LoanID", "Default", "HasMortgage", "HasDependents"])
    y = df["Default"]

    # 2. Identify numerical and categorical columns
    num_cols = ["Age", "Income", "LoanAmount", "CreditScore", "MonthsEmployed", "NumCreditLines", "InterestRate", "LoanTerm", "DTIRatio"]
    cat_cols = ["Education", "EmploymentType", "MaritalStatus", "LoanPurpose", "HasCoSigner"]

    print("Numerical columns:", num_cols)
    print("Categorical columns:", cat_cols)

    # 3. Create preprocessing pipelines
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), num_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), cat_cols)
        ]
    )

    # 4. Create model pipeline
    # HistGradientBoostingClassifier is fast and performs very well on tabular data
    model_pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", HistGradientBoostingClassifier(max_iter=100, random_state=42))
        ]
    )

    # 5. Train-test split (using a 80-20 split)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    print("Training HistGradientBoostingClassifier...")
    model_pipeline.fit(X_train, y_train)

    # 6. Evaluate
    y_pred = model_pipeline.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Test Accuracy: {acc:.4f}")
    print("Classification Report:\n", classification_report(y_test, y_pred))

    # 7. Save model pipeline
    os.makedirs("models", exist_ok=True)
    with open("models/loan_model.pkl", "wb") as f:
        pickle.dump(model_pipeline, f)
    print("Model saved successfully to models/loan_model.pkl")

if __name__ == "__main__":
    main()
