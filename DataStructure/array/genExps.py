'''GenExps save memory and has the same syntax as listcomps but are enclosed in parentheses 
rather than bracketts
'''

# initializing a tuple and an array using generator expression

symbols="%$^*"
myTuple=tuple(ord(symbol) for symbol in symbols)
print(myTuple)

import array
arr=array.array('I',(ord(symbol) for symbol in symbols))
print(arr)