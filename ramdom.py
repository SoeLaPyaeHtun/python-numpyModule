import numpy as np


a = np.random.random((3,2))

print(a)

b = np.random.randint(10,size =(2,3))
print(b)

c = np.random.randint(10,size=10)
print(c)


c = np.random.choice(10,size=10)
print(c)

c = np.random.choice([-2,3,-9],size=10)
print(c)