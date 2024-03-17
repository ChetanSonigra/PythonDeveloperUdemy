def return_distincts(a,b,c):
    s = a+b+c
    m = max(a,b,c)
    n = min(a,b,c)
    if s>15:
        return m
    elif s<10:
        return n
    else:
        return sorted([a,b,c])[1]
    
return_distincts(4,2,8)

def unique_letters(word):
    r  = []
    for i in word:
        if i not in r:
            r.append(i)
    return sorted(r)

unique_letters('entertaining')
            
def twozero(*args):
    c = -1
    for i in args:
        c = args.index(i,c+1)
        if i == 0 and c!=len(args)-1:
            if args[c]==args[c+1]:
                return True
            
    return False

twozero(3,5,6,0,2,3,2,0)
twozero(4,6,2,0,0,2,0,4)

def count_primes(n):
    c = 1
    if n <2:
        return 0
    for i in range(3,n+1):
        f = 0
        for j in range(2,i+1//2):
            if i%j==0 and i!=j:
                f = 1
                break
        if f == 0:
            c +=1
    return c
            
count_primes(5)
count_primes(50)
count_primes(15)
count_primes(2)
        