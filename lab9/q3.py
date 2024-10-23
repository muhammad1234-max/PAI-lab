import matplotlib.pyplot as plt

# Sample data: Ice cream flavors and the number of scoops sold
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookies and cream', 
           'tutti fruity', 'Pistachio', 'Mango']
scoops_sold = [150, 200, 80, 60, 90, 120, 70, 110]

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(scoops_sold, labels=flavors, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Distribution of Ice Cream Sales by Flavor')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular

# Show the plot
plt.show()
