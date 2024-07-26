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
  pass

def display_hint(hint):
  pass

def main():
  pass

if __name__ == "__main__":
  main()
  
# work in progress
print(hangman_art[2])