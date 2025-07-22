import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from mpl_toolkits.mplot3d import Axes3D # Import for 3D plotting

# Simulated version of crimtab (use real if available)
np.random.seed(0)
data = np.random.multivariate_normal([0.5, 0.5], [[0.01, 0.005], [0.005, 0.01]], 1000)
x = data[:, 0]
y = data[:, 1]

# Scale x and y to [0, 1]
scaler = MinMaxScaler()
xy_scaled = scaler.fit_transform(data)
x_scaled, y_scaled = xy_scaled[:, 0], xy_scaled[:, 1]

# Create 2D histogram (density matrix)
hist, xedges, yedges = np.histogram2d(x_scaled, y_scaled, bins=30, density=True)

# Create coordinate grid for the surface plot
X, Y = np.meshgrid(xedges[:-1], yedges[:-1])
Z = hist.T # Transpose to match axes

# Create the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X, Y, Z, cmap='viridis') # Using 'viridis' colormap

# Set the viewing angle (theta=30 degrees)
ax.view_init(elev=30, azim=30) # elev is elevation, azim is azimuth (theta)

ax.set_title("Perspective Plot of Criminal Data")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Density") # Z-axis usually represents density/frequency
plt.show() 