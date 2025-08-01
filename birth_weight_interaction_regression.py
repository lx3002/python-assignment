import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.datasets import get_rdataset

# Load the birthwt dataset
birthwt = get_rdataset('birthwt', 'MASS').data

# Create subset where mother's age <= 40
birthwt_noout = birthwt[birthwt['age'] <= 40]

# Convert smoke values to "Yes" and "No"
birthwt_noout['smoke'] = birthwt_noout['smoke'].map({1: "Yes", 0: "No"})

# Create interaction term between smoke and race
birthwt_noout['smoke_race'] = birthwt_noout['smoke'] + '_' + birthwt_noout['race'].astype(str)

# Prepare the data for regression
# Create dummy variables for smoking status and race interaction
X = pd.get_dummies(birthwt_noout[['age', 'smoke_race']], drop_first=True)
X = sm.add_constant(X)  # Adds constant term for intercept
y = birthwt_noout['bwt']     # Birth weight

# Fit the linear regression model
model = sm.OLS(y, X).fit()

# Print the model summary in a format similar to R
print("\nCall:")
print("lm(formula = bwt ~ age + smoke*race, data = birthwt_noout)")

print("\nResiduals:")
print(f"Min: {model.resid.min():.1f}")
print(f"1Q: {np.percentile(model.resid, 25):.1f}")
print(f"Median: {np.median(model.resid):.1f}")
print(f"3Q: {np.percentile(model.resid, 75):.1f}")
print(f"Max: {model.resid.max():.1f}")

print("\nCoefficients:")
print("-" * 70)
print("                     Estimate Std. Error t value Pr(>|t|)")
print("-" * 70)
print(f"(Intercept)         {model.params[0]:10.2f} {model.bse[0]:10.2f} {model.tvalues[0]:8.2f} {model.pvalues[0]:8.4f} ***")

# Print coefficients for age and interaction terms
for i, (name, param, se, t, p) in enumerate(zip(X.columns[1:], model.params[1:], model.bse[1:], model.tvalues[1:], model.pvalues[1:]), 1):
    significance = '***' if p < 0.001 else '**' if p < 0.01 else '*' if p < 0.05 else ''
    print(f"{name:<20} {param:10.2f} {se:10.2f} {t:8.2f} {p:8.4f} {significance}")

print("-" * 70)

print("\nResidual standard error:", f"{np.sqrt(model.mse_resid):.2f}", "on", f"{model.df_resid}", "degrees of freedom")
print(f"Multiple R-squared:  {model.rsquared:.4f}")
print(f"Adjusted R-squared: {model.rsquared_adj:.4f}")
print(f"F-statistic: {model.fvalue:.2f} on {len(model.params)-1} and {model.df_resid} DF, p-value: {model.f_pvalue:.4f}")

# Print number of observations
print(f"\nNumber of observations: {len(birthwt_noout)}")
print(f"Number of observations removed: {len(birthwt) - len(birthwt_noout)}")

# Print the unique combinations of smoke and race
print("\nUnique combinations of smoking status and race:")
print(birthwt_noout[['smoke', 'race']].drop_duplicates().sort_values(['smoke', 'race'])) 