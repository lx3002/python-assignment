import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Define x values (0 to 5)
x = np.arange(0, 6)

# Calculate binomial probabilities (dbinom(x, size=5, prob=2/5))
n_trials = 5
p_success = 2 / 5
y = binom.pmf(x, n=n_trials, p=p_success)

# Create the plot with vertical lines (type = "h")
plt.figure(figsize=(10, 6))
# Plot vertical lines (stems)
plt.stem(x, y, linefmt='k-', markerfmt='ko', basefmt='k-')

# Customize the plot
plt.title("Binomial Distribution")
plt.xlabel("Value")
plt.ylabel("Probability")
plt.grid(True, linestyle=':', alpha=0.6) # Add a light grid for readability

plt.xticks(x) # Ensure x-axis ticks are at integer values
plt.ylim(bottom=0) # Ensure y-axis starts at 0

plt.show() 