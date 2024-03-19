from tkinter import *

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
                  font=('Dosis', 58), bg='burlywood', width=25)

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
                       onvalue=1, offvalue=0, variable=food_variables[counter])
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
                       onvalue=1, offvalue=0, variable=drink_variables[counter])
    drink.grid(row=counter, column=0,sticky=W)
    
    # create input boxes
    drink_box.append('')
    drink_text.append('')
    drink_text[counter] = StringVar()
    drink_text[counter].set('0')
    drink_box[counter]= Entry(drink_panel, font=('Dosis',18, 'bold'), bd=1, 
                             width=6, state=DISABLED, textvariable=drink_text[counter])
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
                       onvalue=1, offvalue=0, variable=dessert_variables[counter])
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
    column =0
    for button in buttons:
        button = Button(buttons_panel, bd=1, bg='azure4',fg='white',
                        font=('Dosis', 14, 'bold'),text=button.title(),width=9)
        button.grid(row=0,column=column)
        column +=1
        
    # Invoice area
    invoice_text = Text(invoice_panel, font=('Dosis',12,'bold'),bd=1, height=10,width=52)
    invoice_text.grid(row=0,column=0)
        


# prevent window from closing.
application.mainloop()