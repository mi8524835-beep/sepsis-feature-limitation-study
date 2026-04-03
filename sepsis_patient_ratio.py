import pandas as pd

df = pd.read_parquet("df_all_dashboard.parquet")

# stay_id 기준 중복 제거
df = df.drop_duplicates(subset="stay_id").copy()

# sepsis 환자만
sepsis_df = df[df["sepsis3"].astype(int) == 1].copy()

mortality_rate = sepsis_df["hospital_expire_flag"].mean()

print("Sepsis 환자 수:", len(sepsis_df))
print("사망 환자 수:", int(sepsis_df["hospital_expire_flag"].sum()))
print(f"사망률 (%): {mortality_rate * 100:.2f}%")