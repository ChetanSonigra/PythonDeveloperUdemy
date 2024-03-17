def addition():
    n1 = int(input('Enter first number: '))
    n2 = int(input('Enter second number: '))
    print(n1+n2)
    print('Thanks for adding.' + 32)
try:
    #code you want to check.
    addition()
except TypeError:
    # execute if there is an error.
    print('You are concatenating different type of data.')
except ValueError:
    print('You have not provided correct value.')
except:
    print('something went wrong.')
else:
    # execute if there is no error.
    print('Everything went well.')
finally:
    # execute this always.
    print('closing.')
    
# you can search built-in exception in documentation.
# TypeError, ValueError, ZeroDivisionError

def ask_a_number():
    while True:
        try:
            n = int(input('Enter a number: '))
        except:
            print('You have not entered a number.')
        else:
            print(f'You have entered number {n}')
            break
    print('Thank you.')
ask_a_number()