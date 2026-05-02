# Codveda ML Internship

This repository contains my Machine Learning internship tasks completed as part of the Codveda Technologies internship program.

---

## 📁 Project Structure

- Level 1: Basic Machine Learning
- Level 2: Intermediate Machine Learning
- Level 3: Advanced Machine Learning

---

# ✅ Level 1 – Basic Machine Learning

## 🔹 Task 1: Data Preprocessing

### 📌 Description:
Preprocessed a raw dataset to make it suitable for machine learning.

### ⚙️ Steps Performed:
- Handled missing values:
  - Numerical → filled with mean
  - Categorical → filled with mode
- Encoded categorical variables using Label Encoding
- Scaled numerical features using StandardScaler
- Split dataset into training and testing sets (80/20)

### 🛠️ Tools Used:
- Python
- Pandas
- Scikit-learn

---

## 🔹 Task 2: Linear Regression

### 📌 Description:
Built a Linear Regression model to predict house prices.

### 📊 Dataset:
- House Price Dataset (Boston Housing-style dataset)

### ⚙️ Steps Performed:
- Loaded and cleaned dataset
- Applied proper column naming
- Trained Linear Regression model
- Evaluated model performance

### 📈 Evaluation Metrics:
- Mean Squared Error (MSE): **19.37**
- R² Score: **0.65**

### 🔍 Insights:
- RM (number of rooms) has a **positive impact** on house price
- LSTAT (lower status population) has a **negative impact** on house price

### 🛠️ Tools Used:
- Python
- Pandas
- Scikit-learn
- Matplotlib (for visualization)

---

# ✅ Level 2 – Intermediate Machine Learning

## 🔹 Task 1: Logistic Regression

### 📌 Description:
Built a Logistic Regression model to predict customer churn.

### 📊 Dataset:
- Churn Prediction Dataset (churn-bigml-80.csv)

### ⚙️ Steps Performed:
- Loaded and cleaned the churn dataset
- Dropped unnecessary columns (State, Area code)
- Encoded categorical variables using Label Encoding
- Scaled features using StandardScaler
- Split dataset into training and testing sets (80/20)
- Trained Logistic Regression model
- Evaluated model performance

### 📈 Evaluation Metrics:
- Accuracy Score
- Confusion Matrix
- Classification Report (Precision, Recall, F1-Score)

### 🔍 Insights:
- Features like account length, charges, and customer service calls are key predictors for churn
- Binary classification distinguishes between churned and retained customers

### 🛠️ Tools Used:
- Python
- Pandas
- Scikit-learn

---

## 🔹 Task 2: K-Means Clustering

### 📌 Description:
Built a K-Means Clustering model for customer segmentation.

### 📊 Dataset:
- Churn Prediction Dataset (churn-bigml-80.csv)

### ⚙️ Steps Performed:
- Loaded and preprocessed the dataset
- Removed target variable (unsupervised learning approach)
- Scaled features using StandardScaler
- Applied Elbow Method to find optimal number of clusters
- Applied K-Means with K=3 clusters
- Visualized clusters in 2D space

### 📈 Evaluation Metrics:
- Within-Cluster Sum of Squares (WCSS) for Elbow Method
- Cluster distribution analysis

### 🔍 Insights:
- Customers naturally segment into distinct groups based on usage patterns
- Elbow method shows optimal K around 3-4 clusters

### 🛠️ Tools Used:
- Python
- Pandas
- Scikit-learn
- Matplotlib (for visualization)

---

# 🚀 Key Learnings

- Data preprocessing and cleaning techniques
- Handling real-world dataset issues (formatting, missing data)
- Building and evaluating regression models
- Understanding feature impact on predictions

---

# 🔥 Level 3 – Advanced Machine Learning

## 🔹 Task 1: Random Forest Classifier (Customer Churn)

### 📌 Description:
Built a Random Forest model to predict whether a customer will churn based on telecom dataset features.

### 📊 Dataset:
- Churn BigML Dataset

### ⚙️ Steps Performed:
- Data preprocessing and encoding
- Removed irrelevant features (e.g., phone number)
- Split dataset into training and testing sets
- Trained Random Forest Classifier
- Performed hyperparameter tuning using GridSearchCV
- Evaluated model using classification metrics
- Applied cross-validation
- Extracted feature importance

### 📈 Evaluation Metrics:
- Accuracy (Baseline): ~0.90+
- Accuracy (Tuned): ~0.90+
- Cross-validation Score: ~0.88+

### 🔍 Insights:
- Customer service calls strongly influence churn
- International plan users are more likely to churn
- Feature importance helps identify key business drivers

### 🛠️ Tools Used:
- Python
- Pandas
- Scikit-learn
- Matplotlib

---

## 🔹 Task 2: Support Vector Machine (SVM)

### 📌 Description:
Implemented SVM models to classify iris flower species and compared different kernel performances.

### 📊 Dataset:
- Iris Dataset

### ⚙️ Steps Performed:
- Data preprocessing and encoding
- Selected two features for visualization
- Applied feature scaling using StandardScaler
- Trained SVM models using:
  - Linear Kernel
  - RBF Kernel
- Compared performance of both models
- Visualized decision boundaries

### 📈 Evaluation Metrics:
- Linear Kernel Accuracy: ~0.90+
- RBF Kernel Accuracy: ~0.95+

### 🔍 Insights:
- RBF kernel performs better for non-linear data
- SVM is highly effective for classification tasks
- Decision boundary visualization improves model interpretability

### 🛠️ Tools Used:
- Python
- Pandas
- Scikit-learn
- Matplotlib

---

# 🚀 Updated Key Learnings

- Advanced classification techniques (Random Forest, SVM)
- Hyperparameter tuning and model optimization
- Cross-validation for reliable evaluation
- Feature importance and model interpretability
- Kernel-based learning in SVM

---

# 🔗 Updated Future Work

- Implement Neural Networks using TensorFlow/Keras
- Explore Deep Learning for classification tasks
- Apply ML models to real-world datasets

# 📌 Author

**Pasindu Janodh Chandupa Dissanayaka**  
Machine Learning Enthusiast | Software Engineering Undergraduate
