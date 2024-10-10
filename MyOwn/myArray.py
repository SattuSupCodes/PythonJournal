# i want to create an array list using user inputs
myArray=[]

n=int(input("enter no. of elements: "))

for i in range(0,n):
    elements=int(input("enter your elements: "))
    myArray.append(elements)
    
print(myArray)

# python simply uses lists as array, although you can try the import array method. 

import array as arr 
a=arr.array('I', [1,2,3])
print(a)
# do i even remember how to code lamao