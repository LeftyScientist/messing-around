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
print(name + 'is a lovely name.')

play = input("Would you like to play a math game? [Y/N]: ")
play = str.upper(play)

if play == 'N':
    print("Ok, goodbye!")
elif play == 'Y':
    print("Great!")
else:
    print(input("Type Y or N into the terminal. "))

