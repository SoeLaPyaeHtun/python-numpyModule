import numpy as np


# l1 = [1,2,3]
# l2 = [4,5,6]

# a1 = np.array(l1)
# a2 = np.array(l2)

# dot = 0

# for i in range(len(l1)):
#     dot += l1[i] * l2[i]

# print(dot)

# dot=0
# print(dot)

# dot = np.dot(a1, a2)
# print(dot)

# dot = 0

# print((a1 * a2).sum())

# sum1 = a1 * a2 
# print(sum1)

# dot = np.sum(sum1)
# print(dot)
# print(np.sum(a2))


a = np.array([[1,2,3],[5,6,7],[8,7,5]])
b = np.array([[1,2],[3,4],[5,6]])

c = np.dot(a,b)
print(c)