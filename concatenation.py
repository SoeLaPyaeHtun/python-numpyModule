import numpy as np

# a = np.array([[1,2],[3,4]])
# print(a)
# print(a.shape)

# b = np.array([[5,6]])
# print(b)
# print(b.shape)

# c = np.concatenate((a,b))
# print(c)
# print(c.shape)

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

c = np.vstack((a,b))
print(c)

c = np.hstack((a,b))
print(c)

