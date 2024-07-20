import random


print("welcome to hangman")

li=['pineapple', 'apple' , 'orange']



secret_word = random.choice(li)

print("Guess the characters")

guesses = ''

turns=10

while turns>10:
    failed=0
    
    for char in li:
        if char in guesses:
            print(char, end=""),
        else:
            print("_", end="" )
            failed += 1
            
    if failed == 0 :
      print("you won")
    else:
      print("oops")
      break
  
    guess = input("guess a character: ")
    if guess not in li:
        turns -= 1
        print("Wrong")
  


    




# for letter in secret_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")
        
# in process
    