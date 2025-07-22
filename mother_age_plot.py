import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the birthwt dataset from statsmodels
from statsmodels.datasets import get_rdataset
birthwt = get_rdataset('birthwt', 'MASS').data

# Create the plot
plt.figure(figsize=(10, 6))

# Create histogram using seaborn
sns.histplot(data=birthwt, x='age', bins=10, kde=True) # Assuming 'age' column in birthwt is mother's age

# Add title and labels
plt.title("Mother's Ages in Springfield MA, 1986")
plt.xlabel("Mother's Age")
plt.ylabel('Frequency')

# Show the plot
plt.tight_layout()
plt.show() 