import random


print("welcome to hangman")

li=['pineapple', 'apple' , 'orange']

print("choose your word", li)

secret_word = random.choice(li)

guess = input("Guess a letter").lower

print(guess)


    