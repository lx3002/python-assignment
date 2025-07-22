import numpy as np
import matplotlib.pyplot as plt

# Create more realistic earthquake depth data
# Using a combination of normal distributions to simulate real earthquake depth patterns
np.random.seed(42)  # For reproducibility
y1 = np.random.normal(200, 50, 400)  # Shallow earthquakes
y2 = np.random.normal(400, 80, 400)  # Medium depth earthquakes
y3 = np.random.normal(600, 60, 200)  # Deep earthquakes
y = np.concatenate([y1, y2, y3])
y = np.clip(y, 0, 700)  # Ensure values are within reasonable range

# Sort the data for ECDF
y_sorted = np.sort(y)
n = len(y)
prob = np.arange(1, n + 1) / n  # Create cumulative probabilities

# Create ECDF plot
plt.figure(figsize=(10, 6))
plt.step(y_sorted, prob, where='post', color='black', linewidth=1.5)
plt.xlabel('Earthquake Depth')
plt.ylabel('Cumulative Probability')
plt.title('ECDF of Earthquake Depths')
plt.grid(True, alpha=0.3)
plt.show() 