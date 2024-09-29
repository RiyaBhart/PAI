import pandas as pd

df1 = pd.read_csv(r'C:\Users\Me\Desktop\alcoholconsumption.csv')
alcoholconsumption = pd.DataFrame(df1)

year1 = 1987
year2 = 1989

filterconsump = alcoholconsumption[(alcoholconsumption['Year'] == year1) | (alcoholconsumption['Year'] == year2)]

print(filterconsump)
