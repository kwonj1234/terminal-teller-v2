import model_test
import view_test
import random


def run():
    while True:
        choice = view_test.main_menu()
        if choice == "3": #Exit
            return
        elif choice == "1": #Create Account
            view_test.create_account()
            fname = view_test.first_name()
            lname = view_test.last_name()
            pin = view_test.choose_pin()
            initial = float(view_test.deposit_initial())
            data = model_test.Account.load()

            #Create new account then display
            #create random account number
            account_num = [str(random.randint(0,9)) for i in range(0,6)]
            account_num = "".join(account_num)
            while str(account_num) in list(data.keys()):
                account_num = [str(random.randint(0,9)) for i in range(0,6)]
                # for i in range(0,6):
                #     account_num.append(str(random.randint(0,9)))
                account_num = "".join(account_num)
            view_test.new_account(account_num)

            account_num = model_test.Account(fname, lname, account_num, pin, initial)
            model_test.Account.save(account_num)

        elif choice == "2":#log in
            account_num, pin = view_test.login()

            #Check if login info is correct
            if model_test.Account.validate(account_num, pin) == False:
                view_test.bad_login()

            #Login Menu - Check Balance, Withdraw, Deposit, Open Savings Account
            info = model_test.Account.login(account_num)
            account_num = model_test.Account(info["First Name"], info["Last Name"], \
                account_num, info["PIN"], info["checking account"], info["savings account"])
        
            view_test.welcome(account_num.account_num, account_num.fname, account_num.lname)
            while True:
                choice = view_test.login_menu()
                if choice == "1": #check balance
                    view_test.check_balance(info)

                elif choice == "2": #withdraw from checking
                    login_withdrawal(account_num, choice)  #see line 76

                elif choice == "3": #deposit into checking
                    login_deposit(account_num)    #see line 118

                elif choice == "4": #transfer funds
                    login_transfer(account_num)   #see line 131
                    
                elif choice == "5": #create savings
                    yesorno, deposit = view_test.create_savings()
                    model_test.Account.open_savings(account_num ,yesorno, float(deposit))
                    model_test.Account.save(account_num)
                    view_test.savings_opened(float(deposit))

                elif choice == "6": #sign out
                    view_test.signout()
                    return  

                else:
                    view_test.bad_input()  

        else:
            view_test.bad_input()

def login_withdrawal(account_num, choice):  #see line 52, withdraw money
    while True:
        choice = view_test.withdraw()
        #Quick withdrawal 
        if choice.isnumeric() == True:
            if int(choice) in [1,4]:
                #Quick withdrawal options
                list = [10,20,50,100]
                num = list[int(choice) - 1]
                new_balance = model_test.Account.withdraw(account_num, num)

                #Insufficient funds
                if new_balance == False:
                    view_test.insufficient_funds()
                    return

                view_test.withdraw_new_balance(num, new_balance)
                model_test.Account.save(account_num)

        #Withdraw custom amount
            elif choice == "5":
                num = view_test.withdraw_custom()

                #error handling
                if num.isnumeric() != True:
                    view_test.not_dollar()
                    return

                new_balance = model_test.Account.withdraw(account_num, float(num))
                
                #insufficient funds
                if new_balance == False:
                    view_test.insufficient_funds()
                    return
                    
                view_test.withdraw_new_balance(num, new_balance)
                model_test.Account.save(account_num)
            else:
                view_test.bad_input()     
        else:
            view_test.bad_input()

def login_deposit(account_num):   #see line 55
    num = view_test.deposit()

    #error handling
    while num.isnumeric == False:
        view_test.not_dollar()
        num = view_test.deposit()

    num = float(num)
    new_balance = model_test.Account.deposit(account_num,num)
    view_test.deposit_new_balance(num, new_balance)
    model_test.Account.save(account_num)

def login_transfer(account_num):   #see line 57

    from_account = view_test.transfer_from_account()
    #error handling for non-account inputs
    while from_account != "checking" and from_account != "savings":
        view_test.bad_transfer()
        from_account = view_test.transfer_from_account()

    to_account = view_test.transfer_to_account()
    while to_account != "checking" and to_account != "savings":
        view_test.bad_transfer()
        to_account = view_test.transfer_to_account()

    #error handling for non-numeric inputs
    amount = view_test.transfer_amount()
    while amount.isnumeric() == False:
        view_test.not_dollar()
        amount = view_test.transfer_amount()
    
    #convert amount value from string to float
    amount = float(amount)

    #error handling for insufficient funds
    if amount > account_num.transfer_funds[from_account]:
        view_test.insufficient_funds()
        return

    from_balance, to_balance = model_test.Account.transfer(account_num, \
        from_account, to_account, amount)
    view_test.transfer_new_balance(from_balance, to_balance, from_account, to_account)

run()