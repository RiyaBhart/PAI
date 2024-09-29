import pandas as pd


xls = pd.ExcelFile(r'C:\Users\Me\Desktop\PAI LAB\lab6\employee.xlsx') 
df1 = pd.read_excel(xls, "Sheet1")
data = pd.DataFrame(df1)


year = 2019
filteremployee = data[data['Join_Year']==year]
print(filteremployee)
