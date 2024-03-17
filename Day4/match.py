series='N2'

if series == 'N1':
    print('Samsung')
elif series == 'N2':
    print('Nokia')
elif series == 'N3':
    print('iPhone')
else:
    print("This product is not available.")


match series:
    case 'N1':
        print('Samsung')
    case 'N2':
        print('Nokia')
    case 'N3':
        print('iPhone')
    case _:
        print("This product is not available.")

# structure match

client = {'name': 'Chetan',
          'age': 25,
          'occupation': 'IT Consultant'}
movie = {'title': 'Dhoom3',
         'credits': {'main_star': 'ABC',
                     'director': 'XYZ'}}

items = [client,movie, 'book']
for i in items:
    match i:
        case {'name': name,
              'age': age,
              'occupation': occupation}:
            print('This is client.')
            print(name, age, occupation)
        case {'title': title,
              'credits': {'main_star': main_star,
                          'director': director}}:
            print('This is movie.')
            print(title, main_star,director)
        case _:
            print("We don't know what is this.")