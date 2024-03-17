d = {'key1': 44, 'key2': 11}

d.popitem()     # LIFO

# use . and hover over method to get idea of method.
# use python documentation.

# lstrip, isdisjoint
#lstrip: by default removes whitespaces.
print('  Arthur: three!'.lstrip('Arthur: '))

print('Arthur: three!'.removeprefix('Arthur: '))

#isdisjoint - checks if 2 sets are completely seperate or not.

s = {1,2,3}
s2 = {4,5,6}
s3={6,8,1}
print(s.isdisjoint(s2), s.isdisjoint(s3))