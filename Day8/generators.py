# generators saves space. 
# it produces elements when needed.
def my_function():
    return [x*10 for x in range(1,5)]
def my_generator():
    for x in range(1,5):
        yield x*10
print(my_function())
print(my_generator())
g = my_generator()
print(next(g))
print(next(g))  
print(next(g)); print(next(g))
print(next(g)) # stopiteration error

def my_generator():
    x = 1
    yield x
    x += 1
    yield x
    x += 1
    yield x

g = my_generator()
print(next(g))
print(next(g))
print('Hello World')
print(next(g))