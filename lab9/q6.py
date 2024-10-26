import matplotlib.pyplot as plt

#random sample data
math_marks = [78, 85, 62, 90, 88, 76, 95, 89, 77, 84]
science_marks = [82, 80, 65, 88, 91, 73, 92, 86, 79, 83]

#plotting the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(math_marks, science_marks, color='blue', marker='o', label="Student Marks")

plt.xlabel("Mathematics Marks")
plt.ylabel("Science Marks")
plt.title("Comparison of Mathematics and Science Marks")
plt.legend(loc="upper left")  # Position legend at the top-left corner

# Show plot
plt.show()
