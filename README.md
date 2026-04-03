# 🧠 Sepsis vs Mortality Prediction: Feature Limitation Study

## 📌 Overview

This project investigates how the same clinical features behave differently across prediction tasks and patient cohorts.

We compare:

* Sepsis prediction (diagnosis)
* Mortality prediction (prognosis)

---

## ❓ Problem Statement

Can the same organ dysfunction features effectively predict both sepsis and mortality?

---

## 📊 Features

### SOFA-based features

* respiration
* coagulation
* liver
* cardiovascular
* cns
* renal
* sofa_score

### Additional clinical features

* resp_worsening
* coag_worsening
* liver_worsening
* cardio_worsening
* cns_worsening
* renal_worsening
* organ_count

---

## ⚙️ Experimental Setup

### Model

* XGBoost

### Tasks

* Sepsis prediction
* Mortality prediction

### Cohorts

* Full cohort
* Sepsis cohort

---

## 📈 Results

| Task      | Feature    | Cohort | AUROC      |
| --------- | ---------- | ------ | ---------- |
| Sepsis    | SOFA-based | Full   | **0.852**  |
| Mortality | Full       | Full   | **0.8867** |
| Mortality | SOFA-only  | Sepsis | **0.6450** |
| Mortality | Full       | Sepsis | **0.6442** |

---

## 📊 Sepsis Cohort Statistics

* Total patients: 41,296
* Deaths: 5,215
* Mortality rate: **12.63%**

👉 Highly imbalanced dataset
👉 Accuracy (~87%) is not a reliable metric

---

## 📉 Mortality by SOFA Score

| SOFA | Mortality (%) |
| ---- | ------------- |
| 2    | 9.13%         |
| 4    | 13.69%        |
| 6    | 17.88%        |
| 8    | 21.91%        |
| 10   | 29.27%        |
| 12   | 35.38%        |
| 14   | 45.00%        |

👉 Mortality increases as SOFA score increases
👉 Sharp increase observed at SOFA ≥ 10

---

## 🔍 Key Insights

### 1. Feature Limitation

SOFA-based features work well for sepsis prediction but are insufficient for mortality prediction.

---

### 2. Cohort Effect

Restricting the dataset to sepsis patients significantly reduces mortality prediction performance.

---

### 3. Class Imbalance

Low mortality rate (~12.6%) leads to misleadingly high accuracy.

---

### 4. Critical Insight

SOFA score shows strong correlation with mortality
but does not translate into strong predictive performance.

---

## 🧠 Why This Happens

* SOFA captures **current severity (static)**
* Mortality depends on **temporal progression (dynamic)**

👉 Diagnosis ≠ Prognosis

---

## 🧾 Conclusion

Model performance depends not only on feature selection
but also on prediction task and cohort definition.

---

## 💡 Takeaway

* Feature usefulness is task-dependent
* Model performance is cohort-dependent
* Static features are insufficient for prognosis

---

## 📁 Project Structure

```bash
├── train_xgb.py
├── train_sofa_only.py
├── train_mortality_in_sepsis.py
├── make_mortality_label.py
├── sepsis_patient_ratio.py
├── results_summary.txt
└── README.md
```

---

## 🚀 How to Run

```bash
python3 make_mortality_label.py
python3 train_xgb.py
python3 train_sofa_only.py
python3 train_mortality_in_sepsis.py
python3 sepsis_patient_ratio.py
```

---

## 🎯 Key Message

> The same features can behave very differently
> depending on the prediction task and cohort.

---
