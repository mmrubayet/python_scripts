#import codecademylib
import pandas as pd

df = pd.read_csv('imdb.csv')

# df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']
df.rename(columns = {'name' : 'movie_title'}, inplace = True)

print(df)
