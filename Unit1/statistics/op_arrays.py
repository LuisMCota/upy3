import numpy as np

a1 = np.array([1,2,3])
#print(a1)

a2 = np.array([[[1,2,3],[4,5,6]]])
#print(a2)

a3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
#print(a3)

a = np.array([1,2,3])
b = np.array([1,0,1])
print(a@b)
print(a.dot(b))