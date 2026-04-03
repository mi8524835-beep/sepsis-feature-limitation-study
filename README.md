# 🧠 Sepsis vs Mortality Prediction: Feature Limitation Study

## 1. Overview

본 프로젝트는 동일한 임상 feature(SOFA 기반 장기 기능 지표)를 사용하여
패혈증 진단과 사망률 예측 간 성능 차이를 비교하고,
feature와 cohort가 예측 성능에 미치는 영향을 분석하는 것을 목표로 한다.

---

## 2. Problem Definition

동일한 organ dysfunction feature가
패혈증 진단과 사망률 예측 모두에 효과적인가?

---

## 3. Data & Features

### 🔹 Dataset

* ICU 환자 데이터 (stay_id 기준)
* 중복 제거 후 환자 단위 분석

---

### 🔹 Feature 구성

#### ✔ SOFA-based features

* respiration
* coagulation
* liver
* cardiovascular
* cns
* renal
* sofa_score

#### ✔ Additional clinical features

* resp_worsening
* coag_worsening
* liver_worsening
* cardio_worsening
* cns_worsening
* renal_worsening
* organ_count

---

## 4. Experimental Design

### 🔹 Model

* XGBoost

---

### 🔹 Tasks

1. Sepsis prediction
2. Mortality prediction

---

### 🔹 Cohort

* 전체 환자 (Full cohort)
* 패혈증 환자 (Sepsis cohort)

---

## 5. Results

### 🔹 Sepsis Prediction (Full cohort)

* AUROC: **0.852**

👉 organ dysfunction feature만으로도 높은 성능

---

### 🔹 Mortality Prediction (Full feature, Full cohort)

* AUROC: **0.8867**

👉 다양한 feature 사용 시 높은 예측 성능

---

### 🔹 Mortality Prediction (SOFA-only, Sepsis cohort)

* AUROC: **~0.64**

👉 feature 제한 시 성능 감소

---

### 🔹 Mortality Prediction (Full feature, Sepsis cohort)

* AUROC: **0.6442**

👉 동일 feature라도 cohort 제한 시 성능 감소

---

## 6. Key Findings

### 🔥 핵심 1: Feature 영향

> 동일한 SOFA feature는 패혈증 예측에는 효과적이지만,
> 사망률 예측에는 충분하지 않다.

---

### 🔥 핵심 2: Cohort 영향

> 동일한 feature라도 환자 cohort를 제한하면 예측 성능이 감소한다.

---

## 7. Insight

* Diagnosis (패혈증)
  → 현재 상태 기반 → static feature로 충분

* Prognosis (사망률)
  → 시간 흐름 + 환자 상태 변화 필요
  → feature 및 cohort에 민감

---

## 8. Conclusion

본 실험을 통해 동일한 feature라도
예측 대상(task)과 데이터 구성(cohort)에 따라 성능이 크게 달라질 수 있음을 확인하였다.

---

## 9. Takeaway

👉 Feature usefulness is task-dependent
👉 Model performance is cohort-dependent
👉 Diagnosis ≠ Prognosis
