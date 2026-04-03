import pandas as pd
import numpy as np

# 기존 패혈증 라벨 파일
labels = pd.read_csv("labels.csv")   # stay_id, sepsis3

# 사망 여부가 있는 파일
df = pd.read_parquet("df_all_dashboard.parquet")

# stay_id 기준으로 사망률 라벨만 추출
mort = df[["stay_id", "hospital_expire_flag"]].copy()

# 혹시 stay_id가 중복이면 하나만 남기기
mort = mort.drop_duplicates(subset="stay_id")

# 컬럼명 통일
mort["mortality"] = mort["hospital_expire_flag"].astype(int)

# 기존 labels와 합치기
labels_mort = labels.merge(
    mort[["stay_id", "mortality"]],
    on="stay_id",
    how="left"
)

# 결측 처리
labels_mort["mortality"] = labels_mort["mortality"].fillna(0).astype(int)

# 저장
np.save("y_mortality.npy", labels_mort["mortality"].values)

print(labels_mort.head())
print("mortality mean:", labels_mort["mortality"].mean())
print("saved: y_mortality.npy")