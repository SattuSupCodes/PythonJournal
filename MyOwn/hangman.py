import random


print("welcome to hangman")

li=['pineapple', 'apple' , 'orange']

print("choose your word", li)

secret_word = random.choice(li)

guess = input("Guess a letter").lower

print(guess)

for letter in secret_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
        
# in process
    