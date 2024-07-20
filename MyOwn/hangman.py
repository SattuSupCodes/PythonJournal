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
    




# for letter in secret_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")
        
# in process
    