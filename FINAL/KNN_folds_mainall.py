import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/content/dermatology.data', header=None, na_values="?")

df.fillna(df.median(), inplace=True)

X = df.iloc[:, :-1]  
Y = df.iloc[:, -1]  

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42, stratify=Y)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, Y_train)
Y_pred = knn.predict(X_test)
print("Confusion Matrix:\n", confusion_matrix(Y_test, Y_pred))
print("\nClassification Report:\n", classification_report(Y_test, Y_pred))
print("\nAccuracy Score:", accuracy_score(Y_test, Y_pred))

cm = confusion_matrix(Y_test, Y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="pink", xticklabels=np.unique(Y), yticklabels=np.unique(Y))
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
cv_scores = cross_val_score(knn, X, Y, cv=10)
print("\n10-Fold Cross Validation Scores:", cv_scores)
print("\nMean CV Accuracy:", np.mean(cv_scores))
