"""
constants.py — All dummy data, color palette, feature definitions, and static content
for the Loan Default Prediction Dashboard.

All data is STATIC / PLACEHOLDER. Replace with real data when integrating the ML backend.
"""

# ══════════════════════════════════════════════════════════════
# COLOR PALETTE
# ══════════════════════════════════════════════════════════════

COLORS = {
    "primary": "#2563EB",
    "primary_light": "#3B82F6",
    "primary_dark": "#1E40AF",
    "secondary": "#1E40AF",
    "success": "#16A34A",
    "success_light": "#22C55E",
    "warning": "#F59E0B",
    "warning_light": "#FBBF24",
    "danger": "#DC2626",
    "danger_light": "#EF4444",
    "background": "#F8FAFC",
    "card_bg": "#FFFFFF",
    "border": "#E5E7EB",
    "text_primary": "#111827",
    "text_secondary": "#6B7280",
    "text_muted": "#9CA3AF",
    "accent_purple": "#7C3AED",
    "accent_teal": "#0D9488",
    "accent_indigo": "#4F46E5",
    "accent_rose": "#E11D48",
}

# Plotly-friendly color sequence
CHART_COLORS = [
    "#2563EB", "#7C3AED", "#0D9488", "#F59E0B",
    "#DC2626", "#16A34A", "#E11D48", "#4F46E5",
    "#0EA5E9", "#8B5CF6", "#14B8A6", "#F97316",
]

# ══════════════════════════════════════════════════════════════
# PROJECT METADATA
# ══════════════════════════════════════════════════════════════

PROJECT_NAME = "Loan Default Prediction"
PROJECT_SUBTITLE = "Understand how Machine Learning predicts whether a customer is likely to default on a loan."
PROJECT_VERSION = "1.0.0"
PROJECT_AUTHOR = "ML Project Team"
GITHUB_URL = "https://github.com"
LINKEDIN_URL = "https://linkedin.com"

# ══════════════════════════════════════════════════════════════
# NAVIGATION
# ══════════════════════════════════════════════════════════════

NAV_ITEMS = [
    ("🏠", "Home"),
    ("📦", "Dataset"),
    ("📊", "EDA"),
    ("⚙️", "Preprocessing"),
    ("📈", "Week-05 Task"),
    ("🚀", "Boosting"),
    ("🎯", "Project Demo"),
]

# ══════════════════════════════════════════════════════════════
# DATASET SUMMARY (dummy values)
# ══════════════════════════════════════════════════════════════

DATASET_STATS = {
    "total_rows": 255_347,
    "total_columns": 18,
    "categorical_features": 6,
    "numerical_features": 11,
    "target_variable": "Default",
    "dataset_size_mb": 23.7,
    "missing_percentage": 2.3,
    "completion_rate": 97.7,
}

# ══════════════════════════════════════════════════════════════
# FEATURE DEFINITIONS
# ══════════════════════════════════════════════════════════════

