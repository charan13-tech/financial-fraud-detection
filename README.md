# 💳 Financial Fraud Detection using Machine Learning

> An end-to-end machine learning pipeline for detecting fraudulent financial transactions using Logistic Regression and XGBoost.

---

## 📖 Overview

Financial fraud has become a major challenge in digital payment systems. This project develops a machine learning pipeline capable of identifying fraudulent transactions using supervised learning techniques.

The project includes exploratory data analysis, data preprocessing, feature engineering, model training, hyperparameter tuning, and model evaluation. Two machine learning models—Logistic Regression and XGBoost—are compared to identify the most effective approach for fraud detection.

---

## ✨ Features

- Exploratory Data Analysis (EDA)
- Data Cleaning & Preprocessing
- Feature Engineering
- Scikit-Learn Pipeline
- Logistic Regression Baseline
- XGBoost Classifier
- Hyperparameter Tuning using RandomizedSearchCV
- Model Comparison
- Feature Importance Analysis

---

## 📊 Dataset

| Property | Value |
|----------|-------|
| Problem | Binary Classification |
| Domain | Financial Fraud Detection |
| Transactions | 6,362,620 |
| Features | 11 |

> **Note:** The dataset is not included due to its size.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost

---

# ⚙️ Machine Learning Workflow

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
Train/Test Split
      │
      ▼
Data Preprocessing
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
Feature Importance
```

---

# 📈 Model Comparison

| Metric | Logistic Regression | XGBoost |
|---------|--------------------:|---------:|
| Accuracy | 0.95 | 1.00* |
| Precision | 0.02 | 0.95 |
| Recall | 0.94 | 0.75 |
| F1 Score | 0.04 | 0.84 |
| ROC-AUC | 0.99 | 0.99 |

> *Rounded to two decimal places.

---

# 📂 Repository Structure

```text
Financial-Fraud-Detection/
│
├── notebooks/
│   └── 01_EDA.ipynb
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🚀 Getting Started

Clone the repository

```bash
git clone https://github.com/charan13-tech/financial-fraud-detection.git
```

Move into the project

```bash
cd financial-fraud-detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook

```bash
jupyter notebook
```

Open

```text
notebooks/01_EDA.ipynb
```

---

# 📌 Current Progress

- ✅ Data preprocessing pipeline
- ✅ Logistic Regression baseline
- ✅ XGBoost classifier
- ✅ Hyperparameter tuning
- ✅ Model comparison
- ✅ Feature importance analysis

---

# 🔮 Planned Enhancements

- SHAP Explainability
- FastAPI REST API
- Streamlit Dashboard
- Docker Containerization
- Model Serialization
- Cloud Deployment

---

# 📚 Skills Demonstrated

- Exploratory Data Analysis
- Data Preprocessing
- Feature Engineering
- Machine Learning
- Ensemble Learning
- Hyperparameter Optimization
- Model Evaluation
- Explainable AI (planned)
- MLOps Fundamentals (planned)

---

# 🤝 Contributing

Contributions are welcome. Feel free to fork the repository and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider starring the repository!
