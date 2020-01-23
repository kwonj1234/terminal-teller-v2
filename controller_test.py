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
            else:
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
                        login_withdrawal(account_num)  #see line 76

                    elif choice == "3": #deposit into checking
                        num = view_test.deposit()
                        new_balance = model_test.Account.deposit(account_num,num)
                        view_test.deposit_new_balance(num, new_balance)
                        model_test.Account.save(account_num)

                    elif choice == "4": #transfer funds
                        from_account, to_account, amount = view_test.transfer()

                        #Add " account" at the end of the string so it matches the key in the dictionary
                        from_account = from_account + " account"
                        to_account = to_account + " account"
                        #convert amount value from string to float
                        amount = float(amount)

                        info = model_test.Account.transfer(account_num, from_account, to_account, amount)
                        view_test.transfer_new_balance(info, from_account, to_account)
                    elif choice == "5":
                        yesorno, deposit = view.create_savings()
                        model.open_savings(yesorno, float(deposit), account_num)
                        view.savings_opened(float(deposit))
                    elif choice == "6":
                        view.signout()
                        return                 
        else:
            view_test.bad_input()

def login_withdrawal(account_num):  #see line 50
    while True:
        choice = view_test.withdraw()
        #Quick withdrawal 
        if int(choice) in [1,4]:
            #Quick withdrawal options
            list = [10,20,50,100]
            num = list[int(choice) - 1]
            new_balance = model_test.Account.withdraw(account_num, num)
            #Insufficient funds
            if new_balance == False:
                view_test.insufficient_funds()
            view_test.withdraw_new_balance(num, new_balance)
            return

    #Withdraw custom amount
        elif choice == "5":
            num = view_test.withdraw_custom()
            new_balance = model_test.Account.withdraw(account_num, num)
            if new_balance == False:
                view_test.insufficient_funds()
                return
            view_test.withdraw_new_balance(num, new_balance)
            model_test.Account.save(account_num)
            return
        else: 
            view_test.bad_input

run()