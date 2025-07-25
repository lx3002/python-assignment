import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

# Sample data similar to R's trees dataset
data = {
    'Girth': [8.3, 8.6, 8.8, 10.5, 10.7, 10.8, 11.0, 11.0, 11.1, 11.2, 11.3, 11.4, 11.4, 11.7, 12.0, 12.9, 12.9, 13.3, 13.7, 13.8, 14.0, 14.2, 14.5, 16.0, 16.3, 17.3, 17.5, 17.9, 18.0, 18.0, 20.6],
    'Height': [70, 65, 63, 72, 81, 83, 66, 75, 80, 75, 79, 76, 76, 69, 75, 74, 85, 86, 71, 64, 78, 80, 74, 72, 77, 81, 82, 80, 80, 80, 87],
    'Volume': [10.3, 10.3, 10.2, 16.4, 18.8, 19.7, 15.6, 18.2, 22.6, 19.9, 24.2, 21.0, 21.4, 21.3, 19.1, 22.2, 33.8, 27.4, 25.7, 24.9, 34.5, 31.7, 36.3, 38.3, 42.6, 55.4, 55.7, 58.3, 51.5, 51.0, 77.0]
}
df = pd.DataFrame(data)

# Remove edgecolor from here
axes = scatter_matrix(df, alpha=1, figsize=(8, 8), diagonal='none', marker='o', color='black')

# Set marker style to unfilled black circles
for ax in axes.ravel():
    for artist in ax.collections:
        artist.set_facecolor('none')
        artist.set_edgecolor('black')

plt.suptitle('Scatterplot Matrix of Trees Dataset', y=1.02)
plt.show() 