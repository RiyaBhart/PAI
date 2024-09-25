import pandas as pd

data = {
    'Title': ['Movie A', 'Movie B', 'Movie C', 'Movie D'],
    'Revenue': [2500000, 1500000, 3000000, 500000],
    'Budget': [900000, 800000, 950000, 400000]
}


df = pd.DataFrame(data)

filtered_movies = df[(df['Revenue'] > 2000000) & (df['Budget'] < 1000000)]

print(filtered_movies)
