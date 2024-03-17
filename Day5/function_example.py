coffee_price = [('Cappuccino', 1.5),
                ('Espresso',2.5),
                ('Mocha', 1.9)]

def most_expensive_coffee(list_of_coffes):
    highest_price = 0
    most_expensive_coffee = ''
    for coffee, price in list_of_coffes:
        if price> highest_price:
            highest_price = price
            most_expensive_coffee = coffee
        
    return f'Most expensive coffee is {most_expensive_coffee} with price of {highest_price}'

print(most_expensive_coffee(coffee_price))