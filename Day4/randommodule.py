from random import *
# from random import randint, import random

my_random = randint(1,10); print(my_random) # 1,10 inclusive
my_random = uniform(1,5); print(my_random); print(round(my_random, 1))
my_random = random(); print(my_random) # chooses a float number between 0 and 1.
color = ['Blue','Red','Green','White']
my_random = choice(color); print(my_random)
l = list(range(5,50,5))
shuffle(l); print(l)
