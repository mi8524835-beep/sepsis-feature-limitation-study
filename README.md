# Sepsis vs Mortality Prediction: Feature Limitation Study

## Overview
This project compares predictive performance across different clinical prediction tasks using the same SOFA-based organ dysfunction features.

## Problem
Can the same organ dysfunction features effectively predict both sepsis and mortality?

## Features
- respiration
- coagulation
- liver
- cardiovascular
- cns
- renal
- sofa_24hours

## Tasks

1. Sepsis prediction
2. Mortality prediction

## Results
| Task | ROC-AUC |
|------|--------|
| Sepsis prediction | 0.807 |
| Mortality prediction | 0.465 |

## Key Insight
The same feature set performed well for sepsis prediction but poorly for mortality prediction.  
This suggests that static early organ dysfunction is useful for identifying sepsis, but insufficient for predicting patient outcomes without temporal progression and additional patient-level information.

## Additional Experiments
- Reduced 3-organ model: ROC-AUC 0.765
- Direct criteria-based model: ROC-AUC 0.740

## Takeaway
Feature usefulness depends on the prediction target.  
Strong features for diagnosis are not always strong features for prognosis.
