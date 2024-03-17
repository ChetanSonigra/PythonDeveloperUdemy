# immutable, faster than list, ordered sequence of elements.

t = tuple(); print(type(t))
t = (1,); print(type(t))
t = (1,'f', 5.5)
t = 1,2,3
print(t[2])
# t[0] = 5  throws error tuple doesn't support item assignment
l = list(t); print(type(l))
a,b,c = l
print(a,b,c)
l = tuple(l); print(type(l))
x,y,z = t
print(x,y,z) # if not same number of elements on both, it will raise ValueError
t = 1,2,3,1

print(t.count(1))
print(t.index(2))