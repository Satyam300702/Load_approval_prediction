Project Overview

This project predicts whether a loan application will be approved or rejected based on applicant information such as income, credit history, loan amount, and property area.

A stacking ensemble model was implemented combining CatBoost, XGBoost, LightGBM, and Decision Tree classifiers, with Random Forest as the meta-model. The approach balances accuracy and generalization for imbalanced datasets.
--------------------------------------------------------------------------------------------------------------------------------------------------
Dataset

Source: Loan Prediction Dataset

Number of rows: 614

Number of columns: 13 (after dropping Loan_ID)

Key features:

Gender, Married, Dependents, Education, Self_Employed

ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History

Property_Area

Target: Loan_Status (0 = Rejected, 1 = Approved)
---------------------------------------------------------------------------------------------------------------------------------------------------
Data Preprocessing

Handled missing values:

Categorical: filled with mode

Numerical: filled with median

Encoded categorical features using LabelEncoder and One-Hot Encoding

Converted Dependents values 3+ → 3

Scaled numerical features using StandardScaler

Addressed class imbalance using SMOTE
---------------------------------------------------------------------------------------------------------------------------------------------------
Models Used

Decision Tree (tuned with RandomizedSearchCV)

Random Forest

XGBoost

LightGBM

CatBoost

KNN (tested, not included in final stacking)

Stacking Ensemble:

Base models: CatBoost, XGBoost, LightGBM, Decision Tree

Meta-model: Random Forest
------------------------------------------------------------------------------------------------------------------------------------------------
Model Evaluation
Test Set Performance
Metric	Score
Accuracy	0.83
ROC-AUC	0.79
F1-Score	0.88 (for approved loans)
----------------------------------------------------------------------------------------------------------------------------------------------------

