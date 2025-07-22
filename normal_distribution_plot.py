import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define x values from -3 to 3 with a step of 0.01
x = np.arange(-3, 3.01, 0.01) # Use 3.01 to include 3.0

# Calculate the probability density function (PDF) for a standard normal distribution
y = norm.pdf(x)

# Create the plot with a line (type = "l")
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='black', linewidth=1.5)

# Customize the plot
plt.title("Normal Distribution")
plt.xlabel("x") # R's default x-label if not specified is often just "x"
plt.ylabel("f(x)")
plt.grid(True, linestyle=':', alpha=0.6) # Add a light grid for readability

plt.show() 