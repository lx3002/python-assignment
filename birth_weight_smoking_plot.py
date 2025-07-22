import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the birthwt dataset from statsmodels
from statsmodels.datasets import get_rdataset
birthwt = get_rdataset('birthwt', 'MASS').data

# Create the plot
plt.figure(figsize=(10, 6))

# Create box plot using seaborn
sns.boxplot(data=birthwt, x='smoke', y='bwt')

# Add title and labels
plt.title("Birth Weight by Mother's Smoking Habit")
plt.xlabel("Mother Smokes")
plt.ylabel("Birth Weight (g)")

# Show the plot
plt.tight_layout()
plt.show() 