import pandas as pd     
import numpy as np
fandango = pd.read_csv("fandango_score_comparison.csv")
# print(fandango.head(2))
# 3
# Import the Series object from pandas
from pandas import Series

series_film = fandango["FILM"]
series_rt = fandango["RottenTomatoes"]
film_names = series_film.values
rt_scores = series_rt.values
# 4
# print film_names
series_custom = Series(data = rt_scores, index = film_names)
# print(series_custom[['Minions (2015)', 'Leviathan (2014)']])

fiveten = series_custom[5:10]
# print(fiveten)
# 5
original_index = series_custom.index.tolist()
original_index = sorted(original_index)
sorted_by_index = series_custom.reindex(original_index)

#6
sc2 = series_custom.sort_index()
sc3 = series_custom.sort_values()
# print sc3

#7
s_new = series_custom/10
s_new = s_new.sort_index()
# print s_new

# Add each value with each other
np.add(series_custom, series_custom)
# Apply sine function to each value
np.sin(series_custom)
# Return the highest value (will return a single value not a Series)
np.max(series_custom)

series_normalized = series_custom/20

# 8
series_greater_than_50 = series_custom[series_custom > 50]
# print series_greater_than_50
# print(series_custom > 50)

# 9
rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])
rt_mean = (rt_users + rt_critics)/2
print rt_mean