import matplotlib.pyplot as plt

# Sample data: Cities and their respective populations
cities = ['karachi', 'islamabad', 'lahore', 'rawalpindi', 'sukkhur', 
          'hyderabad', 'peshawar', 'gilgit', 'hunza', 'Swat']
populations = [8419600, 3980400, 2716000, 2328000, 1681000, 
               1584200, 1547200, 1424500, 1343000, 1035300]

# Create a horizontal bar graph
plt.figure(figsize=(10, 6))
plt.barh(cities, populations, color='skyblue')
plt.xlabel('Population')
plt.title('Population of Cities')
plt.grid(axis='x')

# Show the plot
plt.tight_layout()
plt.show()