FEATURES = [
    {
        "name": "Age",
        "dtype": "int64",
        "example": "34",
        "description": "Age of the loan applicant in years",
        "icon": "👤",
        "category": "Demographic",
    },
    {
        "name": "Income",
        "dtype": "float64",
        "example": "$72,500",
        "description": "Annual income of the applicant",
        "icon": "💰",
        "category": "Financial",
    },
    {
        "name": "LoanAmount",
        "dtype": "float64",
        "example": "$15,000",
        "description": "Total loan amount requested",
        "icon": "🏦",
        "category": "Loan",
    },
    {
        "name": "CreditScore",
        "dtype": "int64",
        "example": "720",
        "description": "Applicant's credit score (300–850)",
        "icon": "📊",
        "category": "Financial",
    },
    {
        "name": "MonthsEmployed",
        "dtype": "int64",
        "example": "48",
        "description": "Number of months at current job",
        "icon": "💼",
        "category": "Employment",
    },
    {
        "name": "NumCreditLines",
        "dtype": "int64",
        "example": "4",
        "description": "Number of open credit lines",
        "icon": "💳",
        "category": "Financial",
    },
    {
        "name": "InterestRate",
        "dtype": "float64",
        "example": "12.5%",
        "description": "Interest rate on the loan",
        "icon": "📈",
        "category": "Loan",
    },
    {
        "name": "LoanTerm",
        "dtype": "int64",
        "example": "36",
        "description": "Loan term in months",
        "icon": "📅",
        "category": "Loan",
    },
    {
        "name": "DTIRatio",
        "dtype": "float64",
        "example": "0.35",
        "description": "Debt-to-Income ratio",
        "icon": "⚖️",
        "category": "Financial",
    },
    {
        "name": "Education",
        "dtype": "category",
        "example": "Bachelor's",
        "description": "Highest education level attained",
        "icon": "🎓",
        "category": "Demographic",
    },
    {
        "name": "EmploymentType",
        "dtype": "category",
        "example": "Full-time",
        "description": "Type of employment",
        "icon": "🏢",
        "category": "Employment",
    },
    {
        "name": "MaritalStatus",
        "dtype": "category",
        "example": "Married",
        "description": "Marital status of applicant",
        "icon": "💍",
        "category": "Demographic",
    },
    {
        "name": "HasMortgage",
        "dtype": "category",
        "example": "Yes",
        "description": "Whether applicant has a mortgage",
        "icon": "🏠",
        "category": "Financial",
    },
    {
        "name": "HasDependents",
        "dtype": "category",
        "example": "Yes",
        "description": "Whether applicant has dependents",
        "icon": "👨‍👩‍👧",
        "category": "Demographic",
    },
    {
        "name": "LoanPurpose",
        "dtype": "category",
        "example": "Home",
        "description": "Purpose of the loan",
        "icon": "🎯",
        "category": "Loan",
    },
    {
        "name": "HasCoSigner",
        "dtype": "category",
        "example": "No",
        "description": "Whether the loan has a co-signer",
        "icon": "🤝",
        "category": "Loan",
    },
    {
        "name": "Default",
        "dtype": "int64 (binary)",
        "example": "0",
        "description": "Target — 1 if defaulted, 0 otherwise",
        "icon": "🎯",
        "category": "Target",
    },
]

# ══════════════════════════════════════════════════════════════
# FEATURE IMPORTANCE (dummy ranking)
# ══════════════════════════════════════════════════════════════

FEATURE_IMPORTANCE = [
    ("Income", 0.182),
    ("Credit Score", 0.168),
    ("Loan Amount", 0.145),
    ("Interest Rate", 0.132),
    ("DTI Ratio", 0.098),
    ("Months Employed", 0.087),
    ("Age", 0.072),
    ("Education", 0.054),
    ("Num Credit Lines", 0.038),
    ("Loan Term", 0.024),
]

# ══════════════════════════════════════════════════════════════
# MODEL DATA
# ══════════════════════════════════════════════════════════════

