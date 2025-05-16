# 🏠 Bengaluru House Price Prediction System

A machine learning-based web application to predict house prices in Bengaluru using features like location, size (BHK), bathrooms, and square footage.

---

## 🚀 Demo

> Coming soon: []()

---

## 📌 Features

- 📊 Data Cleaning & Preprocessing
- 📈 Model Training using Lasso Regression, Ridge Regression
- 📦 Pipeline for OneHotEncoding, Scaling, and Regression
- 🌐 Web Interface using Streamlit or Flask
- 🔮 Real-time Price Prediction based on user inputs

---


---

## 💡 Dataset

- 📂 File: `Bengaluru_House_Data.csv`
- 🎯 Target: `price`
- 📋 Features:
  - `location`
  - `total_sqft`
  - `bath`
  - `bhk`

---

## 🧪 ML Model Pipeline

- `OneHotEncoder` → for categorical feature `location`
- `StandardScaler` → for `total_sqft`, `bath`, `bhk`
- `Lasso Regression` → for training (better regularization)

> Model trained using `Pipeline` and `ColumnTransformer`

---

## 🛠️ Installation & Setup

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/animesharyan07/Task3
cd Bengaluru-House-Price-Prediction
```
### 🔧 2. Create Virtual Environment
```bash
python -m venv env
env\Scripts\activate      
source env/bin/activate 
```
### 🔧 3. Install Dependencies
```bash
pip install pandas numpy scikit-learn flask joblib pickle
```

🌐 Technologies Used
Python 

pandas, numpy, scikit-learn

Lasso Regression, Ridge Regression

Flask 

joblib/ pickle for model serialization  


✍️ Developed by
👨‍💻 [Animesh Aryan]
