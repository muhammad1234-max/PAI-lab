#random temp values
temperatures = [
    30, 32, 33, 31, 29, 35, 34, 33, 32, 31, 
    30, 34, 32, 29, 28, 27, 26, 31, 33, 34, 
    35, 36, 30, 31, 32, 33, 30, 28, 29, 27
]

sum=0
for x in range(len(temperatures)):
    sum = sum+temperatures[x]

avg_temp = sum / len(temperatures)
print(f"average temperature: {avg_temp}")

#calculating highest and lowest temperature
highest = max(temperatures)
lowest = min(temperatures)
print(f"Highest Temperature: {highest}")
print(f"Lowest Temperature: {lowest}")

#sorting the list in ascending order using bubble sort
sorted_temp =temperatures.copy()
for i in range(len(sorted_temp) - 1):
    for j in range(len(sorted_temp) - 1 - i):
        if sorted_temp[j] > sorted_temp[j + 1]:
            # Swap the elements
            temp = sorted_temp[j]
            sorted_temp[j] = sorted_temp[j + 1]
            sorted_temp[j + 1] = temp


print(f"temperatures in ascending order: {sorted_temp}")

day_to_remove = 5
if 1 <= day_to_remove <= len(temperatures):
    removed = temperatures.pop(day_to_remove - 1)
    print(f"Removed Temperature for Day {day_to_remove}: {removed}")
else:
    print("Invalid day to remove.")
    
print(f"Temperatures after removal: {temperatures}")
