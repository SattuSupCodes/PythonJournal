# list comprehensibility and readability
# code-way 1
symbols="#$&"
codes=[]
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

# code in more comprehensive way

symbols_="%$#"
codes=[ord(symbol) for symbol in symbols]
print(codes)