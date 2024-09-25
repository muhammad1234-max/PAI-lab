import pandas as pd

#an existing DataFrame with random data from internet 
existing_df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Department': ['Finance', 'IT', 'HR'],
    'Year': [2019, 2020, 2021]
})

#importing data from the excel datasheet into a new dataframe
new_data = pd.read_excel('employee.xlsx') #excel sheet hasnt actually been defined

#concatenate the existing DataFrame with the new data
combined_df = pd.concat([existing_df, new_data], ignore_index=True)


filtered_employees = combined_df[combined_df['Year'] == 2024]
print(filtered_employees)
