import pandas as pd

# fed the program a random data file made by me
df = pd.read_csv('movies.csv')
print(df)

filtered_movies = df[(df['revenue'] > 2_000_000) & (df['budget'] < 1_000_000)]


if filtered_movies.empty:
    print("No movies found with revenue > 2 million and budget < 1 million.")
else:
    print(filtered_movies[['title', 'revenue', 'budget']])

