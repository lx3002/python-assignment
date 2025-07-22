import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

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

# Plot image
plt.imshow(hist.T, origin='lower', aspect='auto', cmap='gray', extent=[0, 1, 0, 1])
plt.title("Image Plot of Criminal Data")
plt.xlabel("")
plt.ylabel("")
plt.grid(False)
plt.show() 