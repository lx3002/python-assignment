import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.datasets import get_rdataset
from scipy import stats

# Load the birthwt dataset
birthwt = get_rdataset('birthwt', 'MASS').data

# Create binary outcome variable for birth weight below 2500g
birthwt['birthwt_below_2500'] = (birthwt['bwt'] < 2500).astype(int)

# Remove the original birth weight column
X = birthwt.drop(['bwt', 'birthwt_below_2500'], axis=1)
y = birthwt['birthwt_below_2500']

# Add constant term for the intercept
X = sm.add_constant(X)

# Fit logistic regression model with explicit binomial family and logit link
glm_1 = sm.GLM(y, X, family=sm.families.Binomial(link=sm.families.links.logit()))
results = glm_1.fit()

# Create diagnostic plots
plt.style.use('seaborn')
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Diagnostic Plots for GLM.1', fontsize=14)

# Get model diagnostics
fitted_values = results.fittedvalues
residuals = results.resid_pearson
leverage = results.get_influence().hat_matrix_diag
cooks_d = results.get_influence().cooks_distance[0]

# 1. Residuals vs Fitted
axes[0, 0].scatter(fitted_values, residuals, alpha=0.5, color='blue')
axes[0, 0].axhline(y=0, color='red', linestyle='--')
axes[0, 0].set_xlabel('Fitted Values')
axes[0, 0].set_ylabel('Pearson Residuals')
axes[0, 0].set_title('Residuals vs Fitted')
# Add smoothed line
sns.regplot(x=fitted_values, y=residuals, scatter=False, ax=axes[0, 0], color='red', lowess=True)

# 2. Normal Q-Q Plot
residuals_sorted = np.sort(residuals)
quantiles = stats.norm.ppf(np.linspace(0.01, 0.99, len(residuals)))
axes[0, 1].scatter(quantiles, residuals_sorted, alpha=0.5, color='blue')
axes[0, 1].plot([min(quantiles), max(quantiles)], [min(quantiles), max(quantiles)], 'r--')
axes[0, 1].set_xlabel('Theoretical Quantiles')
axes[0, 1].set_ylabel('Sample Quantiles')
axes[0, 1].set_title('Normal Q-Q')

# 3. Scale-Location Plot
sqrt_abs_residuals = np.sqrt(np.abs(residuals))
axes[1, 0].scatter(fitted_values, sqrt_abs_residuals, alpha=0.5, color='blue')
axes[1, 0].set_xlabel('Fitted Values')
axes[1, 0].set_ylabel('sqrt(|Standardized Residuals|)')
axes[1, 0].set_title('Scale-Location')
# Add smoothed line
sns.regplot(x=fitted_values, y=sqrt_abs_residuals, scatter=False, ax=axes[1, 0], color='red', lowess=True)

# 4. Residuals vs Leverage
axes[1, 1].scatter(leverage, residuals, alpha=0.5, color='blue')
axes[1, 1].axhline(y=0, color='red', linestyle='--')
axes[1, 1].set_xlabel('Leverage')
axes[1, 1].set_ylabel('Pearson Residuals')
axes[1, 1].set_title('Residuals vs Leverage')
# Add Cook's distance contours
x = np.linspace(min(leverage), max(leverage), 100)
for i in [0.5, 1]:
    y = np.sqrt(i * (1 - x) / x)
    axes[1, 1].plot(x, y, 'r--', alpha=0.5)
    axes[1, 1].plot(x, -y, 'r--', alpha=0.5)

plt.tight_layout()
plt.show() 