import streamlit as st
import numpy as np
import pickle

# Load your trained model (make sure loan_model.pkl is in the same folder)
model = pickle.load(open("loan_model.pkl", "rb"))

# Streamlit App Title and Description
st.set_page_config(page_title="Loan Approval Predictor")
st.title("🏦 Loan Approval Prediction")
st.write("Enter the details below to check if the loan will be approved.")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
loan_term = st.number_input("Loan Term (in days)", value=360)
credit_history = st.selectbox("Credit History", ["Good (1.0)", "Bad (0.0)"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Data preprocessing
def preprocess_input():
    gender_val = 1 if gender == "Male" else 0
    married_val = 1 if married == "Yes" else 0
    education_val = 0 if education == "Graduate" else 1
    self_employed_val = 1 if self_employed == "Yes" else 0
    credit_val = 1.0 if credit_history == "Good (1.0)" else 0.0
    area_val = {"Urban": 2, "Semiurban": 1, "Rural": 0}[property_area]

    features = np.array([[gender_val, married_val, education_val, self_employed_val,
                          applicant_income, coapplicant_income, loan_amount,
                          loan_term, credit_val, area_val]])
    return features

# Predict and Display Result
if st.button("Predict Loan Approval"):
    input_data = preprocess_input()
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Loan Approved!")
    else:
        st.error("❌ Loan Rejected.")
