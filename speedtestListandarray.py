import numpy as np

from timeit import default_timer as timer


a1 = np.random.random(1000)
a2 = np.random.random(1000)

l1 = list(a1)
l2 = list(a2)

def dotList():
    dot = 0
    for i in range(len(l1)):
        dot += l1[i] * l2[i]
    return dot

def dott():
    return np.dot(a1, a2)

start = timer()
for t in range(1000):
    dotList()
end = timer()
t1 = end - start
print("ListCalculation",t1)


start = timer()
for t in range(1000):
    dott()
end = timer()
t2 = end - start
print("numpy calculation",t2)

print("ration: ",t1/t2)