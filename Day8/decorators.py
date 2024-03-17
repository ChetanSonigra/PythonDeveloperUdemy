# decorators are functions that modify behaviour of another functions.
# and help shorten our code.
# function is an object, which can be stored inside variable and can be added in argument
def decorate_greeting(function):
    def another_function(word):
        print('Hellow')
        function(word)
        print('Good Bye')
    return another_function

@decorate_greeting
def uppercase(text):
    print(text.upper())
    
@decorate_greeting
def lowercase(text):
    print(text.lower())
    
#decorated_uppercase  = decorate_greeting(uppercase) # for having different functions
#decorated_lowercase = decorate_greeting(lowercase)
lowercase('DSFsdf')

