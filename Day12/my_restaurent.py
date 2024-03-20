from tkinter import *
from tkinter import filedialog, messagebox
import random
import datetime, os
operator = ''

food_costs = [20,40,25,50,45,90,75,70]
drink_costs = [50,20,25,70,15,30,55,90]
dessert_costs = [20,50,25,50,45,50,45,40]

def click_button(character):
    global operator
    operator = operator+ character
    calculator_display.delete(0,END)
    calculator_display.insert(END,operator)
    
def delete_all():
    global operator
    operator = ''
    calculator_display.delete(0,END)

def get_result():
    global operator
    result = str(eval(operator))
    calculator_display.delete(0, END)
    calculator_display.insert(0, result)
    operator = ''
    
def review_check():
    x = 0
    for b in food_box:
        if food_variables[x].get() == 1:
            food_box[x].config(state=NORMAL)
            if food_box[x].get() == '0':
                food_box[x].delete(0,END)
            food_box[x].focus()
        else:
            food_box[x].config(state=DISABLED)
            food_text[x].set('0')
        x += 1
    
    x = 0
    for b in drink_box:
        if drink_variables[x].get()==1:
            drink_box[x].config(state=NORMAL)
            if drink_box[x].get() == '0':
                drink_box[x].delete(0,END)
            drink_box[x].focus()
        else:
            drink_box[x].config(state=DISABLED)
            drink_text[x].set('0')
        x += 1
        
    x = 0
    for b in dessert_box:
        if dessert_variables[x].get()==1:
            dessert_box[x].config(state=NORMAL)
            if dessert_box[x].get() == '0':
                dessert_box[x].delete(0,END)
            dessert_box[x].focus()
        else:
            dessert_box[x].config(state=DISABLED)
            dessert_text[x].set('0')
        x +=1

def total_calculation():
    food_subtotal = 0
    p = 0
    for x in food_text:
        food_subtotal += float(x.get())*food_costs[p]
        p+=1
    drink_subtotal = 0
    p = 0
    for x in drink_text:
        drink_subtotal += float(x.get())*drink_costs[p]
        p+=1
    dessert_subtotal = 0
    p = 0
    for x in dessert_text:
        dessert_subtotal += float(x.get())*dessert_costs[p]
        p+=1
    my_subtotal = food_subtotal + drink_subtotal + dessert_subtotal
    my_taxes = my_subtotal*0.11
    my_total = my_subtotal+my_taxes
    
    food_cost_var.set(f'Rs. {food_subtotal}')
    drink_cost_var.set(f'Rs. {drink_subtotal}')
    dessert_cost_var.set(f'Rs. {dessert_subtotal}')
    subtotal.set(f'Rs. {my_subtotal}')
    taxes.set(f'Rs. {my_taxes}')
    total.set(f'Rs. {my_total}')
    
def create_invoice():
    invoice_text.delete(1.0,END)
    invoice_number = f'N# {random.randint(1000,9999)}'
    my_date = datetime.datetime.now()
    invoice_date= f'{my_date.month}/{my_date.day}/{my_date.year} - {my_date.hour}:{my_date.minute}'
    invoice_text.insert(END, f'Information: \t{invoice_number}\t\t{invoice_date}\n')
    invoice_text.insert(END, f'*'*78 + '\n')
    invoice_text.insert(END, f'Items\t\tQuantity\tItems Cost\n')
    invoice_text.insert(END, f'-'*93 + '\n')
    x = 0
    for f in food_text:
        if f.get() != '0':
            invoice_text.insert(END, f'{food_list[x]}\t\t{f.get()}\t{food_costs[x]}*{f.get()}\n')
        x += 1
    x = 0
    for d in drink_text:
        if d.get() != '0':
            invoice_text.insert(END, f'{drink_list[x]}\t\t{d.get()}\t{drink_costs[x]}*{d.get()}\n')
        x += 1
    x = 0
    for dt in dessert_text:
        if dt.get() != '0':
            invoice_text.insert(END, f'{dessert_list[x]}\t\t{dt.get()}\t{dessert_costs[x]}*{dt.get()}\n')
        x += 1   
    invoice_text.insert(END, f'-'*93 + '\n')
    invoice_text.insert(END, f'Food Subtotal\t\t\t{food_cost_var.get()}\n')
    invoice_text.insert(END, f'Drink Subtotal\t\t\t{drink_cost_var.get()}\n')
    invoice_text.insert(END, f'Dessert Subtotal\t\t\t{dessert_cost_var.get()}\n')
    invoice_text.insert(END, f'-'*93 + '\n')
    invoice_text.insert(END, f'Subtotal\t\t\t{subtotal.get()}\n')
    invoice_text.insert(END, f'Taxes\t\t\t{taxes.get()}\n')
    invoice_text.insert(END, f'Total\t\t\t{total.get()}\n')
    invoice_text.insert(END, f'*'*78 + '\n')
    invoice_text.insert(END, F'See you soon!')

