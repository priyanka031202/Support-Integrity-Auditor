# Support Integrity Auditor (SIA)

## Overview

Support Integrity Auditor (SIA) is a machine learning based ticket auditing system designed to detect priority mismatches in customer support tickets.

The application analyzes ticket information and predicts whether the assigned priority is consistent with the ticket severity.

## Features

* Single Ticket Analysis
* Batch CSV Upload Analysis
* Priority Mismatch Detection
* XGBoost Machine Learning Model
* Interactive Dashboard
* Download Prediction Results
* Streamlit Web Application

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Streamlit
* Plotly
* Joblib

## Project Structure

Support_Integrity_Auditor/

* app.py
* predict.py
* train_pipeline.py
* requirements.txt
* README.md

models/

* sia_xgboost_model.pkl
* tfidf_vectorizer.pkl

data/
outputs/
notebooks/

## Model Performance

* Algorithm: XGBoost Classifier
* Accuracy: 72.62%
* Dataset Size: 20,000 Support Tickets

## How To Run

1. Clone the repository

2. Install dependencies

pip install -r requirements.txt

3. Launch the application

streamlit run app.py

## Author

Priyanka Choudhary
