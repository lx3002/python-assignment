import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Simulate the Puromycin dataset based on the structure described
# conc: numeric vector of substrate concentrations (ppm)
# rate: numeric vector of instantaneous reaction rates (counts/min/min)
# state: factor with levels "treated" "untreated"

# Sample data generation (realistic values based on web search)
# For "untreated"
conc_untreated = np.array([0.02, 0.02, 0.06, 0.06, 0.11, 0.11, 0.22, 0.22, 0.56, 0.56, 1.10])
rate_untreated = np.array([67, 51, 84, 86, 98, 115, 131, 124, 144, 158, 160])

# For "treated"
conc_treated = np.array([0.02, 0.02, 0.06, 0.06, 0.11, 0.11, 0.22, 0.22, 0.56, 0.56, 1.10, 1.10])
rate_treated = np.array([76, 47, 97, 107, 123, 139, 159, 152, 191, 201, 207, 200])

# Create DataFrame
data_untreated = pd.DataFrame({'conc': conc_untreated, 'rate': rate_untreated, 'state': 'untreated'})
data_treated = pd.DataFrame({'conc': conc_treated, 'rate': rate_treated, 'state': 'treated'})

Puromycin = pd.concat([data_untreated, data_treated]).reset_index(drop=True)

# Separate data for plotting
untreated_data = Puromycin[Puromycin['state'] == 'untreated']
treated_data = Puromycin[Puromycin['state'] == 'treated']

# Create the plot
plt.figure(figsize=(8, 6))

# Plot "untreated" data with pch=1 (empty circle)
plt.scatter(untreated_data['conc'], untreated_data['rate'],
            facecolors='none', edgecolors='black', marker='o', s=50, label='Untreated')

# Plot "treated" data with pch=16 (filled circle)
plt.scatter(treated_data['conc'], treated_data['rate'],
            color='black', marker='o', s=50, label='Treated')

# Add labels and title
plt.xlabel("Substrate concentration (ppm)")
plt.ylabel("Reaction velocity (counts/min/min)")
plt.title("Reaction Velocity vs. Substrate Concentration")

# Add legend
# For the legend, we need to manually create artists to control marker styles
from matplotlib.lines import Line2D

legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='Untreated', 
           markerfacecolor='none', markeredgecolor='black', markersize=8),
    Line2D([0], [0], marker='o', color='w', label='Treated', 
           markerfacecolor='black', markeredgecolor='black', markersize=8)
]

plt.legend(handles=legend_elements, loc="lower right")

plt.grid(True, linestyle='--', alpha=0.7)
plt.show() 