import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the birthwt dataset from statsmodels
from statsmodels.datasets import get_rdataset
birthwt = get_rdataset('birthwt', 'MASS').data

# Create the plot
plt.figure(figsize=(10, 6))

# Create count plot using seaborn
sns.countplot(data=birthwt, x='race')

# Add title and labels
plt.title("Count of Mother's Race in Springfield MA, 1986")
plt.xlabel('Race')
plt.ylabel('Count')

# Show the plot
plt.tight_layout()
plt.show() 