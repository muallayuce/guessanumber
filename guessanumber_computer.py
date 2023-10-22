# guess a number (computer)
import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input('Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess another number. Too low.')
        elif guess > random_number:
            print('Sorry, guess another number. Too high.')

    print("Congrats!")


guess(10)
