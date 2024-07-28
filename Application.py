# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 14:32:25 2024

@author: dhana
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# Loading The Models
diabetes_model = pickle.load(open("Diabetes_model.sav", 'rb'))
loan_model = pickle.load(open("Loan_approval.sav", 'rb'))
heart_disease_model = pickle.load(open("heart_disease_model.sav", 'rb'))


# Sidebar For Streamlit
with st.sidebar:
    
    selected = option_menu('Prediction System', 
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Loan Approval Prediction'],
                           icons=['activity', 'heart', 'bank'],
                           default_index = 0)


if (selected == 'Diabetes Prediction'):
    # Page Title
    st.title("Diabetes Prediction For Woman Using ML")
    
    # Getting The Input From User
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Number Of Pregnancies")
        Glucose = st.text_input("Blood Glucose Level")
        BloodPressure = st.text_input("Blood Pressure value")
        
    with col2:
        SkinThickness = st.text_input("Skin Thickness value")
        Insulin = st.text_input("Insulin Level")
        BMI = st.text_input("Body Mass Index (BMI)")
        
    with col3:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
        Age = st.text_input("Age of the Person")
        # code for prediction
        
    diab_diagnosis = ''
    
    # Creating a Prediction button
    
    if st.button("Diabetes Test Button"):
        diagnosis = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if diagnosis[0]==1:
            diab_diagnosis = 'The Person is Diabetic'
        
        else:
            diab_diagnosis = 'The Person is Not Diabetic'
            
        st.snow()
        st.info(diab_diagnosis)


if (selected == 'Heart Disease Prediction'):
    # Page Title
    st.title("Heart Disease Prediction Using ML")
    
    # Getting The Input From User
    col1,col2,col3 = st.columns(3)
    
    
    with col1:
        Age = st.text_input("Enter The Age")
        Gender = st.text_input("Enter the Gender (Male-1 Female-0)")
        Cp = st.text_input("Enter Chest Pain value")
        TrestBps = st.text_input("'TrestBps' value")
        thal = st.text_input("'Thal' Value")
        
    with col2:
        Cholestral = st.text_input("Cholestral Value")
        fbs = st.text_input("'fbs' Value")
        RestECG = st.text_input("Rest ECG Value")
        Thalach = st.text_input("'Thalach' Value")
        
    with col3:
        Exang = st.text_input("'Exang' Value")
        Oldpeak = st.text_input("'oldpeak' Value")
        slope = st.text_input("'slope' Value")
        ca = st.text_input("'ca' Value")
    
        # code for prediction
        
    heart_disease = ''
    
    # Creating a Prediction button
    
    if st.button("Heart Disease Test Button"):
       # age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal
        diagnosis = heart_disease_model.predict([[Age, Gender, Cp, TrestBps, Cholestral, fbs, RestECG, Thalach, Exang, Oldpeak, slope, ca, thal]])
        
        if diagnosis[0]==1:
            heart_disease = 'The Person has Heart Disease'
        
        else:
            heart_disease = 'The Person Does Not Have Heart Disease'
       
        st.snow()
        st.info(heart_disease)
        
    

if (selected == 'Loan Approval Prediction'):
    # Page Title
    st.title("Loan Approval Prediction Using ML")
    

    col1,col2,col3 = st.columns(3)
    with col1:
        Gender = st.text_input("Specify The Gender (Male-1 Female-0)")
        Education = st.text_input("Education (Graduate->1 / Non-Graduate->0)")
        CoapplicantIncome = st.text_input("Enter Co-Applicants Income")
        Credit_History = st.text_input("Enter Credit History (0 or 1)")
        
    with col2:
        married = st.text_input("Is Married (0 or 1)")
        Self_Employed = st.text_input("self Employed ? (0 or 1)")
        LoanAmount = st.text_input("Enter the Loan Amount")
        Property_Area = st.text_input("{'Rural':0, 'Urban':1, 'Semiurban':2}")
        
        
    with col3:
        Dependents = st.text_input("Number of dependants")
        ApplicantIncome = st.text_input("Enter Applicants Income")
        Loan_Amount_Term = st.text_input("Loan Amount Tenure (DAYS)")
        
    # code for prediction
    
    Loan = ''
    
    # Creating a Prediction button
    
    if st.button("Loan Approval Test Button"):

        Loan_prediction = loan_model.predict([[Gender, married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]])
        
        if Loan_prediction[0]==1:
            Loan = 'Congrats, Your Loan is Approved'
        
        else:
            Loan = 'Sorry, Your Loan is Rejected'
          
        st.snow()
        st.info(Loan)
    
    
    
    
    