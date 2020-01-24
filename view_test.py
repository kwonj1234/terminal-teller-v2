from getpass import getpass

def main_menu():
    print()
    print("Welcome to Terminal Teller\n")
    print("What would you like to do today")
    print("1) Create Account")
    print("2) Log In")
    print("3) Quit")
    return input()

#Create Account
def create_account():
    print("\nThank you for choosing to open an account with ByteBank!")

def first_name():
    print("Please enter your first name: ")
    return input()

def last_name():
    print("\nPlease enter your last name: ")
    return input()

def choose_pin():
    print("\nPlease enter a four digit PIN")
    print("(Make sure your PIN is unique to you and easy to remember)")
    return getpass()

def deposit_initial():
    print("\nPlease deposit at least $0.01 to open your account")
    return input()

def new_account(account_num):
    print("\nYou've opened an account with ByteBank!")
    print(f"Your Account Number is : {account_num}")

#Login
def login():
    print("\nPlease enter your Account Number and PIN")
    return (getpass("\nAccount Number: ") , getpass("\nPIN: "))

def welcome(account_num, fname, lname):
    print(f'\nHello {fname} {lname}')
    print(f'Account Number: {account_num}')

def login_menu():
    print('\nWhat would you like to do today?')
    print('1) Check Balance')
    print('2) Withdraw Funds')
    print('3) Deposit Funds')
    print('4) Transfer Funds')
    print('5) Open Savings Account')
    print('6) Sign Out')
    return input()

#Check Balance
def check_balance(info):
    print('\nYour Checking Account has a balance of : $' + "{:.2f}".format(info["checking account"]))
    if info["savings account"] != "None":
        print('Your Savings Account has a balance of : $' + "{:.2f}".format(info["savings account"]))

#Withdraw funds
def withdraw():
    print('\nHow much would you like to withdraw?')
    print('1) $10')
    print('2) $20')
    print('3) $50')
    print('4) $100')
    print('5) Enter Custom Amount')
    return input()

def withdraw_custom():
    print('\nEnter Custom Amount')
    return input()

def withdraw_new_balance(num, new_balance):
    print('\nYou withdrew : $' + "{:.2f}".format(num))
    print('Your new Checking Account balance is : $' + "{:.2f}".format(new_balance))

#Deposit into your account
def deposit():
    print('\nHow much would you like to deposit?')
    return input()

def deposit_new_balance(num, new_balance):
    print('\nYou deposited : $' + "{:.2f}".format(num))
    print('Your Checking Account balance is : $' + "{:.2f}".format(new_balance))

#Transfer money from one account to the other
def transfer_from_account():
    from_account = input('\nWhich account would you like to transfer funds from?\n')
    return from_account

def transfer_to_account():
    to_account = input('\nWhich account would you like to transfer funds to?\n')
    return to_account

def transfer_amount():
    amount = input('\nHow much would you like to transfer?\n')
    return amount

def transfer_new_balance(from_balance, to_balance, from_account, to_account):
    print('\nYour new account balance is')
    print(f'{from_account} : $' + "{:.2f}".format(from_balance))
    print(f'{to_account} : $' + "{:.2f}".format(to_balance))

#Create a Savings Account
def create_savings():
    print('\nMinimum deposit to open a Savings Account is $500')
    yesorno = input('Would you like to transfer money from your Checkings Account (y/n)?')
    deposit = input('How much would you like to deposit? ')
    return yesorno, deposit

def savings_opened(num):
    print('\nCongratulations you have opened a Savings Account')
    print('Your currect Savings Account balance is: $' + "{:.2f}".format(num))
    
#Signing Out
def signout():
    print('\nThank you for visiting Byte Bank\n')

#Bad input responses
def bad_login():
    print("Invalid Account Number or Pin")

def insufficient_funds():
    print("Insufficient funds")

def bad_input():
    print("Invalid Input")

def bad_transfer():
    print("Please choose either checking or savings")

def not_dollar():
    print("Please enter a dollar value")
