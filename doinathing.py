#spec: 1-100, if divisible by 3, return fiz, divisible by 5, return buz, if both, return fizbuz, if neither, return the number
# modulo returns the remainder
# while loop to generate returns from 1 to 100
number = 1

while number < 101:

    if (number % 3 == 0) and (number % 5 == 0):
        print('fizbuz')
    elif number % 5 == 0:
        print('buz')
    elif number % 3 == 0:
        print('fiz')
    else:
        print(number)
    number += 1

name = input("Hello! My name is ######, what's yours?: ")
print(name + ' is a lovely name.')

play = input("Would you like to play a number game? [Y/N]: ")
play = str.upper(play)

game_over = False

if play == 'N':
    print("Ok, goodbye!")
    game_over = True
elif play == 'Y':
    print("Great!")
else:
    print(input("Type Y or N into the terminal. "))

import random
numbers = [1,2,3,4,5,6,7,8,9,10]
answer = int(random.choice(numbers))

guesses = 0

while guesses <= 3 and game_over == False:
    print("You have three (3) guesses to guess the number I am thinking!")
    guess = input("I am thinking of a number between 1 and 10 . . . : ")
    guess = int(guess)

    if guess == answer:
        print("You win!")
        play_again = input("Play again? [Y/N]: ")
        play_again = str.upper(play_again)
        if play_again == 'Y':
            guesses = 0
        elif play_again == 'N':
            print("Thanks for playing!")
            game_over = True
        else:
            print("Please answer Y or N.")
    else:
        print("Try again.")

    guesses += 1

    while guesses == 3:
        try_again = input("Game over! Play again? [Y/N]: ")
        try_again = str.upper(try_again)
        if try_again == 'Y':
            guesses = 0
            game_over = False
        elif try_again == 'N':
            print("Thanks for playing!")
            game_over = True
            