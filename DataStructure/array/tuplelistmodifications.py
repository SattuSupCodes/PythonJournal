'''trying modifications'''

myTuple=tuple([1,2,3])
myTuple_=tuple([4,5,6])

a=myTuple.__add__(myTuple_)
print(a) #adding both tuples into one
b= myTuple.__mul__(3) 
print(b) #repeated concatenation
c=myTuple.__rmul__(3)
print(c) # reversed repeated concatenation 
d= myTuple.__iter__()
print(d) #get iterator




