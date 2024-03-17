# ordered sequence of objects.

l = ['a', 10, 3.3, [3,4,5]]

# indexing, slicing, mutable.
print(l, type(l), len(l))
print(l[2],l[:2])

l2 = [1,2,3]

print(l+l2, l, l2, sep='\n')
l3 =l +l2
print(l3)
l3[3] = 's'
print(l3)

l3.append('j'); print(l3)
l3.pop(); print(l3)
l3.pop(2); print(l3)
deleted = l3.pop(2); print(deleted)

l = ['g', 'm', 'b', 'o', 'c']
l.sort()   # inplace sort, returns None.
print(l)
l.reverse() # inplace reverse, returns None.
print(l)

l2 = sorted(l)
print(l2)