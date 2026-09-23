# Loan Default ML Project

## Task-06: Boosting (AdaBoostClassifier)

`Task-06.ipynb` applies a simple boosting model on `Loan_default.csv` using `AdaBoostClassifier`.

### What Task-06 does

1. Loads `Loan_default.csv`.
2. Samples up to `50,000` rows for faster practical execution.
3. Uses `Default` as target and drops `LoanID` (ID-like column).
4. Builds preprocessing pipeline:
   - Numeric columns: median imputation
   - Categorical columns: most-frequent imputation + one-hot encoding
5. Trains and evaluates:
   - **Boosting**: `AdaBoostClassifier`
6. Prints model metrics:
   - Accuracy
   - Precision
   - Recall
   - F1
   - ROC-AUC
7. Prints the final boosting results table for easy interpretation.

### How to run Task-06

Open `Task-06.ipynb` in Jupyter Notebook or PyCharm Notebook editor and run all cells sequentially.

Optional (script-style run): export the notebook cells to a `.py` file, then execute with:

```powershell
.\.venv\Scripts\python.exe task_06_run.py
```

### Expected output

- Dataset shape and target ratio
- Metrics table for `AdaBoostClassifier`
