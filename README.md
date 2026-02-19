# **💳 Credit Card Fraud Detection System**
---
## **📌 Project Overview**

The Credit Card Fraud Detection System aims to identify fraudulent credit card transactions and distinguish them from legitimate ones. With the rapid increase in online payments, detecting fraud accurately is critical to reduce financial losses and ensure secure transactions.

This project analyzes historical transaction data and predicts whether a transaction is fraudulent or legitimate using machine learning techniques. The trained model is deployed using a Streamlit web application for real-time prediction. 

---

## **🎯 Objectives**

- Detect fraudulent credit card transactions accurately

- Analyze transaction behavior using historical data

Provide real-time fraud prediction through a user-friendly interface

---

## **📂 Dataset**

The dataset contains historical credit card transaction records with attributes such as:

- Transaction amount

- Merchant and category

- Transaction date and time

- Customer and merchant locations

- Customer demographic details

- Fraud label (is_fraud)

---

## **🛠️ Technologies Used**

- Programming Language: Python

- Machine Learning: LightGBM

- Data Processing: Pandas, NumPy

- Model Saving: Joblib

- Geographical Distance: Geopy

- Web Framework: Streamlit
  
---

## **⚙️ System Approach**

- Collect historical credit card transaction data

- Clean and preprocess the data

- Perform feature engineering (time features, distance calculation)

- Encode categorical attributes

- Train a machine learning classification model

- Evaluate the model using appropriate metrics

- Deploy the trained model using Streamlit

---

## **🧠 Machine Learning Algorithm**

Algorithm Used: Light Gradient Boosting Machine (LightGBM)

Problem Type: Binary Classification

- 0 → Legitimate Transaction

- 1 → Fraudulent Transaction

LightGBM is chosen for its efficiency, accuracy, and ability to handle large and imbalanced datasets.

---

## **📊 Model Evaluation**

The model performance is evaluated using:

- Precision

- Recall

- F1-score

- Confusion Matrix

Recall is given higher priority, as missing fraudulent transactions can lead to significant financial loss.

---

## **🖥️ Web Application**

A Streamlit-based web application allows users to:

- Enter transaction details

- Automatically preprocess inputs

- Predict whether a transaction is fraudulent or legitimate

- View results instantly
