import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/knn_skin_disease_dataset.csv')
X = df.iloc[:, :-1]
Y = df.iloc[:, -1]

label_encoder = LabelEncoder()
Y_encoded = label_encoder.fit_transform(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y_encoded, test_size=0.3, stratify=Y_encoded, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(scaler.fit_transform(X))

plt.figure(figsize=(8, 5))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=Y_encoded, cmap='viridis')
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA Scatter Plot (Encoded Labels)")
plt.colorbar(label="Encoded Labels")
plt.show()

inertia = []
cluster_range = range(1, 11)
for cluster in cluster_range:
    kmeans = KMeans(n_clusters=cluster, random_state=42)
    kmeans.fit(X_pca)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(cluster_range, inertia, marker='o')
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.title("Elbow Method for Optimal Clusters")
plt.grid(True)
plt.show()

optimal_clusters = 4
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
clusters = kmeans.fit_predict(X_pca)

plt.figure(figsize=(8, 5))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='viridis')
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA with KMeans Clustering")
plt.show()

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, Y_train)
y_pred = knn.predict(X_test_scaled)

acc = accuracy_score(Y_test, y_pred)
f1score = f1_score(Y_test, y_pred, average='weighted')
cm = confusion_matrix(Y_test, y_pred)
cr = classification_report(Y_test, y_pred)

print("Accuracy score:", acc)
print("F1 score:", f1score)
print("Confusion Matrix:\n", cm)
print("Classification Report:\n", cr)

plt.figure(figsize=(8, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='pink', xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix Heatmap")
plt.show()

if cm.shape == (2, 2):
    TN, FP, FN, TP = cm.ravel()
    print("TP:", TP)
    print("TN:", TN)
    print("FP:", FP)
    print("FN:", FN)

cv_scores = cross_val_score(knn, X, Y_encoded, cv=4)
print("4-Fold Cross-Validation Scores:", cv_scores)
print("Mean CV Accuracy:", np.mean(cv_scores))
