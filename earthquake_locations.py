import numpy as np
import matplotlib.pyplot as plt

# Create sample earthquake data (replace with actual quakes data)
np.random.seed(42)
# Generate 1000 random points around New Zealand
longitude = np.random.uniform(165, 180, 1000)  # Longitude range
latitude = np.random.uniform(-40, -30, 1000)   # Latitude range

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(longitude, latitude, color='black', s=15, alpha=0.6)

# Customize the plot to match R's style
plt.title('Location of Earthquake Epicenters')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Remove the grid
plt.grid(False)

# Show the plot
plt.show() 