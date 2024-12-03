import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,precision_score,f1_score,recall_score, accuracy_score, classification_report
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

df = pd.read_csv('/content/knn_skin_disease_dataset.csv', na_values='?')

numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

X = df.iloc[:, :-1]
Y = df.iloc[:, -1]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42, stratify=Y)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, Y_train)

y_pred = knn.predict(X_test)

acc = accuracy_score(Y_test, y_pred)
print(f"Test Accuracy: {acc:.4f}")

cm = confusion_matrix(Y_test, y_pred)
print("Confusion Matrix:\n", cm)

sns.heatmap(cm, cmap='pink', annot=True, fmt="d", xticklabels=np.unique(Y), yticklabels=np.unique(Y))
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix Heatmap")
plt.show()

print("\nClassification Report:\n", classification_report(Y_test, y_pred))

cv_scores = cross_val_score(knn, X, Y, cv=4)
print("\nFold Cross Validation Scores:", cv_scores)
print("Mean CV Accuracy:", np.mean(cv_scores))

precision = precision_score(Y_test,y_pred,average='macro')
print(f"Precision: {precision:.2f}")

recall = recall_score(Y_test, Y_test, average='macro')
print(f"Recall: {recall:.2f}")

f1 = f1_score(Y_test, Y_test,average='macro')
print(f"F1 Score: {f1:.2f}")

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

lr = LogisticRegression()
lr.fit(X_train, Y_train)
y_pred_lr = lr.predict(X_test)
print("Accuracy:", accuracy_score(Y_test, y_pred_lr))
print("Confusion Matrix:\n", confusion_matrix(Y_test, y_pred_lr))
print("Classification Report:\n", classification_report(Y_test, y_pred_lr))

svm = SVC()
svm.fit(X_train, Y_train)
y_pred_svm = svm.predict(X_test)
print("Accuracy:", accuracy_score(Y_test, y_pred_svm))
print("Confusion Matrix:\n", confusion_matrix(Y_test, y_pred_svm))
print("Classification Report:\n", classification_report(Y_test, y_pred_svm))

