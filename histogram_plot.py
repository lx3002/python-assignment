import numpy as np
import matplotlib.pyplot as plt

# Create sample data (replace this with your actual data)
x = np.array([
    3624, 6315, 4530, 3378, 5114, 4884, 5348, 4809, 4815, 4091,
    4963, 4119, 5107, 4458, 4628, 4669, 3712, 3545, 3694, 5299,
    4755, 4751, 4675, 3098, 4254, 4347, 4508, 5149, 4281, 5237,
    3601, 4903, 3875, 5087, 4561, 3983, 4660, 4449, 4558, 3635,
    4167, 3821, 4188, 4022, 3907, 4701, 4864, 3617, 4468, 4566
])

# Create histogram with 8 breaks and unshaded rectangles
plt.hist(x, bins=8, facecolor='none', edgecolor='black', linewidth=1.5)
plt.xlabel('Income')
plt.title('Histogram of State Income in 1977')
plt.show() 