def save_invoice():
    invoice_info = invoice_text.get(1.0, END)
    my_file = filedialog.asksaveasfile('w',defaultextension='.txt')
    my_file.write(invoice_info)
    my_file.close()    
    messagebox.showinfo('Notification', 'Your invoice has been saved.')

def reset_display():
    invoice_text.delete(0.1, END)
    x = 0
    for f in food_box:
        f.config(state=DISABLED)
        food_text[x].set('0')
        food_variables[x].set('0')
        x +=1
    x = 0
    for d in drink_box:
        d.config(state=DISABLED)
        drink_text[x].set('0')
        drink_variables[x].set('0')
        x +=1
    x = 0
    for dt in dessert_box:
        dt.config(state=DISABLED)
        dessert_text[x].set('0')
        dessert_variables[x].set('0')
        x +=1
    food_cost_var.set('')
    drink_cost_var.set('')
    dessert_cost_var.set('')
    subtotal.set('')
    taxes.set('')
    total.set('')
    

# Initialize TK
application = Tk()

# window size
application.geometry('1200x630+0+0')

# prevent from maximizing
application.resizable(False,False)

# Window title
application.title('My Restaurant - Invoicing System')

# Window background color
application.config(bg='burlywood1')

# top panel
top_panel = Frame(application, bd=1, relief=FLAT) # FLAT, RAISED, SUNKEN, GROOVE, RIDGE
top_panel.pack(side=TOP)

# title tag
title_tag = Label(top_panel, text='Invoicing System', fg='azure4',
                  font=('Dosis', 58), bg='burlywood', width=30)

title_tag.grid(row=0, column=0)

