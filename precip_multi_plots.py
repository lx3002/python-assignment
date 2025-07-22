import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, probplot

# Simulate 'precip' dataset (70 annual precipitation values)
# Replace with your actual precipitation data if available
np.random.seed(42)
precip_data = np.random.normal(loc=40, scale=10, size=70)
precip_data = np.clip(precip_data, 0, 100) # Ensure values are positive and reasonable

# Set up the 2x2 subplot grid
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("Precipitation Data Analysis", fontsize=16, y=1.02) # Main title for the entire figure

# --- Plot 1: Boxplot (top-left) ---
ax00 = axes[0, 0]
ax00.boxplot(precip_data)
ax00.set_title("Boxplot of Precipitation")
ax00.set_ylabel("Precipitation (inches)")
ax00.grid(False) # R's default doesn't have grids on boxplots

# --- Plot 2: Histogram (top-right) ---
ax01 = axes[0, 1]
ax01.hist(precip_data, bins=10, edgecolor='black', facecolor='white', linewidth=1.2) # Unshaded like R's hist
ax01.set_title("Histogram of Precipitation")
ax01.set_xlabel("Precipitation (inches)")
ax01.set_ylabel("Frequency")
ax01.grid(False) # R's default doesn't have grids on histograms

# --- Plot 3: ECDF Plot (bottom-left) ---
ax10 = axes[1, 0]
precip_sorted = np.sort(precip_data)
n_precip = len(precip_data)
ecdf_y = np.arange(1, n_precip + 1) / n_precip
ax10.step(precip_sorted, ecdf_y, where='post', color='black', linewidth=1.5)
ax10.set_title("ECDF of Precipitation")
ax10.set_xlabel("Precipitation (inches)")
ax10.set_ylabel("Cumulative Probability")
ax10.grid(True, linestyle=':', alpha=0.6) # R ECDF often has a light grid or no grid

# --- Plot 4: Q-Q Plot (bottom-right) ---
ax11 = axes[1, 1]
# Calculate theoretical and sample quantiles
qq_result = probplot(precip_data, dist="norm", plot=None)
theoretical_quantiles = qq_result[0][0]
sample_quantiles = qq_result[0][1]
slope, intercept, r_value = qq_result[1][0], qq_result[1][1], qq_result[1][2]

# Plot Q-Q points
ax11.scatter(theoretical_quantiles, sample_quantiles, color='black', s=15, alpha=0.4, marker='o')

# Plot red reference line
ax11.plot(theoretical_quantiles, slope * theoretical_quantiles + intercept, color='red', linewidth=1)

ax11.set_title("Normal Q-Q Plot")
ax11.set_xlabel("Theoretical Quantiles")
ax11.set_ylabel("Sample Quantiles")
ax11.grid(False) # R's default qqplot doesn't have grids
ax11.set_aspect('equal', adjustable='box') # Make it square

plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to prevent title overlap
plt.show() 