# check status of an integer using boolean values (flag)

x = int(input("enter no.1: "))
y = int(input("enter no.2: "))

if x<0 and y>=0 or x>=0 and y<0 :
    flag = False
    print(flag)
elif x<0 and y<0:
    flag = True
    print(flag)
else:
    print("invalid input")  