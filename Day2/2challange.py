name = input('Enter your name: ')
sales = float(input('Enter your monthly sales: '))

print(f"Hello {name}, This month your commision is ${round(sales*0.13,3)}")