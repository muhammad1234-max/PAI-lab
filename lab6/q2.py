import pandas as pd

df = pd.read_csv("movies.csv")

#will sort based on the data in the runtime column being in the descending order
sorted_data = df.sort_values(by="runtime",ascending=False)

print(sorted_data[["title","runtime"]])
