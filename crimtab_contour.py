import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Simulated version of crimtab (use real if available)
# We'll create a Gaussian-like matrix for demonstration
np.random.seed(0)
data = np.random.multivariate_normal([0.5, 0.5], [[0.01, 0.005], [0.005, 0.01]], 1000)
x = data[:, 0]
y = data[:, 1]

# Scale x and y to [0, 1] to match R's normalized output
scaler = MinMaxScaler()
xy_scaled = scaler.fit_transform(data)
x_scaled, y_scaled = xy_scaled[:, 0], xy_scaled[:, 1]

# Create 2D histogram (density matrix)
hist, xedges, yedges = np.histogram2d(x_scaled, y_scaled, bins=30, density=True)

# Create coordinate grid
X, Y = np.meshgrid(xedges[:-1], yedges[:-1])

# Plot contour
plt.contour(X, Y, hist.T, colors='black')  # transpose to match axes correctly
plt.title("Contour Plot of Criminal Data")
plt.xlabel("")
plt.ylabel("")
plt.grid(False)
plt.show()
