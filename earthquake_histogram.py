import numpy as np
import matplotlib.pyplot as plt

# Create sample data (replace this with your actual earthquake data)
# This is a sample of 1000 earthquake depths
y = np.random.uniform(0, 700, 1000)  # Replace this with your actual data

# Create histogram with specific bin edges (0 to 700 with step of 70)
bins = np.arange(0, 701, 70)  # Creates array [0, 70, 140, ..., 700]
plt.hist(y, bins=bins, facecolor='none', edgecolor='black', linewidth=1.5)
plt.xlabel('Earthquake Depth')
plt.title('Histogram of Earthquake Depths')
plt.show() 