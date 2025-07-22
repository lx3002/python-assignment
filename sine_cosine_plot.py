import numpy as np
import matplotlib.pyplot as plt

# Define x values from 0 to 2*pi with 100 points
x = np.linspace(0, 2 * np.pi, 100)

# Calculate sine and cosine values
sine = np.sin(x)
cosine = np.cos(x)

# Create the plot with both lines
plt.figure(figsize=(10, 6))

# Plot sine wave in black
plt.plot(x, sine, color='black', linestyle='-', linewidth=1.5, label='Sine')

# Plot cosine wave in black (same color as R's col=c(1,1))
plt.plot(x, cosine, color='black', linestyle='--', linewidth=1.5, label='Cosine') # Using dashed for differentiation

# Customize the plot
plt.title("Sine and Cosine Waves")
plt.xlabel("x")
plt.ylabel("Value")
plt.grid(True, linestyle=':', alpha=0.6) # Add a light grid for readability

# Add a legend
plt.legend(loc='upper right')

plt.show() 