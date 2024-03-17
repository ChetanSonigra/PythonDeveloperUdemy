word = 'Python'
l = []
for i in word:
    l.append(i)
print(l)
l = [i for i in word if i not in 'yh']
print(l)

l = [n/5 for n in range(1,30,2) if n/5>3]; print(l)
l = [n/5 if n/5>3 else 'no' for n in range(1,30,2)]; print(l)