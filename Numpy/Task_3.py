import numpy as np

a = np.array([[1, 6],
              [2, 8],
              [3, 11],
              [3, 10],
              [1, 7]])

mean_a = np.array([a[:, 0].mean(), a[:, 1].mean()])

a_centered = np.subtract(a, mean_a)

a_centered_sp = a_centered[:, 0] @ a_centered[:, 1]

print(a_centered_sp / (a[:, 0].size - 1))