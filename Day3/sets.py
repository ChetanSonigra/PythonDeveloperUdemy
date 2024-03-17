# unordered collection of unique elements
# set() expects only one argument
s = set([1,2,3,4]); print(s)
s = {1,'f',4,1}; print(s)
s = {}; print(s, type(s))
# print(s[0]) will throw  typeerror
#can't include list and dictionary in sets
# item assignment will TypeError
print(len(s))
s = set([1,2,3,4])
print(2 in s)
s1 = {1,2,3}; s2={3,4,5}
print(s1.union(s2))
s1.add(4)
print(s1)
s1.remove(4); print(s1)
s1.discard(7)
# discard doesn't throw erroe, remove throws error
print(s1.pop())  # removes any random element
s1.clear(); print(s1)  # removes all elements



