import pandas as pd

newdf = pd.read_csv(r'heart.csv')
newdf[newdf['ca']==2]

groupbycp = newdf.groupby('cp')
groupbycp.mean()

# single group single column analysis
groupbycp['age'].mean()

# single group multiple column
groupbycp[['age','ca']].mean()

# multi group single column
multigroup = newdf.groupby(['cp', 'sex'])['age'].mean()
print(multigroup)

# multiple group multiple column
multigroupmulti = newdf.groupby(['cp', 'sex'])[['age','chol']].mean()
print(multigroupmulti)
