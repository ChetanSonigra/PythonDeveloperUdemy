if 5 == 2:
    print('It is correct.')
else:
    print('It is not correct.')

pet = 'dog'   #rabbit

if pet=='cat':
    print('You have a cat.')
elif pet == 'dog':
    print('You have a dog.')
elif pet == 'fish':
    print('You have a fish.')
else:
    print("Don't know which animal your pet is.")


#Nested if else.

age = 16
school_grade=9
if age<18:
    print('you are a minor.')
    if school_grade<7:
        print('failed.')
    else:
        print('passed.')
else:
    print('you are an adult.')