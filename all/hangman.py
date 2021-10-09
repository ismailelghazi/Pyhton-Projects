# import  random
import random

list_of_words = ["lion", "mouse", "laptop"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
win = 0
list_of = random.choice(list_of_words)
# print(list_of)
number = len(list_of)
mots = []
died = 1
test = 6
for tr in range(number):
    mots += "_"
while not win:
    letter = input("give me a letter an i want find a word in this list ").lower()
    for x in range(number):
        letters = list_of[x]
        if letters == letter:
            mots[x] = letter

    print(mots)
    if letter not in list_of:
        test -= 1
        if test == 0:
            win = 1
            print("lose")

    if "_" not in mots:
        win = 1
        print("You win.")
    print(stages[test])
