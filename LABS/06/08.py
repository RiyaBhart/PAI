import pandas as pd

products = pd.read_csv(r'C:\Users\Me\Desktop\productsnew.csv', delimiter=',')
orders = pd.read_csv(r'C:\Users\Me\Desktop\ordersnew.csv', delimiter=',')

print(products.head(5))
print(products.tail(10))
print(orders.head(5))
print(orders.tail(10))

mergedf = pd.merge(orders, products, on='ProductID')
mergedf['Revenue'] = mergedf['Quantity'] * mergedf['Price']
totalrevenue = mergedf['Revenue'].sum()
print("Revenue is : ", totalrevenue, "\n")

productsales = mergedf.groupby('ProductID')['Revenue'].sum().reset_index()
productsales = pd.merge(productsales, products[['ProductID', 'ProductName']], on='ProductID')
top5products = productsales.sort_values(by='Revenue', ascending=False).head(5)
print("5 Best Selling Products based on Revenue: \n", top5products)

low5products = productsales.sort_values(by='Revenue', ascending=False).tail(5)
print("5 Low Selling Products based on Revenue: \n", low5products)

top5categories = mergedf[mergedf['ProductID'].isin(top5products['ProductID'])]['Category'].value_counts()
print("\nMost common product category among the top 5 best-selling products:")
print(top5categories.idxmax())

average = mergedf.groupby('Category')['Price'].mean()
print("\nAverage Price of product in each category : ",average)


mergedf['Order Date'] = pd.to_datetime(mergedf['Order Date'])
mergedf['Day']=mergedf['Order Date'].dt.day
mergedf['Month']=mergedf['Order Date'].dt.month
mergedf['Year']=mergedf['Order Date'].dt.year
dayrev = mergedf.groupby('Day')['Revenue'].sum()
monthrev = mergedf.groupby('Month')['Revenue'].sum()
yearrev = mergedf.groupby('Year')['Revenue'].sum()
print("\nDay with the highest total revenue:", dayrev.idxmax())
print("Month with the highest total revenue:", monthrev.idxmax())
print("Year with the highest total revenue:", yearrev.idxmax())

monthlyrevdf=mergedf.groupby('Month')['Revenue'].sum().reset_index()
print("Total Revenue for each Month : \n",monthlyrevdf)

print("\nChecking for null values in products data:")
print(products.isnull().sum())
print("\nChecking for null values in orders data:")
print(orders.isnull().sum())
