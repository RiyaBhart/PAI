

import matplotlib.pylab as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('bank_transactions_data_2.csv')

df.describe()

# Exclude non-numeric columns
df_numeric = df.select_dtypes(include=[np.number])

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_numeric)

pd.DataFrame(df_scaled).describe()
kmeans = KMeans(n_clusters=2,init='k-means++')
kmeans.fit(df_scaled)

kmeans.inertia_

SSE = []
for cluster in range(1,20):
  kmeans = KMeans(n_clusters = cluster,init='k-means++')
  kmeans.fit(df_scaled)
  SSE.append(kmeans.inertia_)

frame = pd.DataFrame({'Cluster':range(1,20),'SSE':SSE})
plt.figure(figsize=(12,6))
plt.plot(frame['Cluster'],frame['SSE'],marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')

# !pip install kneed

from kneed import KneeLocator

# Determine the elbow point
knee = KneeLocator(frame['Cluster'], frame['SSE'], curve='convex', direction='decreasing')
print(f'Elbow Point: {knee.knee}')


kmeans = KMeans(n_clusters = 6,init ='k-means++')
kmeans.fit(df_scaled)
pred = kmeans.predict(df_scaled)

frame = pd.DataFrame(df_scaled)
frame['cluster']=pred
frame['cluster'].value_counts()

