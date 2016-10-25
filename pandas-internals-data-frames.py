import pandas as pd
fandango = pd.read_csv("fandango_score_comparison.csv")
print(fandango.head(2))
print(fandango.index)
# First 5 rows
fandango[0:5]
# From row at 140 and higher
fandango[140:]
# Just row at index 50
fandango.iloc[50]
# Just row at index 45 and 90
fandango.iloc[[45,90]]

# 2
fandango = pd.read_csv('fandango_score_comparison.csv')
n = fandango.shape
last =n[0] - 1
first_last = fandango.iloc[[0,last]]

# 3
fandango_films = fandango.set_index("FILM", drop = False)
# print(fandango_films.index)

# 4
# Slice using either bracket notation or loc[]
fandango_films["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]
fandango_films.loc["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]

# Specific movie
fandango_films.loc['Kumiko, The Treasure Hunter (2015)']

# Selecting list of movies
movies = ['Kumiko, The Treasure Hunter (2015)', 'Do You Believe? (2015)', 'Ant-Man (2015)']
fandango_films.loc[movies]
movies = ['The Lazarus Effect (2015)','Gett: The Trial of Viviane Amsalem (2015)', 'Mr. Holmes (2015)']
best_movies_ever = fandango_films.loc[movies]

# 5
import numpy as np

# returns the data types as a Series
types = fandango_films.dtypes
# filter data types to just floats, index attributes returns just column names
float_columns = types[types.values == 'float64'].index
# use bracket notation to filter columns to just float columns
float_df = fandango_films[float_columns]

# `x` is a Series object representing a column
deviations = float_df.apply(lambda x: np.std(x))

print(deviations)
