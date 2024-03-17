d = {'c1': 'value1', 'c2':'value1', 'c3': 'value3'}
print(d,type(d))

# unordered, mutable, pairs.

# keys need to be unique while values need not.

result = d['c1']
print(result)

customer = {'first_name': 'Chetan', 'last_name': 'Sonigra', 'Weight': 62, 'Height': 176.5}
query = (customer['Height'])
print(query)

d = {1:55, 2: [10,20,30], 3: {'s1':100, 's2':200}}
print(d[2])
print(d[2][1])
print(d[3]['s2'])

d[4] = 333  # adding  a pair
print(d)
d[1] = 10 # modifying a value of existing key.
print(d)
print(d.keys(), d.values(), d.items(), sep='\n')