import pandas as pd


products = pd.read_csv('products.csv')
orders = pd.read_csv('orders.csv')

#showing the first 5 and last 10 rows of each DataFrame
print("Products DataFrame:")
print(products.head(5))
print(products.tail(10))

print("\nOrders DataFrame:")
print(orders.head(5))
print(orders.tail(10))

#total revenue generated from all orders
orders['TotalRevenue'] = orders['Quantity'] * products.loc[orders['ProductID'] - 1, 'Price'].values
total_revenue = orders['TotalRevenue'].sum()
print("\nTotal Revenue Generated from All Orders: $", total_revenue)

#top 5 best-selling products
best_seller = orders.groupby('ProductID').agg({'Quantity': 'sum'}).nlargest(5, 'Quantity')
best_seller_names = products[products['ProductID'].isin(best_seller.index)]
print("\nTop 5 Best-Selling Products:")
print(best_seller_names)

#top 5 low selling products
low_seller = orders.groupby('ProductID').agg({'Quantity': 'sum'}).nsmallest(5, 'Quantity')
low_seller_names = products[products['ProductID'].isin(low_seller.index)]
print("\nTop 5 Low Selling Products:")
print(low_seller_names)

#most common product category among the top 5 best-selling products
best_selling_categories = best_seller_names['Category'].value_counts()
most_common_category = best_selling_categories.idxmax()
print("\nMost Common Product Category Among Top 5 Best-Selling Products:", most_common_category)

#average price of products in each category
average_price_per_category = products.groupby('Category')['Price'].mean()
print("\nAverage Price of Products in Each Category:")
print(average_price_per_category)

#day, month, and year separately with the highest total revenue
orders['Order Date'] = pd.to_datetime(orders['Order Date'], format='%m-%d-%Y') #using regex to format date
orders['Day'] = orders['Order Date'].dt.day
orders['Month'] = orders['Order Date'].dt.month
orders['Year'] = orders['Order Date'].dt.year

# Total revenue per day, month, and year
daily_revenue = orders.groupby(['Year', 'Month', 'Day'])['TotalRevenue'].sum().reset_index()
highest_revenue_day = daily_revenue.loc[daily_revenue['TotalRevenue'].idxmax()]
print("\nHighest Total Revenue Day, Month, and Year:")
print(f"Day: {highest_revenue_day['Day']}, Month: {highest_revenue_day['Month']}, Year: {highest_revenue_day['Year']}")

#a new DataFrame that shows the total revenue for each month
monthly_revenue = orders.groupby(orders['Order Date'].dt.to_period('M'))['TotalRevenue'].sum().reset_index()
monthly_revenue.columns = ['Month', 'TotalRevenue']
print("\nTotal Revenue for Each Month:")
print(monthly_revenue)

#check for null values or invalid characters
print("\nNull Values in Products DataFrame:")
print(products.isnull().sum())

print("\nNull Values in Orders DataFrame:")
print(orders.isnull().sum())

#cleaning data if null values are found
products.dropna(inplace=True)
orders.dropna(inplace=True)

#checking for invalid characters in ProductID and Quantity columns (for orders)
orders= orders[orders['ProductID'].apply(lambda x: isinstance(x, int)) & orders['Quantity'].apply(lambda x: isinstance(x, int))]

print("\nCleaned Data:")
print(orders)
