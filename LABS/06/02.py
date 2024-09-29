import pandas as pd

data = {
    'movies' : ["Charlie" , "Ready" , "The Lion King"],
    'runtimemovie' : [300 , 230 , 190] 
}

df = pd.DataFrame(data)
sortmovies = df.sort_values("runtimemovie" , ascending=False)
print(sortmovies)
