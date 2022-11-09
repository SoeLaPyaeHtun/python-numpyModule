import numpy as np

# x = np.array([[1,2,3],[4,5,6],[7,8,9]])
# y = np.array([1,2,3])

# a = x + y
# print(a)


a = np.array([[7,5,3,2,5,3,2],[9,7,4,2,3,6,5]])
print(a)
print(a.sum(axis=0))
print(a.std(axis=None))
print(np.std(a, axis=None))