import matplotlib.pyplot as plt
import numpy as np

# Sample height data for 20 students (in cm)
students = ['Student ' + str(i) for i in range(1, 21)]
heights = [160, 165, 170, 155, 180, 175, 168, 162, 172, 158,
           163, 177, 169, 164, 178, 159, 161, 166, 174, 173]

# Bar Chart
plt.figure(figsize=(10, 5))
colors = plt.cm.viridis(np.linspace(0, 1, len(students)))  # Generate different colors
plt.bar(students, heights, color=colors)
plt.title('Heights of Students in Class')
plt.xlabel('Students')
plt.ylabel('Height (cm)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(heights, labels=students, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Distribution of Heights of Students in Class')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
