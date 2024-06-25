'''walrus operator := used when you to assign a value to a variable within an expression. 
This can be useful when you need to use a value multiple times in a loop,
but don't want to repeat the calculation. '''

x="ABC"
codes=[last:= ord(c) for c in x]

print(codes)
print(last)