MODELS = [
    {
        "name": "Logistic Regression",
        "icon": "📐",
        "description": "A linear model that estimates the probability of default using a logistic function. Ideal as a baseline model.",
        "advantages": ["Simple and interpretable", "Fast training", "Works well with linearly separable data", "Low computational cost"],
        "disadvantages": ["Cannot capture non-linear relationships", "Sensitive to outliers", "Requires feature scaling"],
        "difficulty": "Beginner",
        "speed": "Very Fast",
        "accuracy": 78.4,
    },
    {
        "name": "Decision Tree",
        "icon": "🌳",
        "description": "A tree-structured model that splits data based on feature thresholds. Easy to visualize and interpret.",
        "advantages": ["Highly interpretable", "No feature scaling needed", "Handles non-linear data", "Captures interactions"],
        "disadvantages": ["Prone to overfitting", "Sensitive to noisy data", "Unstable — small data changes alter tree"],
        "difficulty": "Beginner",
        "speed": "Fast",
        "accuracy": 81.2,
    },
    {
        "name": "Random Forest",
        "icon": "🌲",
        "description": "An ensemble of decision trees that reduces variance through bagging. Robust and widely used.",
        "advantages": ["Reduces overfitting", "Handles missing values", "Feature importance built-in", "Robust to outliers"],
        "disadvantages": ["Less interpretable", "Slower training", "Memory intensive", "Can overfit noisy data"],
        "difficulty": "Intermediate",
        "speed": "Moderate",
        "accuracy": 86.7,
    },
    {
        "name": "XGBoost",
        "icon": "🚀",
        "description": "Extreme Gradient Boosting — a powerful boosting algorithm that builds trees sequentially to correct errors.",
        "advantages": ["State-of-the-art performance", "Built-in regularization", "Handles missing values", "Parallel processing"],
        "disadvantages": ["Requires hyperparameter tuning", "Longer training time", "Less interpretable", "Overfits on small data"],
        "difficulty": "Advanced",
        "speed": "Moderate",
        "accuracy": 89.3,
    },
    {
        "name": "LightGBM",
        "icon": "⚡",
        "description": "Light Gradient Boosting Machine — optimized for speed and efficiency with leaf-wise tree growth.",
        "advantages": ["Extremely fast", "Low memory usage", "Handles large datasets", "High accuracy"],
        "disadvantages": ["Sensitive to overfitting on small data", "Complex parameters", "Leaf-wise growth may overfit"],
        "difficulty": "Advanced",
        "speed": "Very Fast",
        "accuracy": 88.9,
    },
    {
        "name": "CatBoost",
        "icon": "🐱",
        "description": "Categorical Boosting — handles categorical features natively without encoding. Robust and accurate.",
        "advantages": ["Native categorical support", "Less hyperparameter tuning", "Robust to overfitting", "GPU support"],
        "disadvantages": ["Slower training than LightGBM", "Large model size", "Less community support"],
        "difficulty": "Intermediate",
        "speed": "Moderate",
        "accuracy": 88.1,
    },
]

# Model comparison metrics (dummy)
MODEL_COMPARISON = [
    {"Model": "Logistic Regression", "Accuracy": 0.784, "Precision": 0.761, "Recall": 0.732, "F1": 0.746, "ROC AUC": 0.812, "Train Time": "0.3s", "Pred Speed": "0.01s"},
    {"Model": "Decision Tree", "Accuracy": 0.812, "Precision": 0.798, "Recall": 0.779, "F1": 0.788, "ROC AUC": 0.835, "Train Time": "0.8s", "Pred Speed": "0.01s"},
    {"Model": "Random Forest", "Accuracy": 0.867, "Precision": 0.854, "Recall": 0.841, "F1": 0.847, "ROC AUC": 0.912, "Train Time": "4.2s", "Pred Speed": "0.05s"},
    {"Model": "XGBoost", "Accuracy": 0.893, "Precision": 0.881, "Recall": 0.868, "F1": 0.874, "ROC AUC": 0.938, "Train Time": "6.1s", "Pred Speed": "0.03s"},
    {"Model": "LightGBM", "Accuracy": 0.889, "Precision": 0.876, "Recall": 0.862, "F1": 0.869, "ROC AUC": 0.934, "Train Time": "2.8s", "Pred Speed": "0.02s"},
    {"Model": "CatBoost", "Accuracy": 0.881, "Precision": 0.869, "Recall": 0.855, "F1": 0.862, "ROC AUC": 0.929, "Train Time": "5.5s", "Pred Speed": "0.04s"},
]

# ══════════════════════════════════════════════════════════════
# WORKFLOW STEPS
# ══════════════════════════════════════════════════════════════

