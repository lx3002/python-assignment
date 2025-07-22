import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the birthwt dataset from statsmodels
from statsmodels.datasets import get_rdataset
birthwt = get_rdataset('birthwt', 'MASS').data

# Create the plot
plt.figure(figsize=(10, 6))

# Sort the ages and create a line plot
sorted_ages = sorted(birthwt['age'])
plt.plot(range(len(sorted_ages)), sorted_ages, marker='o', linestyle='-', markersize=4)

# Add title and labels
plt.title("(Sorted) Mother's Ages in Springfield MA, 1986")
plt.xlabel('Index')
plt.ylabel("Mother's Age")

# Show the plot
plt.tight_layout()
plt.show() 