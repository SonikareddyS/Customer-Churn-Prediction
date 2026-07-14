# 🏦 Customer Churn Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Application-black)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange)
![Random Forest](https://img.shields.io/badge/Model-Random%20Forest-success)

---

# 📌 Project Overview

Customer Churn Prediction is a Machine Learning web application that predicts whether a bank customer is likely to leave the bank based on customer information.

The project demonstrates a complete Machine Learning pipeline, including:

- 📂 Data Collection
- 🧹 Data Preprocessing
- 📊 Exploratory Data Analysis (EDA)
- 🤖 Model Training
- 📈 Model Evaluation
- 🌐 Flask Web Deployment

---

# 🚀 Features

- ✅ Customer Churn Prediction
- ✅ Churn Probability Score
- ✅ Risk Level Classification
- ✅ Personalized Customer Recommendation
- ✅ Input Validation
- ✅ Responsive User Interface
- ✅ Machine Learning Model Integration

---

# 🛠 Tech Stack

### Programming Language
- Python

### Machine Learning
- Scikit-Learn
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn

### Backend
- Flask

### Frontend
- HTML5
- CSS3
- JavaScript

### Model Serialization
- Joblib

---

# 📊 Dataset Summary

| Property | Value |
|----------|-------|
| Dataset | Bank Customer Churn Dataset |
| Total Records | 10,000 |
| Training Samples | 8,000 |
| Testing Samples | 2,000 |
| Features Used | 10 |
| Target Variable | Exited |

### Target Labels

```
0 → Customer Stays

1 → Customer Churns
```

---

# 🤖 Machine Learning Workflow

```
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Exploratory Data Analysis
   │
   ▼
Label Encoding
   │
   ▼
Feature Scaling
   │
   ▼
Train-Test Split
   │
   ▼
Random Forest Classifier
   │
   ▼
Model Evaluation
   │
   ▼
Model Serialization
   │
   ▼
Flask Deployment
```

---

# 📈 Model Performance

The final deployed model is a **Random Forest Classifier**.

| Metric | Score |
|---------|-------|
| Accuracy | **86.30%** |
| Precision | **78.54%** |
| Recall | **44.96%** |
| F1-Score | **57.19%** |
| ROC-AUC Score | **70.91%** |

---

# 📊 Classification Report

| Class | Precision | Recall | F1-Score |
|------|----------:|-------:|---------:|
| Customer Stays (0) | **0.87** | **0.97** | **0.92** |
| Customer Churns (1) | **0.79** | **0.45** | **0.57** |

---

# 🔲 Confusion Matrix

| Actual / Predicted | Stay | Churn |
|-------------------|-----:|------:|
| **Stay** | **1543** | **50** |
| **Churn** | **224** | **183** |

---

# 📁 Project Structure

```
Customer-Churn-Prediction
│
├── app
│   ├── app.py
│   ├── templates
│   │      └── index.html
│   └── static
│          ├── style.css
│          └── script.js
│
├── data
│
├── models
│   ├── churn_prediction_model.pkl
│   └── scaler.pkl
│
├── notebooks
│   └── Analysis.ipynb
│
├── reports
│
├── requirements.txt
│
└── README.md
```

---

# 🔍 Sample Prediction

### Sample Customer Details

| Feature | Value |
|---------|-------|
| Credit Score | 560 |
| Country | Germany |
| Gender | Female |
| Age | 55 |
| Tenure | 2 Years |
| Account Balance | ₹150,000 |
| Number of Products | 1 |
| Has Credit Card | No |
| Active Member | No |
| Estimated Salary | ₹65,000 |

### Prediction Result

- ⚠ **Customer is likely to Churn**
- **Prediction Probability:** **76.09%**
- **Risk Level:** **High Risk**

### Recommendation

- Offer loyalty rewards
- Provide cashback offers
- Assign a relationship manager
- Increase customer engagement

---

# 🖥 Application Screenshots

## 🏠 Home Page

<img width="1888" height="622" alt="image" src="https://github.com/user-attachments/assets/ad3d0d02-5885-455e-850a-6883de3e09d6" />


---

## 📊 Prediction Result

<img width="1912" height="342" alt="image" src="https://github.com/user-attachments/assets/63546691-cc77-4123-ad81-47aaf9b6ea98" />


---

# ⚙ Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/SonikareddyS/Customer-Churn-Prediction.git
```

### 2. Navigate to the Project Folder

```bash
cd Customer-Churn-Prediction
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application

```bash
cd app
python app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000
```

---

# 🚀 Future Improvements

- Improve recall through hyperparameter tuning
- Experiment with XGBoost and LightGBM
- Explain predictions using SHAP
- Interactive Analytics Dashboard
- Docker Deployment
- REST API Development
- Cloud Database Integration
- User Authentication

---

# ⭐ Support

If you found this project useful, please consider giving this repository a ⭐ on GitHub.

---

## 📬 Contact

GitHub: https://github.com/SonikareddyS

LinkedIn: https://linkedin.com/in/sonikareddys/
