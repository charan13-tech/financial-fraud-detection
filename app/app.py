import streamlit as st
import pandas as pd
import joblib

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="💳",
    layout="wide"
)

# ---------------------------
# Load Model
# ---------------------------
@st.cache_resource
def load_model():
    return joblib.load("models/best_xgb_pipeline.pkl")

pipeline = load_model()
st.title("💳 Financial Fraud Detection")

st.markdown("""
Predict whether a transaction is **Fraudulent** or **Legitimate**
using an XGBoost Machine Learning model.
""")
@st.cache_data
def load_data():
    return pd.read_csv("data/AIML Dataset.csv")

df = load_data()
X = df.drop(columns=["isFraud"])
st.sidebar.header("Transaction Details")
transaction_type = st.sidebar.selectbox(
    "Transaction Type",
    sorted(df["type"].unique())
)

amount = st.sidebar.number_input(
    "Transaction Amount",
    min_value=0.0,
    value=1000.0,
    step=100.0
)

oldbalanceOrg = st.sidebar.number_input(
    "Old Balance (Origin)",
    min_value=0.0,
    value=0.0
)

newbalanceOrig = st.sidebar.number_input(
    "New Balance (Origin)",
    min_value=0.0,
    value=0.0
)

oldbalanceDest = st.sidebar.number_input(
    "Old Balance (Destination)",
    min_value=0.0,
    value=0.0
)

newbalanceDest = st.sidebar.number_input(
    "New Balance (Destination)",
    min_value=0.0,
    value=0.0
)
input_df = pd.DataFrame({
    "type": [transaction_type],
    "amount": [amount],
    "oldbalanceOrg": [oldbalanceOrg],
    "newbalanceOrig": [newbalanceOrig],
    "oldbalanceDest": [oldbalanceDest],
    "newbalanceDest": [newbalanceDest]
})
if st.button("🔍 Predict Fraud", type="primary"):

    prediction = pipeline.predict(input_df)[0]
    probability = pipeline.predict_proba(input_df)[0][1]

    st.subheader("Prediction Result")
    if prediction == 1:
        st.error("🚨 Fraudulent Transaction")
    else:
        st.success("✅ Legitimate Transaction")
    st.metric(
    label="Fraud Probability",
    value=f"{probability:.2%}"
    )
    if probability >= 0.90:
        st.error("🔴 High Risk")
    elif probability >= 0.60:
        st.warning("🟡 Medium Risk")
    else:
        st.success("🟢 Low Risk")




    