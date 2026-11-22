import pandas as pd
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

def evaluate_predictions(frame: pd.DataFrame) -> dict:
    """Evaluate binary predictions against supplied reference labels."""
    required = {"y_true", "y_pred"}
    missing = required - set(frame.columns)
    if missing:
        raise ValueError(f"Missing evaluation columns: {sorted(missing)}")
    y_true = frame["y_true"].astype(int)
    y_pred = frame["y_pred"].astype(int)
    if not set(y_true.unique()).issubset({0, 1}) or not set(y_pred.unique()).issubset({0, 1}):
        raise ValueError("y_true and y_pred must contain only 0 or 1")
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()
    specificity = float(tn / (tn + fp)) if tn + fp else 0.0
    return {
        "n": int(len(frame)),
        "tn": int(tn), "fp": int(fp), "fn": int(fn), "tp": int(tp),
        "precision": float(precision_score(y_true, y_pred, zero_division=0)),
        "sensitivity_recall": float(recall_score(y_true, y_pred, zero_division=0)),
        "specificity": specificity,
        "f1": float(f1_score(y_true, y_pred, zero_division=0)),
    }