WORKFLOW_STEPS = [
    {"step": 1, "title": "Dataset Collection", "icon": "📦", "desc": "Gather and load the loan default dataset"},
    {"step": 2, "title": "Data Cleaning", "icon": "🧹", "desc": "Handle missing values, duplicates, and errors"},
    {"step": 3, "title": "EDA", "icon": "📊", "desc": "Explore distributions, correlations, and patterns"},
    {"step": 4, "title": "Preprocessing", "icon": "⚙️", "desc": "Encode, scale, and transform features"},
    {"step": 5, "title": "Feature Engineering", "icon": "🔧", "desc": "Create and select the most predictive features"},
    {"step": 6, "title": "Model Training", "icon": "🤖", "desc": "Train multiple ML algorithms on the data"},
    {"step": 7, "title": "Evaluation", "icon": "📉", "desc": "Compare models using metrics and visualizations"},
    {"step": 8, "title": "Deployment", "icon": "🚀", "desc": "Deploy the best model for real-time predictions"},
]

# ══════════════════════════════════════════════════════════════
# PROJECT OVERVIEW CARDS
# ══════════════════════════════════════════════════════════════

OVERVIEW_CARDS = [
    {
        "icon": "🎯",
        "title": "What is the Problem?",
        "description": "Predict whether a borrower is likely to default on their loan using their financial and demographic details.",
    },
    {
        "icon": "💼",
        "title": "Why it Matters",
        "description": "Helps banks & lenders identify high-risk borrowers early, reducing financial loss while speeding up loan approvals.",
    },
    {
        "icon": "📦",
        "title": "The Data",
        "description": "Analyzes 255,000+ loan records with key financial indicators like income, credit score, loan amount, and employment history.",
    },
    {
        "icon": "⚡",
        "title": "How it Works",
        "description": "Machine Learning algorithms evaluate applicant data to generate a real-time risk score and approval recommendation.",
    },
]

# ══════════════════════════════════════════════════════════════
# DID YOU KNOW FACTS
# ══════════════════════════════════════════════════════════════

DID_YOU_KNOW_FACTS = [
    "💡 Banks lose approximately $150 billion annually due to loan defaults worldwide.",
    "💡 Machine Learning models can reduce loan default rates by 25–40% compared to traditional methods.",
    "💡 Credit score alone predicts only 60% of defaults — ML uses 15+ features for better accuracy.",
    "💡 XGBoost is the most popular algorithm for credit risk modeling in the financial industry.",
    "💡 The global lending market is expected to reach $8.8 trillion by 2027.",
    "💡 Feature engineering can improve model accuracy by 10–25% in financial prediction tasks.",
]

# ══════════════════════════════════════════════════════════════
# PREPROCESSING STEPS
# ══════════════════════════════════════════════════════════════

PREPROCESSING_STEPS = [
    {
        "title": "Missing Value Treatment",
        "icon": "🔍",
        "description": "Identified and imputed 2.3% missing values using median for numerical and mode for categorical features.",
        "before": "2.3% missing",
        "after": "0% missing",
        "method": "Median / Mode Imputation",
    },
    {
        "title": "Outlier Detection",
        "icon": "📏",
        "description": "Detected and capped outliers using IQR method for Income, LoanAmount, and InterestRate columns.",
        "before": "847 outliers",
        "after": "0 outliers",
        "method": "IQR Capping",
    },
    {
        "title": "Categorical Encoding",
        "icon": "🔢",
        "description": "Converted categorical variables to numerical representations using Label Encoding and One-Hot Encoding.",
        "before": "6 categorical cols",
        "after": "14 encoded cols",
        "method": "Label + One-Hot Encoding",
    },
    {
        "title": "Feature Scaling",
        "icon": "⚖️",
        "description": "Standardized numerical features to zero mean and unit variance for optimal model performance.",
        "before": "Varied scales",
        "after": "Standardized",
        "method": "StandardScaler",
    },
    {
        "title": "Class Imbalance",
        "icon": "📊",
        "description": "Addressed class imbalance (88:12 ratio) using SMOTE oversampling to create balanced training data.",
        "before": "88:12 ratio",
        "after": "50:50 ratio",
        "method": "SMOTE Oversampling",
    },
    {
        "title": "Train-Test Split",
        "icon": "✂️",
        "description": "Split dataset into 80% training and 20% testing sets with stratified sampling to maintain class distribution.",
        "before": "255,347 rows",
        "after": "204,278 train / 51,069 test",
        "method": "Stratified 80-20 Split",
    },
]

