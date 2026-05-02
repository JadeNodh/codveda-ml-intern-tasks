# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans

# -----------------------------
# 1. Load dataset
# -----------------------------
df = pd.read_csv("datasets/Churn_Prediction_Data/churn-bigml-80.csv")

print("Dataset loaded!")
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
# 4. Remove target (unsupervised)
# -----------------------------
X = df.drop("Churn", axis=1)

# -----------------------------
# 5. Feature scaling
# -----------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------------
# 6. Find optimal K (Elbow Method)
# -----------------------------
wcss = []  # within-cluster sum of squares

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plot elbow graph
plt.plot(range(1, 11), wcss)
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.show()

# -----------------------------
# 7. Apply K-Means (choose K=3 or 4 based on graph)
# -----------------------------
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)

# Add cluster labels to dataset
df["Cluster"] = clusters

print("\nClustered Data:\n", df.head())

# -----------------------------
# 8. Visualize clusters (2D)
# -----------------------------
# Using first 2 features for visualization
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters)
plt.title("Customer Clusters")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()