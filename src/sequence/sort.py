

a = [3 , 7 , 2 , 1 , 8]

### Sorted is new list
b = sorted(a)
print(b)
print(id(a) , id(b))

### list sort is in place
list.sort(a)
print(a)
print(id(a))

def sort_tuple_key(x):
    return x[1]


a = [(3 , 6) , (2 , 10 , 2) , (4 , 3)]
print(sorted(a , key=len))

print('sort by second value ' , sorted(a , key = lambda x : x[1] ))

print(a)

fruits = ['grape', 'raspberry', 'apple', 'banana']
sorted(fruits)
sorted(fruits, reverse=True)
sorted(fruits, key=len)
sorted(fruits, key=len, reverse=True)
