# 🧠 Sepsis vs Mortality Prediction: Feature Limitation Study

## 📌 Overview

This project investigates whether the same clinical features can be effectively used for both diagnosis and prognosis tasks in healthcare.

Using SOFA-based organ dysfunction features, we compare model performance between:

* Sepsis prediction (diagnosis)
* Mortality prediction (prognosis)

---

## ❓ Problem Statement

Can the same organ dysfunction features effectively predict both sepsis and mortality?

---

## 📊 Features

The following SOFA-based clinical features were used:

* respiration
* coagulation
* liver
* cardiovascular
* cns
* renal
* sofa_score

---

## ⚙️ Experimental Setup

### Model

* XGBoost

### Tasks

1. Sepsis prediction
2. Mortality prediction

### Experiments

| Experiment | Feature Set                     |
| ---------- | ------------------------------- |
| Full Model | All available features          |
| SOFA Model | Organ dysfunction features only |

---

## 📈 Results

### 🔹 Sepsis Prediction

* AUROC: **0.852**

→ High performance using SOFA-based features

---

### 🔹 Mortality Prediction (Full Feature)

* AUROC: **0.8867**

→ Strong predictive performance with full feature set

---

### 🔹 Mortality Prediction (SOFA-only)

* AUROC: **~0.64**

→ Significant performance drop when features are limited

---

## 🔍 Key Insight

> The same feature set performs well for diagnosis but poorly for prognosis.

* Sepsis prediction depends on **current patient state**
* Mortality prediction requires **temporal progression and richer patient context**

---

## 🧠 Conclusion

This study demonstrates that feature effectiveness is highly dependent on the prediction task.

* Diagnostic tasks can rely on static physiological indicators
* Prognostic tasks require more comprehensive and temporal data

---

## 💡 Takeaway

> Strong features for diagnosis are not always strong features for prognosis.

---

## 📁 Project Structure

```
├── train_xgb.py              # Full feature mortality / sepsis model
├── train_sofa_only.py        # SOFA-only mortality model
├── make_mortality_label.py   # Mortality label generation
├── results_summary.txt       # Summary of results
└── README.md
```

---

## 🚀 How to Run

```bash
# 1. Create mortality label
python3 make_mortality_label.py

# 2. Train full feature model
python3 train_xgb.py

# 3. Train SOFA-only model
python3 train_sofa_only.py
```

