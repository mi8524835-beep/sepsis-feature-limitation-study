import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    roc_auc_score,
    average_precision_score,
    accuracy_score,
    f1_score,
    classification_report
)
from xgboost import XGBClassifier

print("데이터 불러오는 중...")

X_tab = pd.read_csv("X_tab.csv")
y = np.load("y_mortality.npy")

print("=== Mortality prediction ===")
print("y mean:", y.mean())
print("y unique:", np.unique(y))

# split
X_train, X_test, y_train, y_test = train_test_split(
    X_tab, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

print("원본 X_tab shape:", X_tab.shape)
print("원본 y shape:", y.shape)

# stay_id 제거
X = X_tab.drop(columns=["stay_id"]).copy()

print("모델 입력 X shape:", X.shape)

# train / test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

print("train shape:", X_train.shape, y_train.shape)
print("test shape:", X_test.shape, y_test.shape)

# XGBoost 모델
model = XGBClassifier(
    n_estimators=300,
    max_depth=4,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="binary:logistic",
    eval_metric="logloss",
    random_state=42
)

print("학습 시작...")
model.fit(X_train, y_train)

print("예측 중...")
y_pred_proba = model.predict_proba(X_test)[:, 1]
y_pred = (y_pred_proba >= 0.5).astype(int)

auroc = roc_auc_score(y_test, y_pred_proba)
auprc = average_precision_score(y_test, y_pred_proba)
f1 = f1_score(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)

print(f"AUROC: {auroc:.4f}")
print(f"AUPRC: {auprc:.4f}")
print(f"F1: {f1:.4f}")
print(f"ACC: {acc:.4f}")

print("\n===== XGBoost 결과 =====")
print(f"* AUROC : {auroc:.4f}")
print(f"* AUPRC : {auprc:.4f}")
print(f"* F1-score : {f1:.4f}")
print(f"* Accuracy : {acc:.4f}")

print("\n===== Classification Report =====")
print(classification_report(y_test, y_pred, digits=4))

# feature importance 저장
importance_df = pd.DataFrame({
    "feature": X.columns,
    "importance": model.feature_importances_
}).sort_values("importance", ascending=False)

importance_df.to_csv("xgb_feature_importance.csv", index=False)
print("\nfeature importance 저장 완료: xgb_feature_importance.csv")
pred_df = pd.DataFrame({
    "y_true": y_test,
    "xgb_pred_proba": y_pred_proba
})
pred_df.to_csv("xgb_test_predictions.csv", index=False)
print("저장 완료: xgb_test_predictions.csv")

import joblib

joblib.dump(model, "xgb_model.pkl")
print("모델 저장 완료 😎")

print("y mean:", y.mean())
print("y unique:", np.unique(y))