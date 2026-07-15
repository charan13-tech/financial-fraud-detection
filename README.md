# 💳 Financial Fraud Detection using Machine Learning

An end-to-end Machine Learning project that detects fraudulent financial transactions using supervised learning techniques. The project includes data preprocessing, feature engineering, model training, hyperparameter optimization, explainable AI (SHAP), and deployment through an interactive Streamlit web application.

---

## 🚀 Project Overview

Financial fraud is a significant challenge for digital payment systems. This project builds an intelligent fraud detection system capable of classifying financial transactions as **Fraudulent** or **Legitimate**.

The project follows a complete machine learning workflow from raw data to deployment, emphasizing both predictive performance and model interpretability.

---

## ✨ Features

- 📊 Exploratory Data Analysis (EDA)
- 🧹 Data Cleaning & Preprocessing
- ⚙️ Feature Engineering
- 🔄 Scikit-Learn Pipeline
- 📈 Logistic Regression Baseline
- 🚀 XGBoost Classifier
- 🎯 Hyperparameter Tuning using RandomizedSearchCV
- 📉 Model Evaluation & Comparison
- 🔍 SHAP Explainability
- 🌐 Interactive Streamlit Web Application
- 💾 Model Serialization using Joblib

---

# 📊 Dataset

| Property | Value |
|----------|-------|
| Domain | Financial Fraud Detection |
| Problem Type | Binary Classification |
| Transactions | 6,362,620 |
| Features | 11 |
| Target | isFraud |

> **Note:** The dataset is not included in this repository because of its large size.

---

# 🛠️ Tech Stack

### Programming

- Python

### Libraries

- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- XGBoost
- SHAP
- Joblib
- Streamlit

---

# ⚙️ Machine Learning Pipeline

```text
Raw Dataset
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Train-Test Split
      │
      ▼
Preprocessing Pipeline
(StandardScaler + OneHotEncoder)
      │
      ▼
Logistic Regression
      │
      ▼
XGBoost
      │
      ▼
Hyperparameter Tuning
(RandomizedSearchCV)
      │
      ▼
Model Evaluation
      │
      ▼
SHAP Explainability
      │
      ▼
Model Serialization
(Joblib)
      │
      ▼
Streamlit Deployment
```

---

# 📈 Model Performance

| Metric | Logistic Regression | XGBoost |
|---------|--------------------:|---------:|
| Accuracy | 95% | 99.98%* |
| Precision | 0.02 | 0.95 |
| Recall | 0.94 | 0.75 |
| F1 Score | 0.04 | 0.84 |
| ROC-AUC | 0.99 | 0.99 |

> *Rounded to two decimal places.

---

# 🔍 Explainable AI

The project incorporates **SHAP (SHapley Additive exPlanations)** to interpret model predictions.

Implemented visualizations include:

- SHAP Summary Plot
- SHAP Feature Importance Plot
- SHAP Waterfall Plot
- Individual Prediction Explanation

These visualizations improve model transparency and help understand how different features influence fraud predictions.

---

# 🌐 Streamlit Application

The project includes an interactive Streamlit web application that allows users to:

- Enter transaction details
- Predict Fraud / Legitimate transactions
- View fraud probability
- Display transaction risk level
- Use the trained XGBoost pipeline directly

---

# 📂 Repository Structure

```text
Financial-Fraud-Detection/
│
├── app/
│   └── app.py
│
├── data/
│   └── AIML Dataset.csv
│
├── models/
│   └── best_xgb_pipeline.pkl
│
├── notebooks/
│   ├── 01_Fraud_Detection.ipynb
│   └── 02_SHAP_Explainability.ipynb
│
├── images/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Financial-Fraud-Detection.git
```

Move into the project directory

```bash
cd Financial-Fraud-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app/app.py
```

---

# 📸 Project Screenshots

## Streamlit Application

> Add a screenshot here.

```
images/app.png
```

---

## SHAP Summary Plot

> Add a screenshot here.

```
images/shap_summary.png
```

---

# 🎯 Skills Demonstrated

- Data Analysis
- Exploratory Data Analysis
- Feature Engineering
- Data Preprocessing
- Machine Learning
- Scikit-Learn Pipelines
- Logistic Regression
- XGBoost
- Hyperparameter Optimization
- Model Evaluation
- Explainable AI (SHAP)
- Streamlit Deployment
- Model Serialization

---

# 🔮 Future Improvements

- FastAPI REST API
- Docker Containerization
- Cloud Deployment (Render / Streamlit Cloud)
- Real-Time Fraud Detection Pipeline
- Monitoring & Logging

---



IIT Kharagpur

Feel free to connect or raise an issue if you have suggestions or questions regarding the project.
