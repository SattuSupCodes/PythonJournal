# hangman game 

import random
from wordList import word_list
# dictionary of key() 
hangman_art = { 0: ("   ",
                    "   ",
                    "   "),
                1: (" o ",
                    "   ",
                    "   "),
                2: (" o ",
                    " | ",
                    "   "),
                3: (" o ",
                    "/| ",
                     "   "),
                4: (" o ",
                    "/|\\",
                    "   "),
                5: (" o ",
                    "/|\\",
                    "/  "),
                6: (" o ",
                    "/|\\",
                    "/ \\")}

def hangman_display(wrong_guesses):
  print("***********")
  for line in hangman_art[wrong_guesses]:
    print(line)
  print("***********")

def display_hint(hint):
  print("".join(hint))

def display_answer(answer):
  print("".join(answer))

def main():
  answer = random.choice(word_list)
  hint = ["_"]*len(answer)
  wrong_guesses = 0
  guessed_letters = set()
  is_running = True
  
  while is_running:
    display_man(wrong_guesses)  # type: ignore
    display_hint(hint)
    guess = input("Enter a letter: ").lower()
    

if __name__ == "__main__":
  main()
  
# work in progress
