import streamlit as st
import plotly.express as px
import pandas as pd
from predict import predict_ticket

st.set_page_config(
    page_title="Support Integrity Auditor",
    layout="wide"
)

# =========================
# Sidebar
# =========================

st.sidebar.title("🛡️ SIA")
st.sidebar.subheader("Navigation")

page = st.sidebar.radio(
    "",
    [
        "Single Ticket Analysis",
        "Batch CSV Upload",
        "Dashboard"
    ]
)

# =========================
# Single Ticket Analysis
# =========================

if page == "Single Ticket Analysis":

    st.title("🛡️ Support Integrity Auditor")

    st.write(
        "Detect priority mismatches between ticket severity and assigned priority."
    )

    st.header("Analyze Single Ticket")

    subject = st.text_input(
        "Ticket Subject"
    )

    description = st.text_area(
        "Ticket Description"
    )

    category = st.selectbox(
        "Issue Category",
        [
            "Technical",
            "Billing",
            "Account",
            "General Inquiry",
            "Fraud"
        ]
    )

    channel = st.selectbox(
        "Ticket Channel",
        [
            "Email",
            "Chat",
            "Web Form"
        ]
    )

    resolution_time = st.number_input(
        "Resolution Time (Hours)",
        min_value=1,
        value=24
    )

    if st.button("Analyze Ticket"):

        prediction = predict_ticket(
            subject,
            description,
            category,
            channel,
            resolution_time
        )

        if "Mismatch" in prediction:
            st.error(prediction)
        else:
            st.success(prediction)

# =========================
# Batch CSV Upload
# =========================

elif page == "Batch CSV Upload":

    st.title("📂 Batch Ticket Analysis")

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.subheader("Uploaded Data")

        st.dataframe(df.head())

        required_columns = [
            "Ticket_Subject",
            "Ticket_Description",
            "Issue_Category",
            "Ticket_Channel",
            "Resolution_Time_Hours"
        ]

        missing_cols = [
            col for col in required_columns
            if col not in df.columns
        ]

        if len(missing_cols) > 0:

            st.error(
                f"Missing columns: {missing_cols}"
            )

        else:

            predictions = []

            for _, row in df.iterrows():

                result = predict_ticket(
                    row["Ticket_Subject"],
                    row["Ticket_Description"],
                    row["Issue_Category"],
                    row["Ticket_Channel"],
                    row["Resolution_Time_Hours"]
                )

                predictions.append(result)

            df["Prediction"] = predictions

            st.subheader("Prediction Results")

            st.dataframe(df)

            csv = df.to_csv(index=False)

            st.download_button(
                label="⬇ Download Results CSV",
                data=csv,
                file_name="ticket_predictions.csv",
                mime="text/csv"
            )

# =========================
# Dashboard Placeholder
# =========================

elif page == "Dashboard":

    st.title("📊 Dashboard & Analytics")

    st.write(
        "Upload a CSV file to generate analytics and insights."
    )

    dashboard_file = st.file_uploader(
        "Upload CSV for Dashboard",
        type=["csv"],
        key="dashboard_file"
    )

    if dashboard_file is not None:

        df = pd.read_csv(dashboard_file)

        required_columns = [
            "Ticket_Subject",
            "Ticket_Description",
            "Issue_Category",
            "Ticket_Channel",
            "Resolution_Time_Hours"
        ]

        missing_cols = [
            col for col in required_columns
            if col not in df.columns
        ]

        if len(missing_cols) > 0:

            st.error(
                f"Missing columns: {missing_cols}"
            )

        else:

            predictions = []

            for _, row in df.iterrows():

                result = predict_ticket(
                    row["Ticket_Subject"],
                    row["Ticket_Description"],
                    row["Issue_Category"],
                    row["Ticket_Channel"],
                    row["Resolution_Time_Hours"]
                )

                predictions.append(result)

            df["Prediction"] = predictions

            total_tickets = len(df)

            mismatches = (
                df["Prediction"]
                .str.contains("Mismatch")
                .sum()
            )

            consistent = (
                total_tickets - mismatches
            )

            mismatch_rate = (
                mismatches / total_tickets
            ) * 100

            st.subheader("Key Metrics")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Total Tickets",
                total_tickets
            )

            col2.metric(
                "Mismatches",
                mismatches
            )

            col3.metric(
                "Consistent",
                consistent
            )

            col4.metric(
                "Mismatch %",
                f"{mismatch_rate:.2f}%"
            )

            st.markdown("---")

            st.subheader(
                "Prediction Distribution"
            )

            pie_data = pd.DataFrame(
                {
                    "Category": [
                        "Mismatch",
                        "Consistent"
                    ],
                    "Count": [
                        mismatches,
                        consistent
                    ]
                }
            )

            fig1 = px.pie(
                pie_data,
                names="Category",
                values="Count",
                title="Mismatch Distribution"
            )

            st.plotly_chart(
                fig1,
                use_container_width=True
            )

            st.markdown("---")

            st.subheader(
                "Tickets by Issue Category"
            )

            category_counts = (
                df["Issue_Category"]
                .value_counts()
                .reset_index()
            )

            category_counts.columns = [
                "Category",
                "Count"
            ]

            fig2 = px.bar(
                category_counts,
                x="Category",
                y="Count",
                title="Tickets by Category"
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )

            st.markdown("---")

            st.subheader(
                "Prediction Results"
            )

            st.dataframe(df)