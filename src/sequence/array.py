from array import array
from random import random

## This is a generator
floats = array('d' , (random() for i in range( 10 **7)))
print(floats[-1])

floats = array('d' , [1.0 , 2.0])
print(floats)
print( floats[1])
floats = sorted(floats , reverse=True)
print(floats)

