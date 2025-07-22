import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.datasets import get_rdataset

# Load the birthwt dataset
birthwt = get_rdataset('birthwt', 'MASS').data

# Prepare the data for regression
X = birthwt[['age']]  # Mother's age
X = sm.add_constant(X)  # Adds constant term for intercept
y = birthwt['bwt']     # Birth weight

# Fit the linear regression model
model = sm.OLS(y, X).fit()

# Create a figure with 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Diagnostic Plots for Birth Weight ~ Mother\'s Age', y=1.02)

# 1. Residuals vs Fitted
axes[0, 0].scatter(model.fittedvalues, model.resid, alpha=0.5)
axes[0, 0].axhline(y=0, color='r', linestyle='--')
axes[0, 0].set_xlabel('Fitted values')
axes[0, 0].set_ylabel('Residuals')
axes[0, 0].set_title('Residuals vs Fitted')

# 2. Normal Q-Q plot
sm.qqplot(model.resid, line='45', ax=axes[0, 1])
axes[0, 1].set_title('Normal Q-Q')

# 3. Scale-Location plot
axes[1, 0].scatter(model.fittedvalues, np.sqrt(np.abs(model.resid)), alpha=0.5)
axes[1, 0].set_xlabel('Fitted values')
axes[1, 0].set_ylabel('√|Standardized residuals|')
axes[1, 0].set_title('Scale-Location')

# 4. Residuals vs Leverage
influence = model.get_influence()
leverage = influence.hat_matrix_diag
axes[1, 1].scatter(leverage, model.resid, alpha=0.5)
axes[1, 1].axhline(y=0, color='r', linestyle='--')
axes[1, 1].set_xlabel('Leverage')
axes[1, 1].set_ylabel('Residuals')
axes[1, 1].set_title('Residuals vs Leverage')

# Adjust layout and display
plt.tight_layout()
plt.show()

# Print additional diagnostic statistics
print("\nAdditional Diagnostic Statistics:")
print("-" * 50)
print(f"Mean of residuals: {np.mean(model.resid):.4f}")
print(f"Standard deviation of residuals: {np.std(model.resid):.4f}")
print(f"Skewness of residuals: {stats.skew(model.resid):.4f}")
print(f"Kurtosis of residuals: {stats.kurtosis(model.resid):.4f}")
print(f"Cook's distance range: {influence.cooks_distance[0].min():.4f} to {influence.cooks_distance[0].max():.4f}") 