'''While loops:
is it's true, repeat it'''

password=input("enter: ")
confirm=input("confirm: ")
while password!=confirm:
    print("wrong password")
    password=input("re-enter: ")
    confirm=input("confirm: ")
print("logged in")