import pandas as pd
from scipy import stats
from statsmodels.datasets import get_rdataset

# Load the birthwt dataset
birthwt = get_rdataset('birthwt', 'MASS').data

# Convert smoke values to "Yes" and "No"
birthwt['smoke'] = birthwt['smoke'].map({1: "Yes", 0: "No"})

# Separate birth weights for smokers and non-smokers
smokers_bwt = birthwt[birthwt['smoke'] == "Yes"]['bwt']
non_smokers_bwt = birthwt[birthwt['smoke'] == "No"]['bwt']

# Perform t-test
t_stat, p_value = stats.ttest_ind(smokers_bwt, non_smokers_bwt)

# Print results
print("\nT-test Results:")
print("-" * 50)
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")
print("\nSummary Statistics:")
print("-" * 50)
print("\nSmokers (Yes):")
print(f"Mean birth weight: {smokers_bwt.mean():.2f} g")
print(f"Standard deviation: {smokers_bwt.std():.2f} g")
print(f"Sample size: {len(smokers_bwt)}")
print("\nNon-smokers (No):")
print(f"Mean birth weight: {non_smokers_bwt.mean():.2f} g")
print(f"Standard deviation: {non_smokers_bwt.std():.2f} g")
print(f"Sample size: {len(non_smokers_bwt)}") 