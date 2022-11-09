import numpy as np


# a = np.array([[1,2,3,4],[5,6,7,8],[4,3,2,1]])

# print(a)
# print(a.shape)
# print(a[1,:])
# print(a[1,1])
# print(a[:,3])
# print(a[1,:])


# a = np.array([[1,2],[3,4],[5,6]])

# print(a.shape)
# print(a[a>2])

# b = np.where(a>2,a,-1)
# print(b)


a = np.array([1,2,3,4,5,6])
b = [2,3,4]
print(a[b])

print(a[np.argwhere(a%2==0).flatten()])