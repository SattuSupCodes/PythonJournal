a='how you doin?'
b='sup?'
print(a,b)
choices=input("choose 'how you doin?' or 'sup?': ")
if(choices==a):
    print("you think you joey?")
elif(choices==b):
    print("srsly? sup? you could do better")
else:
    print("just choose from the options bruh")
    
'''nesting conditions'''
destination=input("choose your destination: ").lower()
if (destination =='mountain'):
    print('visit Mussoorie')
else:
    if(destination=='beach'):
        print('visit Goa')
    else:
        print('uhhh')
    
    
