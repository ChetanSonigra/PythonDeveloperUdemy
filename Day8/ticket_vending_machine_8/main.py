"""
    This module is main function for ticket vending machine.
"""

from python1.Day8.ticket_vending_machine_8.helpers import m,c,p, add_lines
# can't provide "8_ticket..." as package name


def ticket_vending():
    """Ticket vending machine"""
    med = m()
    per = p()
    cos = c()
    while True:
        try:
            i = int(input('Enter 1 to continue 2 to exit: '))
        except ValueError:
            continue
        else:
            if i == 2:
                return "Thank you for using ticket vending machine!!"
            cat = select_category()
            calculate_number(cat,med,per,cos)


@add_lines
def calculate_number(category,med,per,cos):
    """This function calculates sequencial number for given category."""
    if category == 'Medicine':
        print(f'M-{next(med)}')
    elif category == 'Perfumes':
        print(f'P-{next(per)}')
    else:
        print(f'C-{next(cos)}')


def select_category():
    """This function selects category."""
    categories = ['Medicine','Perfumes','Cosmetics']
    while True:
        for i in categories:
            print(i)
        selected_cat = input('Enter a category: ')
        if selected_cat in categories:
            return selected_cat


ticket_vending()
