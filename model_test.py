import json
import random

def load():
    with open('data.json', 'r') as f_object:
        data = json.load(f_object)
    return data

def save(data):
    with open('data.json', 'w') as f_object:
        json.dump(data, f_object, indent=2)

class Create_Account:
    data = load()

    def __init__(self, fname, lname, pin, initial):
        self.fname = fname
        self.lname = lname
        self.pin = pin
        self.initial = initial

    def create(self):
        account_num = [str(random.randint(0,9)) for i in range(0,6)]
        # for i in range(0,6):
        #     account_num.append(str(random.randint(0,9)))
        account_num = "".join(account_num)
        self.data[account_num] = {"First Name" : self.fname, "Last Name" : self.lname, "PIN" : self.pin, "checking account" : self.initial}
        save(self.data)
        return account_num

class Accounts:

    def __init__(self, fname, lname, account_num, pin, checking, savings):
        self.fname = fname
        self.lname = lname
        self.account_num = account_num
        self.pin = pin
        self.checking = checking
        self.savings = savings
    
    @classmethod
    def load(cls):
        with open('data.json', 'r') as f_object:
            data = json.load(f_object)
        return data

    @classmethod
    def login(cls, account_num, pin):
        data = Accounts.load()

        #Check for account number and pin in data
        if account_num not in list(data.keys()) or \
            pin != data[account_num]["PIN"]:
            return False
        #Return only user relevant data
        info = data[account_num]
        account_num = Accounts(info["First Name"], info["Last Name"], \
            account_num, pin, info["checking account"], info["savings account"])
        print(self.fname, self.lname, self.account_num, self.pin, \
            self.checking, self.savings)
        return info

    def save(self, data):
        with open('data.json', 'w') as f_object:
            json.dump(data, f_object, indent=2)

    def withdrawal(self, num):
        data = Accounts.load()
        if self.checking < num:
            return False
        self.checking -= num
        data[self.account_num]["checking account"] = self.checking
        self.save(data)
        return self.checking #new account balance

    