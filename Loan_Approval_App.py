# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 20:15:56 2025

@author: HP
"""
import numpy as np
import pickle
import streamlit as st
import os

model_path = os.path.join(os.path.dirname(__file__),"loan_approval.sav")
try:
    loan = pickle.load(open(model_path,"rb"))
except FileNotFoundError:
    st.error("Model file not found")
    st.stop()
    
def Loan_prediction(input_data):
    input_data_as_np_array = np.asarray(input_data).reshape(1,-1)
    prediction = loan.predict(input_data_as_np_array)
    prediction
    if prediction[0] == 1:
        return "Loan Approved"
    else:
        return "Loan Not Approved"
def main():
    st.title("Loan Approval Prediction App")
    
    Gender = st.selectbox("Gender",["Male","Female"])
    Married = st.selectbox("Married",["Yes","No"])
    Dependents = st.selectbox("Dependents",["0","1","2","3+"])
    Education = st.selectbox("Education",["Graduate","Not Graduate"])
    Self_Employed = st.selectbox("Self_Employed",["Yes","No"])
    ApplicantIncome = st.number_input("Applicant Income")
    CoapplicantIncome = st.number_input("Coapplicant Income")
    LoanAmount = st.number_input("Loan Amount")
    Loan_Amount_Term = st.number_input("Loan Amount Term")
    Credit_History = st.selectbox("Credit History",[1.0,0.0])
    Property_Area = st.selectbox("Property_Area",["Urban","Rural","Semiurban"])


    Gender = 1 if Gender =="Male" else 0
    Married = 1 if Married == "Yes" else 0
    Education = 1 if Education == "Graduate" else 0
    Self_Employed = 1 if Self_Employed == "Yes" else 0
    
    if Dependents == "3+":
        Dependents = 3
    else:
        Dependents = int(Dependents)
        
    Property_Area_Rural = 1 if Property_Area == "Rural" else 0
    Property_Area_Urban = 1 if Property_Area == "Urban" else 0
    
    loan_data = ""
    if st.button("Predict"):
        loan_data = Loan_prediction([Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area_Rural,Property_Area_Urban])
    st.success(loan_data)

if __name__ == "__main__":
     main()        
        