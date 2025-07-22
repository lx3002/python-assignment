import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the InsectSprays dataset
data = {
    'count': [10, 7, 20, 14, 14, 12, 10, 23, 17, 20, 14, 13, 11, 17, 21, 11, 16, 14, 17, 17, 19, 21, 7, 13, 0, 1, 7, 2, 3, 1, 2, 1, 3, 0, 1, 4, 3, 5, 12, 6, 4, 3, 5, 5, 5, 5, 2, 4, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'spray': ['A']*12 + ['B']*12 + ['C']*12 + ['D']*12 + ['E']*12 + ['F']*12
}
df = pd.DataFrame(data)

# Create the boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='spray', y='count', data=df, color='white', width=0.5)

# Customize the plot to match R's style
plt.title('Boxplot of Insect Counts by Spray Type')
plt.xlabel('Spray Type')
plt.ylabel('Count')

# Remove the grid
plt.grid(False)

# Show the plot
plt.show() 