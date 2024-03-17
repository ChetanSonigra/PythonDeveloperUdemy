def add_lines(function):
    def add_func(cat,med,per,cos):
        print('Your number is ')
        function(cat,med,per,cos)
        print('Wait and someone will be with you shortly.')
    return add_func

def m():
    x = 0
    while True:
        x += 1
        yield x
def p():
    x = 0
    while True:
        x += 1
        yield x
def c():
    x = 0
    while True:
        x += 1
        yield x