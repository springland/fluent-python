symbols = '$¢£¥€¤'
s_tuple = (ord(symbol) for symbol in symbols)
print(s_tuple)
for s in s_tuple:
    print(s)
import array
s_array = array.array('I', (ord(symbol) for symbol in symbols))
print(s_array)

a , b , *rest = range(5)
print(rest)
