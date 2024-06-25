# using 2D arrays we do cartesian product with listcomp
colors=['black', 'white']
sizes=['s', 'm', 'l']
tshirts=[(colors, size) for color in colors for size in sizes]
print(tshirts)

# second method
for color in colors:
    for size in sizes:
        print((color, size))
        
