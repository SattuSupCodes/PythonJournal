'''sorting lists with built-in fucntions'''

l=['apple', 'raspberry', 'mango' , 'guava' , 'kiwi']

a=sorted(l)
b=sorted(l, reverse=True)
c=sorted(l, key=len)
d=sorted(l, key=len, reverse=True)
e=l.sort()
print(a,b,c,d,e)

