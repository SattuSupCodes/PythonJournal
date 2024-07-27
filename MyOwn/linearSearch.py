username = input("enter username: ")
namesData = ["natasha" , "shruti" , "kanak" , "ashrey" , "rahul"]

while username not in namesData:
    print("username not found")
    reEnter = input ("re-enter username: ")
    if reEnter in namesData:
        print("username found")
        break
    else:
        continue
    
import re


# linear search 


def linearSearch(array,x,n):
    for i in range(0,n):
       
     if array[i] == x:
        return i
    return -1

arr = [30,70,65,36,356,78,23,12,1,90]

x = int(input("enter index: "))

n = len(arr)
result = linearSearch(arr,x,n)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)


# linear search through index

def linearSearch_index(array,index):
    if 0<= index < len(array):
        return array[index]
    else:
        return "invalid index"
    
try:
    user_index = int(input("Enter the index: "))
    result = linearSearch_index(arr, user_index)
    print(f"Element at index {user_index}: {result}")
except ValueError:
    print("Please enter a valid integer for the index.")