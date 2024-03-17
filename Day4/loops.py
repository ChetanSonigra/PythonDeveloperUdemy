#iterables: in which elements can be iterated. list, str, dict, tuple 

letters = ['a', 'b', 'c']
for l in letters:
    l_num = letters.index(l) +1
    print(f"letter {l_num}:", l)

numbers = [i for i in range(9)]
sum = 0
for n in numbers:
    if n%2==0:
        sum=sum+n
print(sum)

for a,b in [[1,2], [3,4],[5,6]]:
    print(a,b)

d = {'a':1, 'b':2, 'c':3}
for i in d:
    print(i)
for i in d.items():
    print(i)
for i in d.values():
    print(i)


#While

coins = 5
while coins>0:
    print(f'I have {coins} coins')
    coins -=1
else:
    print('I have no more coins.')


#pass - just as a placeholder. 
#break - breaks the loop.
#continue - goes to next iteration without executing remaining 
# lines in loop for particular iteration

name = input('Enter your name: ')

for k in name:
    if k == 'r':
        break
    print(k)
name = input('Enter your name: ')

for k in name:
    if k=='r':
        continue
    print(k)

