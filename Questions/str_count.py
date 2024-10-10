# to check whether two strings (cat and hat) come in a string same number of times or not (return true else false)

str1 = ["cat"]
str2 = ["hat"]

str3 = [str1,str2]
x = str3.count(str1)
y = str3.count(str2)

your_str = str(input("enter your string"))

while str1 and str2 in your_str:
    if x == y:
        print(True)
    else:
        print(False)
    break
    

def count_fun(s):
    s.count("cat") == s.count("hat")
    
str4 = str(input("enter your string: "))
print(count_fun(str4))

# nhi horha 