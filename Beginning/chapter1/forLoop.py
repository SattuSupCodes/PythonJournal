'''for every true element, do soemthing'''
username=input("Enter username: ")
invalid="!@#$%^&*()"

for letter in username:
    if letter in invalid:
        print("this character not valid", letter)
    