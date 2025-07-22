import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the birthwt dataset from statsmodels
from statsmodels.datasets import get_rdataset
birthwt = get_rdataset('birthwt', 'MASS').data

# Create the plot
plt.figure(figsize=(10, 6))

# Create scatter plot using seaborn
sns.scatterplot(data=birthwt, x='age', y='bwt', alpha=0.6)

# Add title and labels
plt.title("Birth Weight by Mother's Age in Springfield MA, 1986")
plt.xlabel("Mother's Age")
plt.ylabel("Birth Weight (g)")

# Show the plot
plt.tight_layout()
plt.show() 