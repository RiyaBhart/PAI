import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Step 1: Load the dataset (Example: Wholesale Customers dataset)
# Replace this with your dataset
df = pd.DataFrame({
    'Fresh': [12669, 7057, 6353, 13265, 22615, 9413, 12126, 7579, 5963, 6006],
    'Milk': [9656, 9810, 8808, 11957, 5410, 8259, 3199, 4956, 3648, 11093],
    'Grocery': [7561, 9568, 7684, 4221, 7198, 5126, 6975, 9426, 6192, 18881],
    'Frozen': [214, 1762, 2405, 6404, 4809, 1781, 1235, 1669, 425, 1159],
    'Detergents_Paper': [2674, 3293, 3516, 507, 288, 618, 2845, 2566, 507, 1975],
    'Delicassen': [1338, 1776, 7844, 1788, 1524, 2474, 4076, 525, 1788, 5185]
})

# Step 2: Standardize the dataset
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Step 3: Apply K-Means for a range of clusters and compute inertia
inertia = []
cluster_range = range(1, 11)
for k in cluster_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

# Step 4: Plot the Elbow Curve
plt.figure(figsize=(8, 5))
plt.plot(cluster_range, inertia, marker='o')
plt.title('Elbow Method for Optimal Number of Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia (Sum of Squared Distances)')
plt.grid(True)
plt.show()

from sklearn.cluster import KMeans

# Using the same dataset from problem 1 (scaled_data already prepared)
optimal_clusters = 3  # Assume from elbow curve
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
kmeans.fit(scaled_data)

df['Cluster'] = kmeans.labels_
print("Customer Segments:\n", df.groupby('Cluster').mean())
