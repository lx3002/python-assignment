import numpy as np
import matplotlib.pyplot as plt

# --- Simulate sample data (replace with your actual data for 'x' and 'y') ---
np.random.seed(42)
# Treated group (e.g., lower values)
x_data = np.random.normal(loc=100, scale=15, size=100)
# Untreated group (e.g., higher values)
y_data = np.random.normal(loc=120, scale=20, size=100)

# Filter data to match xlim if necessary, or just set xlim later
x_data = x_data[(x_data >= 60) & (x_data <= 200)]
y_data = y_data[(y_data >= 60) & (y_data <= 200)]

# --- Calculate ECDF for 'x' (Treated) ---
x_sorted = np.sort(x_data)
n_x = len(x_data)
y_ecdf_x = np.arange(1, n_x + 1) / n_x

# --- Calculate ECDF for 'y' (Untreated) ---
y_sorted = np.sort(y_data)
n_y = len(y_data)
y_ecdf_y = np.arange(1, n_y + 1) / n_y

# --- Create the plot ---
plt.figure(figsize=(10, 6))

# Plot ECDF for 'x' (Treated) - default black line
# 'where="post"' creates the vertical steps
plt.step(x_sorted, y_ecdf_x, where='post', color='black', linewidth=1.5, label='Treated')

# Plot ECDF for 'y' (Untreated) - blue line
plt.step(y_sorted, y_ecdf_y, where='post', color='blue', linewidth=1.5, label='Untreated')

# Customize the plot
plt.title("Treated versus Untreated")
plt.xlabel("Value")
plt.ylabel("Cumulative Probability")
plt.xlim(60, 200) # Set x-axis limits
plt.grid(True, linestyle=':', alpha=0.6) # Add a light grid for readability

# Add legend
plt.legend(loc="lower right", frameon=False) # Changed from "bottomright" to "lower right"

plt.show() 