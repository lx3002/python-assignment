import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.datasets import get_rdataset

# Load the birthwt dataset
birthwt = get_rdataset('birthwt', 'MASS').data

# Create binary outcome variable for birth weight below 2500g
birthwt['birthwt_below_2500'] = (birthwt['bwt'] < 2500).astype(int)

# Remove the original birth weight column
X = birthwt.drop(['bwt', 'birthwt_below_2500'], axis=1)
y = birthwt['birthwt_below_2500']

# Add constant term for the intercept
X = sm.add_constant(X)

# Fit logistic regression model
glm_1 = sm.GLM(y, X, family=sm.families.Binomial(link=sm.families.links.logit()))
results = glm_1.fit()

# Get predicted probabilities
predicted_probs = results.predict(X)

# Create the plot
plt.figure(figsize=(10, 6))
plt.style.use('seaborn')

# Create scatter plot
plt.scatter(birthwt['bwt'], predicted_probs, alpha=0.5, color='blue')

# Add labels and title
plt.xlabel('Birth Weight (grams)')
plt.ylabel('Predicted Probability')
plt.title('Birth Weight vs Predicted Probability')

# Add a vertical line at 2500g
plt.axvline(x=2500, color='red', linestyle='--', alpha=0.5, label='2500g threshold')

# Add a horizontal line at 0.5
plt.axhline(y=0.5, color='green', linestyle='--', alpha=0.5, label='0.5 probability threshold')

# Add legend
plt.legend()

# Add grid
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show() 