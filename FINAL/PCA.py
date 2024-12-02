import pandas as pd

df = pd.read_csv('Analysis.csv')
df.head(5)

from sklearn.preprocessing import StandardScaler

df_numeric = df.select_dtypes(include=[np.number])

scaler = StandardScaler()
scaled_X = scaler.fit_transform(df_numeric)

scaled_X

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(scaled_X)
plt.figure(figsize=(8,6))
plt.scatter(principal_components[:,0],principal_components[:,1])
plt.xlabel('First principal component')
plt.ylabel('Second principal component')

df_comp = pd.DataFrame(pca.components_,index=['PC1','PC2'],columns=df_numeric.columns)
df_comp

import seaborn as sns

plt.figure(figsize=(20,3),dpi=150)
sns.heatmap(df_comp,annot=True)

pca.explained_variance_ratio_

np.sum(pca.explained_variance_ratio_)

pca_10 = PCA(n_components=10)
pca_10.fit(scaled_X)

np.sum(pca_10.explained_variance_ratio_)

explained_variance = []

explained_variance = []
for n in range(1, len(df_numeric.columns) + 1):
    pca = PCA(n_components=n)
    pca.fit(scaled_X)
    explained_variance.append(np.sum(pca.explained_variance_ratio_))



# Generate the line plot in a new figure
plt.figure(figsize=(8, 6))
plt.plot(range(1, len(explained_variance) + 1), explained_variance, marker='o', linestyle='-', color='b')
plt.xlabel("Number of Components")
plt.ylabel("Cumulative Variance Explained")
plt.title("Elbow Curve")
plt.grid(True)
plt.show()
