import pandas as pd
df1 = pd.read_csv(r'C:\Users\Me\Desktop\alcoholconsumption.csv')
alcoholconsumption = pd.DataFrame(df1)
print("Shape of dataset is : ",alcoholconsumption.shape)
print("Columns of dataset are : ",alcoholconsumption.columns)
