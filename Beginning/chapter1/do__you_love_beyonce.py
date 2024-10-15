def beyonce():
    jayz = str(input("do you love Beyonce? (Y/N): "))
    while jayz == 'N':
    
       print("you're lost, choose again")
       try_again_or_be_aaliyah = str(input("do you love beyonce?(Y,N): "))
       print(try_again_or_be_aaliyah)
       
       if try_again_or_be_aaliyah == 'Y':
           break
       else:
           continue
       
       
beyonce()
       