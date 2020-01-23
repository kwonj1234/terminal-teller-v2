import json
import random

class Account:
    
    def __init__(self, fname, lname, account_num, pin, checking, savings = "None"):
        self.fname = fname 
        self.lname = lname
        self.account_num = account_num
        self.pin = pin
        self.checking = checking
        self.savings = savings
        self.transfer_funds = {"checking" : self.checking, "savings": self.savings}

    @classmethod
    def load(cls):
        with open('data.json', 'r') as f_object:
            data = json.load(f_object)
        return data

    def save(self):
        data = self.load()
        data[self.account_num] = {"First Name": self.fname, "Last Name": self.lname, \
            "PIN": self.pin, "checking account": self.checking, "savings account": self.savings}

        with open('data.json', 'w') as f_object:
            json.dump(data, f_object, indent=2)

    @classmethod
    def validate(cls,login_account_num, login_pin):
        data = cls.load()
        #Check for account number and pin in data
        if login_account_num not in list(data.keys()) or \
            login_pin != data[login_account_num]["PIN"]:
            return False
        return True

    @classmethod
    def login(cls,account_num):
        data = cls.load()
        info = data[account_num]
        return info

    def withdraw(self,num):
        if self.checking < num:
            return False
        self.checking -= num
        return self.checking       

    def deposit(self,num):
        if num <= 0:
            return False
        self.checking += num
        return self.checking

    def transfer(self, from_account, to_account, amount):
        self.transfer_funds[from_account] -= amount
        self.transfer_funds[to_account] += amount
        #TODO Show error code for when person does not have 2 accounts.

        return self.transfer_funds[from_account], self.transfer_funds[to_account]

    def open_savings(self, yesorno, num):
        if yesorno == 'y':
            self.checking -= num
            self.saving = num
        self.saving = num


