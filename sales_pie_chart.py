import matplotlib.pyplot as plt

# Sales data
pie_sales = [0.12, 0.30, 0.26, 0.16, 0.04, 0.12]

# Labels for each slice
names = ["Blueberry", "Cherry", "Apple", "Boston Creme", "Other", "Vanilla Creme"]

# Colors for each slice
colors = ["blue", "red", "green", "wheat", "orange", "white"]

# Create the pie chart
plt.figure(figsize=(8, 8)) # Make it square for a nice circle
plt.pie(pie_sales, labels=names, colors=colors, autopct='%1.1f%%', startangle=90)

# Add a title (optional, but good for clarity)
plt.title("Pie Chart of Sales")

# Ensure the circle is drawn as a circle
plt.axis('equal')

plt.show() 