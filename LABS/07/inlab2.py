import pandas as pd
df = pd.read_csv(r'heart.csv')

#changing nbame of column
df.rename(columns={'sex':'gender'},inplace=True)
print(df)

#finding min,max and mean of chol
print("min cholestrol : ",df['chol'].min())
print("max cholestrol : ",df['chol'].max())
print("mean cholestrol : ",df['chol'].mean())

#grouping 0 as female and 1 as male
df['gender']=df['gender'].map({0:'female',1:'male'})
print('0 as female and 1 as male : \n',df)

#group by female and male
female_group = df[df['gender'] == 'female']
print("female group : \n",female_group)

male_group = df[df['gender'] == 'male']
print("male group : \n",male_group)

#mean 
filterdata = df.groupby('gender').mean()
print("mean : ",filterdata)


