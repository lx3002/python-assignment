import numpy as np
import matplotlib.pyplot as plt

# Recreate the VADeaths dataset as a NumPy array
# Rows: Age groups (50-54, 55-59, 60-64, 65-69, 70-74)
# Columns: Population groups (Rural/Male, Rural/Female, Urban/Male, Urban/Female)
va_deaths_data = np.array([
    [11.7, 8.7, 15.4, 8.4],
    [18.1, 11.7, 24.3, 13.9],
    [26.9, 20.3, 37.0, 19.3],
    [41.0, 30.9, 54.6, 35.1],
    [66.0, 54.3, 71.1, 57.5]
])

# Labels for rows and columns
age_groups = ["50-54", "55-59", "60-64", "65-69", "70-74"]
pop_groups = ["Rural/Male", "Rural/Female", "Urban/Male", "Urban/Female"]

# Number of age groups and population groups
n_age_groups = len(age_groups)
n_pop_groups = len(pop_groups)

# Set up bar positions
bar_width = 0.2
index = np.arange(n_age_groups) # The x locations for the age groups

plt.figure(figsize=(12, 7))

# Create grouped bars
for i in range(n_pop_groups):
    plt.bar(index + i * bar_width, va_deaths_data[:, i], bar_width, label=pop_groups[i])

# Customize the plot
plt.xlabel("Age Group")
plt.ylabel("Death Rate per 1000")
plt.title("Virginia Death Rates per 1000 in 1940")
plt.xticks(index + bar_width * (n_pop_groups - 1) / 2, age_groups) # Center x-ticks
plt.legend(title="Population Group")
plt.grid(False) # Remove grid for R-like appearance

plt.show() 