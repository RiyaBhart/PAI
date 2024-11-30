1. Download any clustering dataset from internet and after finding how many optimum number of
clusters should be formed using elbow curve, apply k-means on it.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
df = pd.read_csv('/content/wine-clustering.csv')
df.head()
df.describe()
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_df = scaler.fit_transform(df)
pd.DataFrame(scaled_df)
pd.DataFrame(scaled_df).describe()

kmeans = KMeans(n_clusters=3, init='k-means++')
kmeans.fit(scaled_df)

kmeans.inertia_
SSE = []
for i in range(1,20):
  kmeans = KMeans(n_clusters=i, init='k-means++')
  kmeans.fit(scaled_df)
  SSE.append(kmeans.inertia_)

frame = pd.DataFrame({'Cluster':range(1,20), 'SSE':SSE})
plt.figure(figsize=(12,6))
plt.plot(frame['Cluster'], frame['SSE'], marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('SSE')
plt.show()
kmeans = KMeans(n_clusters=11, init='k-means++')
kmeans.fit(scaled_df)
pred = kmeans.predict(scaled_df)
frame = pd.DataFrame(scaled_df)
frame['cluster'] = pred
frame['cluster'].value_counts()
