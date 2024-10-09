import numpy as np

# Define the data type for the structured array
dtype = np.dtype([
    ('name', 'U20'),   # String with max length 20
    ('height', 'f4'),  # Float (4 bytes)
    ('class', 'i4')    # Integer (4 bytes)
])

# Create the structured array with sample data
data = np.array([
    ('Alice', 5.5, 3),
    ('Bob', 6.0, 2),
    ('Charlie', 5.7, 3),
    ('David', 5.9, 2),
    ('Eve', 5.4, 3)
], dtype=dtype)

# Sort the structured array by class, then by height
sorted_data = np.sort(data, order=['class', 'height'])

# Print the sorted structured array
print("Sorted Structured Array:")
print(sorted_data)
