accounts = dict()

class Person:
    def __init__(self,fname,lname):
        self.fname= fname
        self.lname = lname
class Customer(Person):
    def __init__(self,fname, lname, account_no, balance=0):
        super().__init__(fname,lname)
        self.account_no = account_no
        self.balance = balance
    def __str__(self):
        return f"Customer: {self.fname} {self.lname}\nAccount Balance {self.account_no}: ${self.balance}"
    def acc_print(self):
        print(f'Hello {self.fname} {self.lname}, Your account no. {self.account_no} has balance ${self.balance}')
    def deposit(self, amount):
        self.balance += amount
        print(f'Your deposit of ${amount} is successful. Available balance: ${self.balance}')
    def withdraw(self, amount):
        if self.balance <amount:
            print("you don't have sufficient balance.")
            return
        self.balance -= amount
        print(f"Your withdrawl of {amount} is successful. Available balance: ${self.balance}")
def code_to_choose():
    print('1. Deposit \n2. Withdraw \n3. Exit')
    n = int(input('Choose from options: '))
    return n
def create_customer():
    fname = input('Enter your first name: ')
    lname = input('Enter your last name: ')
    account_no = input('Enter your account number: ')
    while account_no in accounts:
        print('This account already exist. Please enter other account number.')
        account_no = input('Enter your account number: ')
    cust = Customer(fname,lname,account_no)
    accounts[account_no] = cust
    print(f'Account {cust.account_no} is created successfully.')

def start():
    create_or_login = int(input('1. Create account \n2. Login to account'))
    if create_or_login ==1:
        create_customer()
    acc_no = input('Enter your account number: ')
    while acc_no not in accounts:
        print('Entered accoutn number does not exist.')
        acc_no = input('Enter your account number: ')
    n = 0
    while n!=3:
        n = code_to_choose()
        if n ==1:
            amount = float(input('Enter the amount you want to deposit: '))
            while amount<0:
                print('amount can not be negetive.')
                amount = float(input('Enter the amount you want to deposit: '))
            accounts[acc_no].deposit(amount)
        elif n ==2:
            amount = float(input('Enter the amount you want to withdraw: '))
            while amount<0:
                print('amount can not be negetive.')
                amount = float(input('Enter the amount you want to withdraw: '))
            accounts[acc_no].withdraw(amount)
    return 'You logged off!'
        
start()