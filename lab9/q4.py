import matplotlib.pyplot as plt
import pandas as pd

#data from the question
data = {'age': [18, 22, 24, 29, 32, 34, 37, 40, 25, 28, 23, 31, 33, 39, 26, 21, 36, 38, 35, 27]}
df = pd.DataFrame(data)

#age groups definition
age_bins = [18, 25, 30, 35, 100]  
age_labels = ['18-25', '26-30', '31-35', '36 and above']

# Categorize ages into defined groups
df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=False)

# Count the number of students in each age group
age_group_counts = df['age_group'].value_counts()

#plotting the piechart
plt.figure(figsize=(8, 8))
plt.pie(age_group_counts, labels=age_group_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Distribution of Student Ages")
plt.show()
