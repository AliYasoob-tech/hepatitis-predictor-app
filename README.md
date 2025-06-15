# 🧬 Hepatitis C Predictor App

This is a machine learning-powered web application that predicts the **risk of Hepatitis C** using patient lab test results. The model was trained on medical data and deployed using **Streamlit** for an easy-to-use interface.

## 🔍 Project Overview

- ✅ Binary Classification Task: Predict **Low Risk (0)** or **High Risk (1)**
- ⚙️ Models Used:
  - Logistic Regression
  - **XGBoost (Final Model)** – chosen for its high **recall** and overall performance
- 📊 Performance:
  - ROC AUC Score: **0.98**
  - Accuracy: 96%
  - Priority: High recall to reduce false negatives

## 🚀 Live App

👉 https://hepatitis-predictor-app-4e4if2rzvf9lkuewocytiy.streamlit.app/

## 🧠 Model Pipeline

The final model is wrapped in a **scikit-learn pipeline** that:
- Imputes missing values
- Applies log transformation to skewed features
- Scales numerical features
- Encodes categorical variables
- Feeds the processed input to an XGBoost classifier

## 📦 Tech Stack

| Tool        | Purpose                      |
|-------------|------------------------------|
| Python      | Programming Language         |
| pandas, numpy | Data Handling              |
| scikit-learn | Preprocessing & Pipeline    |
| XGBoost     | Model Training               |
| Streamlit   | App Deployment               |

## 📁 Project Structure
hepatitis-predictor-app/
├── app.py # Streamlit app
├── model.pkl # Trained ML pipeline
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## ⚙️ Setup Locally (Optional)

Clone and run locally:

```bash
git clone https://github.com/AliYasoob-tech/hepatitis-predictor-app.git
cd hepatitis-predictor-app
pip install -r requirements.txt
streamlit run app.py

```

## 📌 Note
This app is built for educational purposes only. It is not intended for real medical diagnosis or treatment decisions.

