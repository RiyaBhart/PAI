import pandas as pd
import matplotlib.pylab as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv(r"heart.csv")
X = df.iloc[:, :-1]
Y = df.iloc[:, -1]

accuracies_by_seed = {}

for seed in range(1, 11):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=seed, stratify=Y)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, Y_train)
    y_pred = knn.predict(X_test)
    accuracy = accuracy_score(Y_test, y_pred)
    accuracies_by_seed[seed] = accuracy

print("Accuracies for each random seed (1-10):")
for seed, acc in accuracies_by_seed.items():
    print(f"Random Seed {seed}: Accuracy = {acc:.2f}")

max_seed = max(accuracies_by_seed, key=accuracies_by_seed.get)
min_seed = min(accuracies_by_seed, key=accuracies_by_seed.get)

print(f"\nHighest Accuracy: {accuracies_by_seed[max_seed]:.2f} at Random Seed = {max_seed}")
print(f"Lowest Accuracy: {accuracies_by_seed[min_seed]:.2f} at Random Seed = {min_seed}")
