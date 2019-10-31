# Задача 8. Вариант 20.
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4)
# так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на
# подсказку в том случае, если у него нет никаких предположений. Разработайте
# систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки,
# получали больше тех, кто запросил подсказку.

# Смирнов Владимир Алексеевич
# 31.10.2019

# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
    """
               Welcome to Word Jumble!
    
       Unscramble the letters to make a word.
    (Press the enter key at the prompt to quit.)
    """
)
print("The jumble is:", jumble)

points = 5000  # Add
pos = 0  # Add
guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    points -= 25  # Add
    want_hint = input("Do you want a hint? (y/n): ")  # Add
    if want_hint == 'y':  # Add
        print("Correct letter with pos {} is {}".format(pos, correct[pos]))   # Add
        points -= 100  # Add
        pos += 1  # Add
    guess = input("Your guess: ")


if guess == correct:
    print("That's it!  You guessed it!\n")
    print("Your score: ", points)  # Add

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")


