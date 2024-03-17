def a_sum(*args):       # any name can be given instead of args, but * is important. args is convention.
    total = 0
    for i in args:
        total += i
    return total
a_sum(34,34,33,4,5)
a_sum(2,4)
a_sum(2)

def a_sum(**kwargs):
    total = 0
    for k,v in kwargs.items():
        print(k,v)
        total += v
    return total
a_sum(a = 3,b =5,d = 2)
    
    
def test(n1,n2,*args,**kwargs):
    print(f'This is first value: {n1}')
    print(f'This is second value: {n2}')
    for arg in args:
        print(f'arg: {arg}')
    for k,v in kwargs.items():
        print(f'{k}: {v}')

test(3,5,55,55,4,33,43,a=3,g=55,d=22)
args = [2,4,5,3]
kwargs = {'a':3,'b':5}

test(5,3,args,kwargs)
test(5,3,*args,**kwargs)