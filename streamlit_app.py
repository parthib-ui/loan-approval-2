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

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Loan Approval Predictor</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f7f8;
            padding: 20px;
        }

        h2 {
            text-align: center;
        }

        form {
            max-width: 500px;
            margin: auto;
            background: #fff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }

        label {
            display: block;
            margin: 15px 0 5px;
        }

        input, select {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
        }

        button {
            background-color: #007BFF;
            color: white;
            padding: 12px;
            border: none;
            width: 100%;
            border-radius: 5px;
            font-size: 16px;
        }

        .result {
            text-align: center;
            font-size: 18px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h2>Loan Approval Prediction</h2>
    <form action="/predict" method="POST">
        <label>Gender:</label>
        <select name="gender">
            <option value="1">Male</option>
            <option value="0">Female</option>
        </select>

        <label>Married:</label>
        <select name="married">
            <option value="1">Yes</option>
            <option value="0">No</option>
        </select>

        <label>Education:</label>
        <select name="education">
            <option value="0">Graduate</option>
            <option value="1">Not Graduate</option>
        </select>

        <label>Self Employed:</label>
        <select name="self_employed">
            <option value="1">Yes</option>
            <option value="0">No</option>
        </select>

        <label>Applicant Income:</label>
        <input type="number" name="applicant_income" required>

        <label>Coapplicant Income:</label>
        <input type="number" name="coapplicant_income" required>

        <label>Loan Amount (in thousands):</label>
        <input type="number" name="loan_amount" required>

        <label>Loan Term (in days):</label>
        <input type="number" name="loan_term" value="360" required>

        <label>Credit History:</label>
        <select name="credit_history">
            <option value="1.0">Good</option>
            <option value="0.0">Bad</option>
        </select>

        <label>Property Area:</label>
        <select name="property_area">
            <option value="2">Urban</option>
            <option value="1">Semiurban</option>
            <option value="0">Rural</option>
        </select>

        <button type="submit">Predict</button>
    </form>
</body>
</html>

from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open("loan_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = [
        int(request.form['gender']),
        int(request.form['married']),
        int(request.form['education']),
        int(request.form['self_employed']),
        float(request.form['applicant_income']),
        float(request.form['coapplicant_income']),
        float(request.form['loan_amount']),
        float(request.form['loan_term']),
        float(request.form['credit_history']),
        int(request.form['property_area'])
    ]
    final_input = np.array([data])
    prediction = model.predict(final_input)[0]
    result = "Loan Approved ✅" if prediction == 1 else "Loan Rejected ❌"
    return f"<h2 class='result' style='text-align:center'>{result}</h2>"

if __name__ == "__main__":
    app.run(debug=True)


