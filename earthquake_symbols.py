import numpy as np
import matplotlib.pyplot as plt

# Create sample earthquake data (replace with actual quakes data)
np.random.seed(42)
# Generate 1000 random points around New Zealand
longitude = np.random.uniform(165, 190, 100)  # Longitude range
latitude = np.random.uniform(-40, -10, 100)   # Latitude range
magnitude = np.random.uniform(4, 6.5, 100)    # Magnitude range

# Calculate circle sizes based on magnitude
# Scale down the sizes to match R's output better
circle_sizes = 10 ** magnitude  # You may need to scale this for your data

# Create the scatter plot with varying circle sizes
plt.figure(figsize=(10, 6))
plt.scatter(longitude, latitude, s=circle_sizes, facecolors='none', edgecolors='black', linewidths=1)

# Customize the plot to match R's style
plt.title('Location of Earthquake Epicenters')
plt.xlabel('Latitude')
plt.ylabel('Longitude')

# Remove the grid
plt.grid(False)

# Show the plot
plt.show() 