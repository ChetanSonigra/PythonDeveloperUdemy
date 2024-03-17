from pathlib import Path,PureWindowsPath
from os import system, path,remove,rmdir,mkdir
folder = Path('insert your path here.')

def recipe_manager():
    Category_list = [category.name for category in Path.glob(folder,'*')]
    n = len([c for c in Path.glob(folder,'**/*') if c.is_file() ])
    print(f'Welcome to the recipe management! We have {n} recipes in {folder}')
    while True:
        i = choose_an_action()
        system('cls')
        if i == 1:
            category = choose_category(Category_list)
            recipe_name = choose_recipe(category)
            if recipe_name:
                read_recipe(category,recipe_name)
            #return to begining function can be provided here.
        elif i == 2:
            category = choose_category(Category_list)
            recipe = create_recipe(category)
            create_recipe_content(category,recipe)
            #return to begining function can be provided here.
        elif i == 3:
            create_category(Category_list)
            #return to begining function can be provided here.
        elif i == 4:
            category = choose_category(Category_list)
            recipe_name = choose_recipe(category)
            if recipe_name:
                delete_recipe(category,recipe_name)
            #return to begining function can be provided here.
        elif i == 5:
            category = choose_category(Category_list)
            delete_category(category)
            Category_list.remove(category)
            #return to begining function can be provided here.
        elif i == 6:
            return 'Thank you for using Recipe Manager!'
        else:
            print('Please choose correct option.')
            continue      
def choose_an_action():
    print('What you want to do: ')
    print('1. Read Recipe', '2. Create Recipe', '3. Create Category', 
          '4. Delete Recipe', '5. Delete Category', '6. Exit', sep='\n')
    option = input('Choose option 1 to 6: ')
    while option not in ('1','2','3','4','5','6'):
        return choose_an_action()
    return int(option)
def choose_category(category_list):
    while True:
        for category in category_list:
            print(category)
        result = input('Type category name from above option: ')
        if result in category_list:
            return result
        print('Enter correct name.')
def choose_recipe(category):
    recipe_list = [recipe for recipe in Path(folder,category).glob('*')]
    if len(recipe_list)<1:
        print(f'There are no recipe available in category {category}.')
        return
    while True:
        for recipe in recipe_list:
            print(recipe.stem)
        recipe = input('Choose from above recipe: ')
        if recipe in [recipe.stem for recipe in recipe_list]:
            return recipe
        else:
            print('Entered recipe does not exist. Enter from above option.')
def read_recipe(category,recipe):
    recipe_file = open(Path(folder,category,f'{recipe}.txt'))  # Error due to not adding .txt
    print(recipe_file.read())
    recipe_file.close()
def create_recipe(category):
    while True:
        recipe = input('Give a recipe name: ')
        if path.exists(Path(folder,category,recipe)):
            print('This recipe already exist. Give a new name.')
        else:
            with open(f'{folder}/{category}/{recipe}.txt', 'x') as fp: # didn't work with double quotes.
                pass
            break
    print(f'Your recipe {recipe} is created in category {category}.')
    return recipe
def delete_recipe(category, recipe):
    if path.exists(Path(folder,category,f'{recipe}.txt')):
        remove(Path(folder,category,f'{recipe}.txt'))
        print(f'Recipe {recipe} has been deleted.')
    else:
        print("The file does not exist")  
def create_category(Category_list):
    while True:
        category = input('Enter category name: ')
        if category not in Category_list:
            mkdir(Path(folder,category))
            Category_list.append(category)
            break
        else:
            print('This category {category} already exist.')
def delete_category(category):
    if path.exists(Path(folder,category)):
        rmdir(Path(folder,category))
        print(f'Category {category} has been deleted.')
    else:
        print(f'The category {category} does not exist.')
def create_recipe_content(category,recipe):
    content = input('Enter recipe contents: ')
    recipe =open(Path(folder,category,f"{recipe}.txt"),'w')
    recipe.write(content)
    recipe.close()      
recipe_manager()
    