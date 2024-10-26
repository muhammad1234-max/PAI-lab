import matplotlib.pyplot as plt

#defining the 3 lists
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     
y1 = [3, 5, 7, 10, 15, 18, 21, 25, 28, 30]  
y2 = [2, 4, 6, 9, 12, 14, 19, 22, 26, 27]  

#plot y1 vs x with a pink line and round markers
plt.plot(x, y1, color='pink', marker='o', linestyle='-', label='Metric 1 (y1)')

plt.plot(x, y2, color='gray', marker='o', linestyle='-', label='Metric 2 (y2)')


plt.title("Two Lines on One Graph")
plt.xlabel("Amazing X-axis")
plt.ylabel("Incredible Y-axis")

plt.legend(loc="lower right")
plt.show()
