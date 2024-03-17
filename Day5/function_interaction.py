from random import shuffle

sticks = ['-','--','---','----']

def mix_sticks(l):
    shuffle(l)
    return l

def try_your_luck():
    a_try = input('Choose a number: ')
    while a_try not in ['1','2','3','4']:
        a_try = input('Choose a number: ')
    return int(a_try)

def verify_try(a_list,a_try):
    if a_list[a_try-1] == '-':
        print('Wash the dishes.')
    else:
        print('You are safe this time.')    
    print(f'You got {a_list[a_try-1]}')
    
mixed_sticks = mix_sticks(sticks)
selection = try_your_luck()
verify_try(mixed_sticks,selection)
