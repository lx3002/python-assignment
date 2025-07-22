import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create x and y values
x = np.linspace(-8, 8, 100)
y = np.linspace(-8, 8, 100)

# Create meshgrid
X, Y = np.meshgrid(x, y)

# Define the function
def f(x, y):
    r = np.sqrt(x**2 + y**2)
    # Handle division by zero at origin
    return np.sin(r) / np.where(r == 0, 1, r)

# Calculate z values
Z = f(X, Y)

# Create the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap='viridis', linewidth=0)

# Remove axes and box
ax.set_axis_off()

# Show the plot
plt.show() 