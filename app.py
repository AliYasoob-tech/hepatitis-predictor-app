import streamlit as st
import pandas as pd
import joblib

model = joblib.load("xgb_pipeline_model.joblib")

st.title("🧬 Hepatitis C prediction App 🧑‍🔬")
st.write("This app predicts the risk of Hepatitis C based on lab results.")

age = st.number_input("Age",18,100,step=1)
sex = st.selectbox("Sex",['m','f'])
alb = st.number_input("Albumin (ALB)", 0.0, 90.0)
alp = st.number_input("Alkaline Phosphatase (ALP)", 0.0, 500.0)
alt = st.number_input("Alanine Transaminase (ALT)", 0.0, 500.0)
ast = st.number_input("Aspartate Transaminase (AST)", 0.0, 500.0)
bil = st.number_input("Bilirubin (BIL)", 0.0, 200.0)
che = st.number_input("Cholinesterase (CHE)", 0.0, 20.0)
chol = st.number_input("Cholesterol (CHOL)", 0.0, 20.0)
crea = st.number_input("Creatinine (CREA)", 0.0, 1000.0)
ggt = st.number_input("GGT", 0.0, 700.0)
prot = st.number_input("Total Protein (PROT)", 0.0, 90.0)

# Prediction Button
if st.button("Predict"):
    # Convert input to DataFrame
    input_df = pd.DataFrame({
        'Age': [age],
        'Sex': [sex],
        'ALB': [alb],
        'ALP': [alp],
        'ALT': [alt],
        'AST': [ast],
        'BIL': [bil],
        'CHE': [che],
        'CHOL': [chol],
        'CREA': [crea],
        'GGT': [ggt],
        'PROT': [prot]
    })

        # Make prediction
    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)
    st.write("Prediction Probability (class 1):", proba[0][1])

    if proba[0][1] > 0.4:
        st.write("High Risk")
    else:
        st.write("Low Risk")
