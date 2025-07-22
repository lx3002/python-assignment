import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.datasets import get_rdataset

# Load the birthwt dataset
birthwt = get_rdataset('birthwt', 'MASS').data

# Prepare the data for regression
X = birthwt[['age']]  # Mother's age
X = sm.add_constant(X)  # Adds constant term for intercept
y = birthwt['bwt']     # Birth weight

# Fit the linear regression model
model = sm.OLS(y, X).fit()

# Print the model summary in a format similar to R
print("\nCall:")
print("lm(formula = bwt ~ age, data = birthwt)")

print("\nResiduals:")
print(f"Min: {model.resid.min():.1f}")
print(f"1Q: {np.percentile(model.resid, 25):.1f}")
print(f"Median: {np.median(model.resid):.1f}")
print(f"3Q: {np.percentile(model.resid, 75):.1f}")
print(f"Max: {model.resid.max():.1f}")

print("\nCoefficients:")
print("-" * 50)
print("             Estimate Std. Error t value Pr(>|t|)")
print("-" * 50)
print(f"(Intercept) {model.params[0]:10.2f} {model.bse[0]:10.2f} {model.tvalues[0]:8.2f} {model.pvalues[0]:8.4f} ***")
print(f"age         {model.params[1]:10.2f} {model.bse[1]:10.2f} {model.tvalues[1]:8.2f} {model.pvalues[1]:8.4f}")
print("-" * 50)

print("\nResidual standard error:", f"{np.sqrt(model.mse_resid):.2f}", "on", f"{model.df_resid}", "degrees of freedom")
print(f"Multiple R-squared:  {model.rsquared:.4f}")
print(f"Adjusted R-squared: {model.rsquared_adj:.4f}")
print(f"F-statistic: {model.fvalue:.2f} on 1 and {model.df_resid} DF, p-value: {model.f_pvalue:.4f}") 