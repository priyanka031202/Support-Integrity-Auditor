import joblib
import pandas as pd
from scipy.sparse import hstack

# Load model
model = joblib.load("models/sia_xgboost_model.pkl")

# Load vectorizer
tfidf = joblib.load("models/tfidf_vectorizer.pkl")


def predict_ticket(
    subject,
    description,
    category,
    channel,
    resolution_time
):

    # Combine text
    text = str(subject) + " " + str(description)

    # TF-IDF features
    text_features = tfidf.transform([text])

    # Manual encoding
    category_map = {
        "Technical": 0,
        "Billing": 1,
        "Account": 2,
        "General Inquiry": 3,
        "Fraud": 4
    }

    channel_map = {
        "Email": 0,
        "Chat": 1,
        "Web Form": 2
    }

    issue_encoded = category_map.get(category, 0)
    channel_encoded = channel_map.get(channel, 0)

    # Derived features
    satisfaction_score = 3

    text_length = len(text)

    word_count = len(text.split())

    structured = pd.DataFrame(
        [[
            issue_encoded,
            channel_encoded,
            resolution_time,
            satisfaction_score,
            text_length,
            word_count
        ]]
    )

    # Combine exactly like training
    final_features = hstack(
        [
            text_features,
            structured.values
        ]
    )

    prediction = model.predict(final_features)[0]

    if prediction == 1:
        return "🚨 Priority Mismatch Detected"
    else:
        return "✅ Priority Looks Consistent"