# ══════════════════════════════════════════════════════════════
# FAQ
# ══════════════════════════════════════════════════════════════

FAQ_ITEMS = [
    ("What is Loan Default Prediction?", "Loan default prediction is the process of using machine learning algorithms to predict whether a borrower will fail to repay their loan based on their financial profile and loan characteristics."),
    ("Why is this important?", "Financial institutions lose billions annually due to loan defaults. Predicting defaults in advance helps banks minimize risk, make better lending decisions, and protect their portfolios."),
    ("What data is used?", "The model uses 18 features including age, income, credit score, loan amount, interest rate, employment history, education, debt-to-income ratio, and more."),
    ("Which ML models are used?", "We compare 6 models: Logistic Regression, Decision Tree, Random Forest, XGBoost, LightGBM, and CatBoost to find the best performer."),
    ("How accurate is the prediction?", "The best model (XGBoost) achieves 89.3% accuracy with a 0.938 ROC-AUC score, indicating excellent discrimination between defaulters and non-defaulters."),
    ("Can this be used in production?", "This dashboard is a prototype. With proper backend integration, API development, and regulatory compliance, it can be deployed as a production system."),
]

# ══════════════════════════════════════════════════════════════
# ML GLOSSARY
# ══════════════════════════════════════════════════════════════

GLOSSARY = {
    "Accuracy": "The percentage of correct predictions out of all predictions made.",
    "Precision": "Of all positive predictions, how many were actually positive.",
    "Recall": "Of all actual positives, how many were correctly predicted.",
    "F1-Score": "The harmonic mean of precision and recall — balances both metrics.",
    "ROC-AUC": "Area Under the ROC Curve — measures the model's ability to distinguish between classes.",
    "Overfitting": "When a model learns noise in training data and performs poorly on new data.",
    "Feature Engineering": "The process of creating new features or transforming existing ones to improve model performance.",
    "Cross-Validation": "A technique to evaluate model performance by splitting data into multiple train-test folds.",
    "Hyperparameter Tuning": "The process of finding the optimal settings for a machine learning algorithm.",
    "Ensemble Learning": "Combining multiple models to produce better predictions than any single model.",
    "SMOTE": "Synthetic Minority Over-sampling Technique — creates synthetic samples for imbalanced classes.",
    "Gradient Boosting": "An ensemble technique that builds models sequentially, each correcting the previous model's errors.",
}

# ══════════════════════════════════════════════════════════════
# CHART EXPLANATION TEMPLATES
# ══════════════════════════════════════════════════════════════

