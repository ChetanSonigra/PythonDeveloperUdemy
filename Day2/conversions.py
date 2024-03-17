a = 5
b = 5.5
c = a + b
print(type(a), type(b), type(c))  # implicit conversion

age = input('enter your age: ')
print(age, type(age))
age = int(age)
print(age, type(age))      # explicit conversion
new_age = age + 4
print("your new age is : " + str(new_age))