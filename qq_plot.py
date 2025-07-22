import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Example data (replace with real earthquake depths)
y = [3.4, 5.6, 4.8, 6.2, 3.9, 4.1, 5.3, 6.0, 4.5, 5.0]

# Generate QQ plot
res = stats.probplot(y, dist="norm")

# Extract quantiles and line fit
theoretical_quantiles, ordered_values = res[0]
slope, intercept, r = res[1]

# Plot QQ points
plt.scatter(theoretical_quantiles, ordered_values, color='black', s=15, alpha=0.4, marker='o')

# Plot red reference line
plt.plot(theoretical_quantiles, slope * np.array(theoretical_quantiles) + intercept, color='red', linewidth=1)

plt.title('Normal Q-Q Plot')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')
plt.grid(False)
plt.axis('equal')  # Make the plot square
plt.show()
