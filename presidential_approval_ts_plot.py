import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Recreate the 'presidents' dataset (quarterly, 1945 Q1 to 1974 Q4)
# This is a sample recreation; you would typically load real data
dates = pd.date_range(start='1945-01-01', end='1974-12-31', freq='QS-JAN')

# Simulate approval ratings: start around 60%, with a slight decline, some fluctuations, and noise
# This simulates a general trend often seen in approval ratings
approval_ratings = (
    60 - np.arange(len(dates)) * 0.15 +
    5 * np.sin(np.arange(len(dates)) * np.pi / 8) +
    np.random.normal(0, 5, len(dates))
)
# Ensure ratings stay within a realistic range (e.g., 0-100)
approval_ratings = np.clip(approval_ratings, 20, 80)

# Create a Pandas Series to simulate the time series
presidents_data = pd.Series(approval_ratings, index=dates)

# Create the time series plot
plt.figure(figsize=(12, 6))
plt.plot(presidents_data.index, presidents_data.values, color='black', linewidth=1)

# Customize the plot
plt.xlabel("Date")
plt.ylabel("Approval Rating")
plt.title("Presidential Approval Ratings")
plt.grid(True, linestyle=':', alpha=0.6) # Add a light grid for readability, similar to R's style

plt.show() 