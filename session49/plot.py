import matplotlib.pyplot as plt

# Our sales data for the year
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [12000, 15000, 18000, 16000, 21000, 22000, 19000, 23000, 25000, 28000, 30000, 26000]

# Create a figure and plot the data
# Size is set to 10 inches wide and 5 inches tall
plt.figure(figsize=(10, 5))
plt.plot(months, sales, label='Monthly Sales', color='indigo', linewidth=2, marker='o')

# Customize the plot with labels and a title
plt.title('Monthly Sales Performance')
plt.xlabel('Month')
plt.ylabel('Sales (in USD)')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
