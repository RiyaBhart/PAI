import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

df = pd.read_csv("new.csv")
df = pd.DataFrame(df)

sizes = []

x_values = df["Species"]
y_values = df["PetalWidthCm"]
clrs = ['pink', 'green', 'yellow', 'red', 'purple', 'black']

plt.scatter(x_values, y_values, c = clrs)
plt.show()
