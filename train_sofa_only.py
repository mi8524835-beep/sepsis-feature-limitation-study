import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, average_precision_score, f1_score, accuracy_score
from xgboost import XGBClassifier

print("=== SOFA-only Mortality Prediction (Sepsis cohort) ===")

# 데이터 로드
df = pd.read_parquet("df_all_dashboard.parquet")

# stay_id 기준 중복 제거
df = df.drop_duplicates(subset="stay_id").copy()

print("before sepsis filter:", df.shape)

# sepsis 환자만 선택
df = df[df["sepsis3"].astype(int) == 1].copy()

print("after sepsis filter:", df.shape)
print("sepsis ratio:", df["sepsis3"].astype(int).mean())

# feature 선택
features = [
    "respiration",
    "coagulation",
    "liver",
    "cardiovascular",
    "cns",
    "renal",
    "sofa_score"
]

# X, y
X = df[features]
y = df["hospital_expire_flag"].astype(int)

print("X shape:", X.shape)
print("y mean:", y.mean())
print("y unique:", np.unique(y))

# split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

# 모델
model = XGBClassifier(
    n_estimators=200,
    max_depth=4,
    learning_rate=0.05,
    n_jobs=1,
    tree_method="hist",
    random_state=42
)

print("학습 중...")
model.fit(X_train, y_train)

# 예측
y_pred_proba = model.predict_proba(X_test)[:, 1]
y_pred = (y_pred_proba >= 0.5).astype(int)

# 평가
auroc = roc_auc_score(y_test, y_pred_proba)
auprc = average_precision_score(y_test, y_pred_proba)
f1 = f1_score(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)

print("\n===== SOFA-only 결과 =====")
print(f"AUROC: {auroc:.4f}")
print(f"AUPRC: {auprc:.4f}")
print(f"F1: {f1:.4f}")
print(f"ACC: {acc:.4f}")