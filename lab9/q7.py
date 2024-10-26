import matplotlib.pyplot as plt
import numpy as np

#denerating random data for sealevel
years = np.arange(1923, 2023)  
sea_level_rise = np.cumsum(np.random.normal(loc=0.2, scale=0.1, size=len(years)))  # Cumulative rise with slight variations

# Plotting the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(years, sea_level_rise, color='teal', marker='o', label="Sea Level Rise")

# Adding labels and title
plt.xlabel("Year")
plt.ylabel("Sea Level Rise (mm)")
plt.title("Simulated Sea Level Rise Over the Past 100 Years")
plt.legend(loc="upper left") 

plt.show()
