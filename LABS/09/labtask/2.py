import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

df = pd.read_csv("dataset.csv")
df = pd.DataFrame(df)

x_values = df["Species"]
y_values = df["SepalLengthCm"]
clrs = ['r', 'g', 'y']

plt.bar(x_values, y_values, color = clrs, width = 0.5)
plt.show()
