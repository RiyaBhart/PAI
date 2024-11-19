import pandas as pd
import matplotlib.pylab as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv(r"C:\Users\Me\Desktop\heart.csv")

X = df.iloc[: ,:-1]
Y = df.iloc[:,-1]

X_train, X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state = 42,stratify = Y)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

accuracies = []
neighbors = range(1, 251)

for k in neighbors:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, Y_train)
    y_pred = knn.predict(X_test)
    acc = accuracy_score(Y_test, y_pred)
    accuracies.append(acc)


max_accuracy = max(accuracies)
min_accuracy = min(accuracies)
best_k = neighbors[accuracies.index(max_accuracy)]
worst_k = neighbors[accuracies.index(min_accuracy)]

print(f"Highest Accuracy: {max_accuracy:.2f} at n_neighbors = {best_k}")
print(f"Lowest Accuracy: {min_accuracy:.2f} at n_neighbors = {worst_k}")

plt.figure(figsize=(12, 6))
plt.plot(neighbors, accuracies, marker='o')
plt.title("Accuracy vs Number of Neighbors")
plt.xlabel("Number of Neighbors (k)")
plt.ylabel("Accuracy")
plt.grid(True)
plt.show()
