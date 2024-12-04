import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame(data)

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

pca = PCA(n_components=2) 
principal_components = pca.fit_transform(scaled_data)

pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])

print("Original DataFrame:")
print(df)

print("\nPCA Transformed DataFrame:")
print(pca_df)

print("\nExplained Variance Ratio:", pca.explained_variance_ratio_)
