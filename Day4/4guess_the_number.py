from random import *
name = input('Enter your name: ')
s = randint(1,100)
g = int(input(f'Hello, {name}.I have a secret number between 1 to 100. Can you identify it?'))
i =1
while i<8:
    if g not in range(1,101):
        g = int(input(f'Try again!, secret number is between 1 to 100, you have guessed outside this range. '))
    elif g == s:
        print(f'Hey {name}, you won! You have guessed it in {i} attempts.')
        break
    elif g < s:
        g = int(input('Try again!, your guess is lower than secret number. '))
    else:
        g = int(input('Try again!, your guess is higher than secret number. '))
    i += 1
if i == 8 and g!=s:
    print(f'Game Over! secret number was {s}.')
elif i==8:
    print(f'Hey {name}, you won! You have guessed it in {i} attempts.')
    




