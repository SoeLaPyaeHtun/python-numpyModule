import numpy as np


a = np.arange(1,7)

# print(a.shape)

# b = a.reshape(2,3)
# c = a.reshape(3,2)
# print(b)
# print(c)


b = a[: , np.newaxis]
print(b)
print(b.shape)

c = a[np.newaxis, :]
print(c)
print(c.shape)