CHART_EXPLANATIONS = {
    "default_distribution": {
        "what": "This bar chart shows the distribution of the target variable — how many loans defaulted vs. did not default.",
        "observe": "Look at the class imbalance: the majority of loans are non-defaulting, which is expected in real-world lending data.",
        "insight": "An imbalanced dataset requires techniques like SMOTE or class weights to prevent the model from being biased toward the majority class.",
        "conclusion": "Approximately 12% of loans in the dataset defaulted, indicating a moderately imbalanced classification problem.",
    },
    "income_distribution": {
        "what": "This histogram shows the distribution of annual income across all loan applicants.",
        "observe": "Notice the right-skewed distribution — most applicants have moderate income, with fewer high-income earners.",
        "insight": "Income is a strong predictor of loan default. Lower-income applicants tend to have higher default rates.",
        "conclusion": "The median income is around $65,000, with the majority falling between $30,000 and $100,000.",
    },
    "credit_score": {
        "what": "This histogram displays the distribution of credit scores across all applicants.",
        "observe": "The distribution is roughly normal, centered around 650–700, which represents average creditworthiness.",
        "insight": "Applicants with scores below 600 have significantly higher default rates — this is a critical feature for prediction.",
        "conclusion": "Credit score is one of the top 3 most important features in predicting loan default.",
    },
    "correlation_heatmap": {
        "what": "This heatmap shows the Pearson correlation coefficients between all numerical features.",
        "observe": "Darker colors indicate stronger correlations. Look for features that are highly correlated with the target variable.",
        "insight": "Highly correlated features may cause multicollinearity. Consider removing one of each correlated pair.",
        "conclusion": "Income and CreditScore show moderate positive correlation. LoanAmount and InterestRate show the strongest correlation with default.",
    },
    "age_vs_default": {
        "what": "This box plot compares the age distribution of defaulters vs. non-defaulters.",
        "observe": "Compare the median, quartiles, and outliers between the two groups.",
        "insight": "Younger applicants tend to have slightly higher default rates, possibly due to less financial stability.",
        "conclusion": "While age alone is not a strong predictor, it contributes meaningful information when combined with other features.",
    },
    "loan_purpose": {
        "what": "This pie chart shows the breakdown of loan purposes across all applications.",
        "observe": "Identify which purposes are most common and which have higher default rates.",
        "insight": "Certain loan purposes (e.g., debt consolidation) may indicate higher financial stress and default risk.",
        "conclusion": "Home and auto loans make up 60% of applications, while education and business loans have higher default rates.",
    },
    "interest_rate": {
        "what": "This line chart shows how average default rate changes across different interest rate ranges.",
        "observe": "Notice the clear upward trend — higher interest rates correlate with higher default rates.",
        "insight": "High interest rates increase monthly payments, making it harder for borrowers to keep up with their loans.",
        "conclusion": "Applicants with interest rates above 15% have a default rate 3x higher than those below 8%.",
    },
    "feature_importance": {
        "what": "This horizontal bar chart ranks features by their importance in predicting loan default.",
        "observe": "Income and Credit Score are the most important features, followed by Loan Amount and Interest Rate.",
        "insight": "Feature importance helps us understand which factors drive predictions and builds trust in the model.",
        "conclusion": "The top 4 features account for 62.7% of the model's decision-making, indicating a well-structured dataset.",
    },
    "roc_curve": {
        "what": "The ROC curve plots True Positive Rate vs. False Positive Rate at various classification thresholds.",
        "observe": "A curve closer to the top-left corner indicates better performance. The diagonal line represents random guessing.",
        "insight": "XGBoost (AUC=0.938) significantly outperforms Logistic Regression (AUC=0.812), showing superior discrimination.",
        "conclusion": "All ensemble models achieve AUC > 0.90, indicating excellent ability to distinguish defaulters from non-defaulters.",
    },
    "confusion_matrix": {
        "what": "The confusion matrix shows the count of True Positives, True Negatives, False Positives, and False Negatives.",
        "observe": "Ideally, the diagonal (TP and TN) should have high values while off-diagonal (FP and FN) should be low.",
        "insight": "In loan default prediction, False Negatives (predicting no default when there is one) are more costly than False Positives.",
        "conclusion": "The XGBoost model correctly identifies 87% of actual defaults while maintaining a low false positive rate.",
    },
    "scatter_income_loan": {
        "what": "This scatter plot shows the relationship between Income and Loan Amount, colored by default status.",
        "observe": "Look for clusters and patterns — defaulters may concentrate in specific regions of the plot.",
        "insight": "Applicants who request large loans relative to their income are more likely to default.",
        "conclusion": "A clear pattern emerges: high loan-to-income ratios are strongly associated with default.",
    },
    "education_default": {
        "what": "This grouped bar chart shows default rates across different education levels.",
        "observe": "Compare the default rate (percentage) across education categories.",
        "insight": "Higher education levels generally correlate with lower default rates, likely due to higher earning potential.",
        "conclusion": "Applicants with a PhD have a 6% default rate, compared to 18% for those with only a high school diploma.",
    },
}
