import time, timeit

def fortest(number):
    l = []
    for num in range(1, number + 1):
        l.append(num)
    #return l

def whiletest(number):
    l = []
    counter = 1
    while counter <= number:
        l.append(counter)
        counter +=1 
    #return l

beginning  = time.time()
fortest(100000)
ending = time.time()
print(ending - beginning)
   

beginning  = time.time()
whiletest(100000)
ending = time.time()
print(ending - beginning)
             
             
declaration = """
whiletest(10)"""

my_setup = '''
def whiletest(number):
    l = []
    counter = 1
    while counter <= number:
        l.append(counter)
        counter +=1 
    #return l
'''

length = timeit.timeit(declaration, my_setup, number = 10000000)

declaration2 = """
fortest(10)"""

my_setup2 = '''
def fortest(number):
    l = []
    for num in range(1, number + 1):
        l.append(num)
    #return l
'''

length2 = timeit.timeit(declaration2, my_setup2, number = 10000000)

print(length, length2)
