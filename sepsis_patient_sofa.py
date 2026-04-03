import pandas as pd

print("=== SOFA score별 사망률 ===")

# 데이터 로드
df = pd.read_parquet("df_all_dashboard.parquet")

# 중복 제거
df = df.drop_duplicates(subset="stay_id").copy()

# sepsis 환자만
df = df[df["sepsis3"].astype(int) == 1].copy()

# SOFA 점수 정수화 (혹시 float일 경우)
df["sofa_score"] = df["sofa_score"].astype(int)

# SOFA score별 사망률 계산
result = df.groupby("sofa_score")["hospital_expire_flag"].agg(
    total="count",
    deaths="sum",
    mortality_rate="mean"
).reset_index()

# 퍼센트 변환
result["mortality_%"] = result["mortality_rate"] * 100

print(result.sort_values("sofa_score"))