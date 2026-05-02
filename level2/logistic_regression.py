# Import libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# -----------------------------
# 1. Load dataset (FIXED PATH)
# -----------------------------
df = pd.read_csv("datasets/Churn_Prediction_Data/churn-bigml-80.csv")

print("Dataset loaded successfully!")
print(df.head())

# -----------------------------
# 2. Drop unnecessary columns
# -----------------------------
df.drop(["State", "Area code"], axis=1, inplace=True)

# -----------------------------
# 3. Encode categorical data
# -----------------------------
for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

# -----------------------------
# 4. Split features & target
# -----------------------------
X = df.drop("Churn", axis=1)
y = df["Churn"]

# -----------------------------
# 5. Feature Scaling
# -----------------------------
scaler = StandardScaler()
X = scaler.fit_transform(X)

# -----------------------------
# 6. Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 7. Train model
# -----------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# -----------------------------
# 8. Predictions
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# 9. Evaluation
# -----------------------------
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
