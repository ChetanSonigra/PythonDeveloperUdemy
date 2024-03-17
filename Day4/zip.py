names = ['a', 'b', 'c']
ages = [3,5,2,6]
cities = ['Rajkot', 'Mumbai', 'Chennai']

a = zip(names, ages)
print(a)
c = list(zip(names, ages, cities))
print(c)

for n, a, l in c:
    print(f"{n} is {a} years old and lives in {l}.")