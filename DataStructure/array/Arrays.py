from array import array
from random import random

arr=array('d', (random() for i in range(10)))
print(arr)
list=[1,2,3,4,5]
myarr=array('q', list)

print(myarr)

# lenght of an array and list
c=myarr.__len__()
print(c)
d=list.__len__()
print(d)
e=arr.__len__()
print(e)
# other functions

y=myarr.pop(2)
print(myarr)

