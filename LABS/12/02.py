import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
     

digits = load_digits()

df = pd.DataFrame(digits.data, columns=[f'pixel_{i}' for i in range(digits.data.shape[1])])
df['number_label'] = digits.target
     

pixels = df.drop('number_label', axis=1)
     

single_image_row = pixels.iloc[0]
     

single_image_array = single_image_row.to_numpy()
     

single_image_reshaped = single_image_array.reshape(8, 8)
     

plt.figure(figsize=(5, 5))
plt.imshow(single_image_reshaped, cmap='gray')
plt.title('Handwritten Digit Sample')
plt.axis('off')
plt.show()
     


scaler = StandardScaler()
pixels_scaled = scaler.fit_transform(pixels)
     

pca = PCA(n_components=2)
pixels_pca = pca.fit_transform(pixels_scaled)
     

print("Variance:")
print(pca.explained_variance_ratio_)
print(f"Total Variance: {sum(pca.explained_variance_ratio_)*100:.2f}%")
     
Variance:
[0.12033916 0.09561054]
Total Variance: 21.59%

plt.figure(figsize=(10, 8))
scatter = plt.scatter(pixels_pca[:, 0], pixels_pca[:, 1],
                      c=df['number_label'],
                      cmap='tab10',
                      alpha=0.7)
plt.colorbar(scatter, label='Digit')
plt.title('Digits in 2D PCA Space')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.show()
     
