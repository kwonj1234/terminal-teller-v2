import json
import random

#TODO Do not exit until someone selects exit

def load():
    with open('data.json', 'r') as f_object:
        data = json.load(f_object)
    return data

def save(data):
    with open('data.json', 'w') as f_object:
        json.dump(data, f_object, indent=2)

def create_account(fname, lname, pin, initial):
    data = load()
    #Create random 6 digit account number
    #Make sure you do not create a repeat of what is already in the data
    account_num = [str(random.randint(0,9)) for i in range(0,6)]
    while str(account_num) in list(data.keys()):
        account_num = [str(random.randint(0,9)) for i in range(0,6)]
        # for i in range(0,6):
        #     account_num.append(str(random.randint(0,9)))
        account_num = "".join(account_num)

    data[account_num] = {"First Name" : fname, "Last Name" : lname, "PIN" : pin, "checking account" : initial}
        # TODO add error handling for non names inputted where names are supposed to be,
        # pins that are not numbers or are not 4 numbers in length
        # account balance that don't make sense
    save(data)
    return account_num

def login(account_num, pin):
    data = load()

    #Check for account number and pin in data
    if account_num not in list(data.keys()) or \
        pin != data[account_num]["PIN"]:
        return False
    #Return only user relevant data
    info = data[account_num]
    return info

def withdrawal(num, account_num):
    data = load()
    if data[account_num]["checking account"] < num:
        return False
    data[account_num]["checking account"] -= num
    save(data)
    return data[account_num]["checking account"] #new account balance

def deposit(num, account_num):
    data = load()
    #return false for negative deposit value
    if num <= 0:
        return False
    
    data[account_num]["checking account"] += num
    save(data)
    return data[account_num]["checking account"] #new account balance

#Transfer money from one account to the other
def transfer(from_account, to_account, amount, account_num):
    data = load()
    data[account_num][from_account] -= amount
    data[account_num][to_account] += amount
    #TODO Show error code for when person does not have 2 accounts.
    save(data)
    return data[account_num]

#Create a savings account
def open_savings(yesorno, num, account_num):
    data = load()
    if yesorno == 'y':
        data[account_num]["checking account"] -= num
        data[account_num]['savings account'] = num
    data[account_num]['savings account'] = num
    save(data)
