import random
import string
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word


def hangman():

    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_latters = set()

    while len (word_letters) > 0:
        print('you have used these latters: ' ,' '.join(used_latters))
        word_list = [letter if letter in used_latters else '-' for letter in word]
        print('current word: ', ''.join(word_list))

        user_latter = input('guess a later ').upper()
        if user_latter in alphabet - used_latters:
          used_latters.add(user_latter)
          if user_latter in word_letters:
              word_letters.remove(user_latter)


        elif user_latter in used_latters:
          print("You have already used that character , please try again latter.")

        else:
          print("invalid character . please try again later")

user_input  = input('type somethinghere .... = ')

hangman()
