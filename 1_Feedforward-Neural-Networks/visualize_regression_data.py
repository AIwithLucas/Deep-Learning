import matplotlib.pyplot as plt
import numpy as np

N = 1000 # no. samples
X = np.random.random((N, 2)) * 6 - 3 # uniformly distributed between (-3, 3)
Y = np.cos(2 * X[:, 0]) + np.cos(3 * X[:, 1])

fig = plt.figure(figsize=(15, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], Y)
plt.show()

