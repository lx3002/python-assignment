import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create sample data (you can replace this with your actual fevdata)
# This is just an example structure - replace with your actual data
data = {
    'height': [150, 155, 160, 165, 170, 175, 180, 185, 190],
    'fev': [2.5, 2.8, 3.0, 3.2, 3.5, 3.8, 4.0, 4.2, 4.5],
    'sex': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M'],
    'age_group': ['young', 'young', 'middle', 'middle', 'old', 'old', 'young', 'middle', 'old'],
    'smoke': ['yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes']
}

# Create DataFrame
fevdata = pd.DataFrame(data)

# Create the faceted scatter plot
plt.figure(figsize=(12, 8))

# Create the plot using seaborn's relplot
g = sns.relplot(
    data=fevdata,
    x='height',
    y='fev',
    hue='smoke',
    col='age_group',
    row='sex',
    kind='scatter',
    height=4,
    aspect=1.2
)

# Add labels
g.set_axis_labels('Height', 'FEV')
g.fig.suptitle('FEV vs Height by Sex and Age Group', y=1.02)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show() 