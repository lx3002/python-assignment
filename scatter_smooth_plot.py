import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create sample data (you can replace this with your actual data)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.2, 100)  # Adding some noise

# Create the plot
plt.figure(figsize=(10, 6))

# Create scatter plot with smoothed line
sns.regplot(x=x, y=y, scatter_kws={'alpha':0.5}, 
            line_kws={'color': 'red'}, 
            lowess=True)  # lowess=True creates a smoothed line

# Add labels
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot with Smoothed Line')

# Show the plot
plt.show() 