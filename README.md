#  Support Integrity Auditor (SIA)

A Machine Learning-powered ticket auditing system that detects potential priority mismatches in customer support tickets.

##  Live Application

Streamlit App:

https://support-integrity-auditor-hhdhxfaad4ky67chcdoojk.streamlit.app/

##  GitHub Repository

Repository:

https://github.com/priyanka031202/Support-Integrity-Auditor

---

#  Project Overview

In large-scale customer support systems, ticket prioritization errors can lead to delayed responses, poor customer satisfaction, and operational inefficiencies.

Support Integrity Auditor (SIA) is designed to analyze support tickets and identify cases where the assigned priority may not align with the severity of the issue.

The system combines Natural Language Processing (NLP) with Machine Learning to evaluate ticket content and predict whether a priority mismatch exists.

---

# Objectives

* Detect priority inconsistencies in support tickets
* Improve customer service quality
* Reduce manual auditing effort
* Support large-scale ticket review processes
* Provide both single-ticket and batch-ticket analysis

---

#  Features

## 1. Single Ticket Analysis

Users can manually enter:

* Ticket Subject
* Ticket Description
* Issue Category
* Ticket Channel
* Resolution Time

The model instantly predicts whether:

 Priority Looks Consistent

or

 Priority Mismatch Detected

---

## 2. Batch CSV Upload

Users can upload a CSV file containing multiple tickets.

The system:

* Processes every ticket
* Generates predictions
* Displays results in a table
* Allows downloading prediction results as CSV

---

## 3. Interactive Dashboard

The dashboard provides:

* Total Tickets Processed
* Number of Mismatches Detected
* Mismatch Percentage
* Category-wise Ticket Distribution
* Prediction Distribution Charts

---

#  Machine Learning Pipeline

## Step 1 — Data Preparation

Ticket data is cleaned and preprocessed.

Operations include:

* Lowercasing
* Removing special characters
* Removing unnecessary text noise

---

## Step 2 — Feature Engineering

Text-based Features:

* TF-IDF Vectorization
* Unigram + Bigram Features

Structured Features:

* Issue Category Encoding
* Ticket Channel Encoding
* Resolution Time
* Text Length
* Word Count
* Satisfaction Score

---

## Step 3 — Feature Matrix Creation

Text features and structured features are combined into a single feature matrix.

Final Feature Shape:

20000 × 5006

---

## Step 4 — Model Training

Algorithm Used:

### XGBoost Classifier

Reasons:

* High performance on tabular data
* Handles sparse TF-IDF features effectively
* Strong classification accuracy
* Fast inference speed

---

## Step 5 — Model Serialization

The trained model is saved using Joblib.

Generated files:

* sia_xgboost_model.pkl
* tfidf_vectorizer.pkl

---

#  Project Structure

Support_Integrity_Auditor/

├── app.py

├── predict.py

├── train_pipeline.py

├── requirements.txt

├── README.md

├── models/

│ ├── sia_xgboost_model.pkl

│ └── tfidf_vectorizer.pkl

├── data/

├── outputs/

└── notebooks/

---

#  Technologies Used

## Programming Language

* Python

## Machine Learning

* Scikit-learn
* XGBoost

## NLP

* TF-IDF Vectorizer

## Data Processing

* Pandas
* NumPy

## Visualization

* Plotly
* Matplotlib
* Seaborn

## Deployment

* Streamlit
* Streamlit Cloud
* GitHub

---

#  Example Prediction

### Ticket

Subject:

Payment Charged Twice

Description:

Customer reports being charged twice for the same transaction and requests an urgent refund.

Output:

 Priority Mismatch Detected

---

# 🔧 Installation

Clone the repository:

git clone https://github.com/priyanka031202/Support-Integrity-Auditor.git

Move into project directory:

cd Support-Integrity-Auditor

Install dependencies:

pip install -r requirements.txt

Run application:

streamlit run app.py

---

#  Future Improvements

* Explainable AI (SHAP)
* Confidence Scores
* Ticket Severity Prediction
* Agent Bias Detection
* Automated Escalation Recommendations
* Real-Time Ticket Monitoring

---

# 👩 Author

Priyanka Choudhary


---


