# 🧠 Sepsis vs Mortality Prediction: Feature Limitation Study

## 📌 Overview

This project explores how the same clinical features perform differently across prediction tasks and patient cohorts.

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

| Task      | Feature | Cohort | AUROC  |
| --------- | ------- | ------ | ------ |
| Sepsis    | SOFA    | Full   | 0.852  |
| Mortality | Full    | Full   | 0.8867 |
| Mortality | SOFA    | Sepsis | ~0.64  |
| Mortality | Full    | Sepsis | 0.6442 |

---

## 🔍 Key Insights

### 1. Feature Dependency

SOFA-based features perform well for sepsis prediction but are insufficient for mortality prediction.

---

### 2. Cohort Dependency

Restricting the cohort to sepsis patients significantly reduces mortality prediction performance.

---

## 🧠 Conclusion

Model performance depends not only on feature selection but also on the prediction task and cohort definition.

---

## 💡 Takeaway

> Feature usefulness depends on the prediction target
> Model performance depends on cohort selection

---

## 📁 Project Structure

```
├── train_xgb.py
├── train_sofa_only.py
├── train_mortality_in_sepsis.py
├── make_mortality_label.py
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
```

