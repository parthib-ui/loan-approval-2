import streamlit as st

st.title("✅ Loan Approval Predictor")
st.write("This is a working Streamlit app.")

import streamlit as st
import pickle

st.title("🏦 Loan Approval Predictor")

try:
    model = pickle.load(open('loan_model.pkl', 'rb'))
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"❌ Model loading failed: {e}")

if st.button("Test Predict"):
    st.write("Prediction placeholder here.")
