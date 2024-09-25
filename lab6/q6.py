import pandas as pd

#using same file as that in q5
df = pd.read_csv("alcohol_consumption.csv")

conditions = df['Year'].isin([1987,1989]) #condition to see if data on these years is present

filtered_data = df[conditions]

print(filtered_data)
