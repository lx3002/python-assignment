import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Recreate the AirPassengers dataset (monthly, 1949-1960)
# This is a sample recreation; you would typically load real data
dates = pd.date_range(start='1949-01', end='1960-12', freq='MS')
# Example: a trend with some seasonality and noise
passengers = (
    100 + np.arange(len(dates)) * 3 +
    50 * np.sin(np.arange(len(dates)) * np.pi / 6) +
    np.random.normal(0, 10, len(dates))
)
# Make sure values are positive
passengers = np.maximum(passengers, 100)

# Create a Pandas Series to simulate time series
air_passengers = pd.Series(passengers, index=dates)

# Create the time series plot
plt.figure(figsize=(12, 6))
plt.plot(air_passengers.index, air_passengers.values, color='black', linewidth=1)

# Customize the plot
plt.xlabel("Date")
plt.ylabel("Passengers (in thousands)")
plt.title("International Airline Passengers")
plt.grid(True, linestyle=':', alpha=0.6) # Add a light grid for readability, similar to R's style

plt.show() 