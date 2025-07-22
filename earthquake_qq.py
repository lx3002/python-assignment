import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Create sample data (replace this with your actual earthquake data)
# Using the same earthquake depth data as before
np.random.seed(42)  # For reproducibility
y1 = np.random.exponential(scale=100, size=500)  # Shallow earthquakes
y2 = np.random.exponential(scale=200, size=300)  # Medium depth earthquakes
y3 = np.random.exponential(scale=300, size=200)  # Deep earthquakes
x = np.concatenate([y1, y2, y3])
x = np.clip(x, 0, 700)  # Ensure values are within reasonable range

# Create Q-Q plot
plt.figure(figsize=(8, 8))  # Square plot like R

# Calculate theoretical quantiles
theoretical_quantiles = stats.norm.ppf(np.linspace(0.01, 0.99, len(x)))
sample_quantiles = np.sort(x)

# Plot the Q-Q plot with small, transparent circles
plt.scatter(theoretical_quantiles, sample_quantiles, color='black', s=15, alpha=0.4, marker='o')

# Add the reference line
slope, intercept, r_value, p_value, std_err = stats.linregress(theoretical_quantiles, sample_quantiles)
plt.plot(theoretical_quantiles, slope * theoretical_quantiles + intercept, 'r-', linewidth=1)

# Remove grid and adjust axes
plt.grid(False)
plt.axis('equal')  # Make the plot square

plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')
plt.title('Normal Q-Q Plot')
plt.show() 