# Left panel
left_panel = Frame(application, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

# Cost Panel
cost_panel = Frame(left_panel, bd=1, relief=FLAT,padx=150, bg='azure4')
cost_panel.pack(side=BOTTOM)

# Food Panel
food_panel = LabelFrame(left_panel, text='Food', fg= 'azure4',
                        bd=1, relief=FLAT, font=('Dosis', 19, 'bold'))
food_panel.pack(side=LEFT)

# Drink Panel
drink_panel = LabelFrame(left_panel, text='Drink', fg= 'azure4',
                        bd=1, relief=FLAT, font=('Dosis', 19, 'bold'))
drink_panel.pack(side=LEFT)

# Dessert Panel
dessert_panel = LabelFrame(left_panel, text='Dessert', fg= 'azure4',
                        bd=1, relief=FLAT, font=('Dosis', 19, 'bold'))
dessert_panel.pack(side=LEFT)

# Right Panel
right_panel = Frame(application, bd=1, relief=FLAT)
right_panel.pack(side= RIGHT)

# Calculator panel
calculator_panel = Frame(right_panel, bd=1, relief=FLAT, bg= 'burlywood')
calculator_panel.pack()

# Invoice Panel
invoice_panel= Frame(right_panel, bd=1, relief=FLAT, bg= 'burlywood')
invoice_panel.pack()

# buttons panel
buttons_panel = Frame(right_panel, bd=1, relief=FLAT, bg= 'burlywood')
buttons_panel.pack() 

# Product lists
food_list = ['Bhel', 'Samosa', 'Pizza1', 'Pizza2', 'Pizza3', 'Pizza4', 'Paneer', 'Panipuri']
drink_list = ['Juice','Lemon soda', 'Wine2', 'Rum', 'Water', 'Beer1', 'Beer2','Cola']
dessert_list = ['Ice cream', 'Peda', 'Mohanthal', 'Barfee', 'Pastry', 'Jamun', 'Browni', 'Halwa']

# create food items
food_variables = []
food_box = []
food_text = []
counter = 0 
for food in food_list:
    # create checkbuttons
    food_variables.append('')
    food_variables[counter]=IntVar()
    food = Checkbutton(food_panel, text=food.title(), font=('Dosis', 19, 'bold'),
                       onvalue=1, offvalue=0, variable=food_variables[counter],
                       command=review_check)
    food.grid(row=counter, column=0,sticky=W)
    
    # create input boxes
    food_box.append('')
    food_text.append('')
    food_text[counter] = StringVar()
    food_text[counter].set('0')
    food_box[counter]= Entry(food_panel, font=('Dosis',18, 'bold'), bd=1, 
                             width=6, state=DISABLED, textvariable=food_text[counter])
    food_box[counter].grid(row= counter, column = 1)   
    counter+=1

# create drink items
drink_variables = []
drink_box = []
drink_text = []
counter = 0 
for drink in drink_list:
    # create checkbuttons
    drink_variables.append('')
    drink_variables[counter]=IntVar()
    drink = Checkbutton(drink_panel, text=drink.title(), font=('Dosis', 19, 'bold'),
                       onvalue=1, offvalue=0, variable=drink_variables[counter],
                       command=review_check)
    drink.grid(row=counter, column=0,sticky=W)
    
    # create input boxes
    drink_box.append('')
    drink_text.append('')
    drink_text[counter] = StringVar()
    drink_text[counter].set('0')
    drink_box[counter]= Entry(drink_panel, font=('Dosis',18, 'bold'), bd=1, 
                             width=6, state=DISABLED, textvariable=drink_text[counter],
                             )
    drink_box[counter].grid(row= counter, column = 1)
    counter+=1
    
# create dessert items
dessert_variables = []
dessert_box = []
dessert_text = []
counter = 0 
for dessert in dessert_list:
    # create checkbuttons
    dessert_variables.append('')
    dessert_variables[counter]=IntVar()
    dessert = Checkbutton(dessert_panel, text=dessert.title(), font=('Dosis', 19, 'bold'),
                       onvalue=1, offvalue=0, variable=dessert_variables[counter],
                       command=review_check)
    dessert.grid(row=counter, column=0,sticky=W)
    
    # create input boxes
    dessert_box.append('')
    dessert_text.append('')
    dessert_text[counter] = StringVar()
    dessert_text[counter].set('0')
    dessert_box[counter]= Entry(dessert_panel, font=('Dosis',18, 'bold'), bd=1, 
                             width=6, state=DISABLED, textvariable=dessert_text[counter])
    dessert_box[counter].grid(row= counter, column = 1)
    counter+=1
    

# variables
food_cost_var = StringVar()
drink_cost_var = StringVar()
dessert_cost_var = StringVar()
subtotal = StringVar()
taxes = StringVar()
total = StringVar()

# food costs labels and fields
food_cost_label = Label(cost_panel, text='Food cost', font=('Dosis', 12, 'bold'),
                        bg= 'azure4',
                        fg= 'white')
food_cost_label.grid(row=0, column=0)
food_cost_text = Entry(cost_panel, bd=1, font=('Dosis', 12, 'bold'),
                        state='readonly', width=10, textvariable=food_cost_var)
food_cost_text.grid(row=0, column=1, padx=10)

# drink costs labels and fields
drink_cost_label = Label(cost_panel, bg='azure4',fg='white', text= 'Drink cost',
                            font=('Dosis', 12, 'bold'))
drink_cost_label.grid(row=1, column=0)
drink_cost_text = Entry(cost_panel, bd=1, font=('Dosis', 12, 'bold'),
                        state='readonly', width=10, textvariable=drink_cost_var)
drink_cost_text.grid(row=1, column=1, padx=10)

# dessert cost labels and fields
dessert_cost_label = Label(cost_panel, bg='azure4', fg='white',
                            font= ('Dosis', 12, 'bold'), text= 'Dessert cost')
dessert_cost_label.grid(row=2, column=0)
dessert_cost_text = Entry(cost_panel, bd=1, font=('Dosis', 12, 'bold'),
                            state='readonly', width=10, textvariable=dessert_cost_var)
dessert_cost_text.grid(row=2, column=1, padx=10)

# subtotal cost labels and fields
subtotal_cost_label = Label(cost_panel, bg='azure4',fg='white',
                            font=('Dosis',12,'bold'),text='Subtotal')
subtotal_cost_label.grid(row=0,column=2)
subtotal_cost_text = Entry(cost_panel, bd=1, font=('Dosis', 12, 'bold'),
                            state='readonly', width=10, textvariable=subtotal)
subtotal_cost_text.grid(row=0, column=3, padx=10)

#taxes labels and fields
taxes_label = Label(cost_panel, bg='azure4', fg='white',
                    font=('Dosis',12, 'bold'),text='Taxes')
taxes_label.grid(row=1, column=2)
taxes_text = Entry(cost_panel, bd=1, font=('Dosis', 12, 'bold'),
                    state='readonly',width=10, textvariable=taxes)
taxes_text.grid(row=1, column=3, padx=10)

# total labels and fields
total_label = Label(cost_panel, bg='azure4', fg='white',
                    font=('Dosis',12, 'bold'), text='Total')
total_label.grid(row=2,column=2)
total_text = Entry(cost_panel, bd=1, font=('Dosis', 12, 'bold'),
                    state='readonly',width=10, textvariable=total)
total_text.grid(row=2, column=3, padx=10)


# buttons
buttons =['Total','Invoice','Save', 'Reset']
buttons_created = []
column =0
for button in buttons:
    button = Button(buttons_panel, bd=1, bg='azure4',fg='white',
                    font=('Dosis', 14, 'bold'),text=button.title(),width=9)
    button.grid(row=0,column=column)
    buttons_created.append(button)
    column +=1
    
buttons_created[0].config(command=total_calculation)
buttons_created[1].config(command=create_invoice)
buttons_created[2].config(command=save_invoice)
buttons_created[3].config(command=reset_display)
# Invoice area
invoice_text = Text(invoice_panel, font=('Dosis',12,'bold'),bd=1, height=10,width=52)
invoice_text.grid(row=0,column=0)


# Calculator display
calculator_display = Entry(calculator_panel, bd=1, font=('Dosis',16,'bold'),
                            width=38)
calculator_display.grid(row=0,column=0,columnspan=4)

# Calculator buttons
calculator_buttons = ['1','2','3','+',
                        '4','5','6','-',
                        '7','8','9','*',
                        'CE','Delete','0','/']
stored_buttons= []
my_row=  1
my_column= 0

for button in calculator_buttons:
    button = Button(calculator_panel, bd=1, bg='azure4',fg='white',
                    font=('Dosis', 16, 'bold'), width=8, text=button.title())
    button.grid(row=my_row, column=my_column)
    stored_buttons.append(button)
    
    my_column +=1
    if my_column == 4:
        my_column = 0
        my_row +=1
    
stored_buttons[0].config(command=lambda: click_button('1'))
stored_buttons[1].config(command=lambda: click_button('2'))
stored_buttons[2].config(command=lambda: click_button('3'))
stored_buttons[3].config(command=lambda: click_button('+'))
stored_buttons[4].config(command=lambda: click_button('4'))
stored_buttons[5].config(command=lambda: click_button('5'))
stored_buttons[6].config(command=lambda: click_button('6'))
stored_buttons[7].config(command=lambda: click_button('-'))
stored_buttons[8].config(command=lambda: click_button('7'))
stored_buttons[9].config(command=lambda: click_button('8'))
stored_buttons[10].config(command=lambda: click_button('9'))
stored_buttons[11].config(command=lambda: click_button('*'))
stored_buttons[12].config(command=get_result)
stored_buttons[13].config(command=delete_all)
stored_buttons[14].config(command=lambda: click_button('0'))
stored_buttons[15].config(command=lambda: click_button('/'))

# prevent window from closing.
application.mainloop()