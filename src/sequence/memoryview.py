import array
numbers = array.array('h' , [-2 , -1 , 0  , 1 , 2] )
print(numbers)
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)


import numpy as np

a = np.arange(12)
print(a)
print(type(a))
print(a.shape)
a.shape=3,4
print(a)
print(a[2])
print(a[2 , 1])
print(a[: , 1])
print(a.transpose())