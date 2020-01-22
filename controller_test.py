import model_test
import view

def run():
    while True:
        choice = view.main_menu()
        if choice == "3": #Exit
            return
        elif choice == "1": #Create Account
            view.create_account()
            fname = view.first_name()
            lname = view.last_name()
            pin = view.choose_pin()
            initial = float(view.deposit_initial())
            #Create new account then display
            user = model_test.Create_Account(fname,lname,pin,initial)
            model_test.Create_Account.create(user)
            view.new_account(model_test.Create_Account.create(user))
            
        elif choice == "2":#log in
            account_num, pin = view.login()
            #Check if login info is correct
            if model_test.Accounts.login(account_num, pin) == False:
                view.bad_login()
            else:
                #Login Menu - Check Balance, Withdraw, Deposit, Open Savings Account
                info = model_test.Accounts.login(account_num, pin)
                view.welcome(account_num, info)
                while True:
                    choice = view.login_menu()
                    if choice == "1":
                        view.check_balance(info)
                    elif choice == "2":
                        login_withdrawal(account_num)  #see line 58
                    elif choice == "3":
                        num = view.deposit()
                        new_balance = model.deposit(num,account_num)
                        view.deposit_new_balance(num, new_balance)
                    elif choice == "4":
                        from_account, to_account, amount = view.transfer()

                        #Add " account" at the end of the string so it matches the key in the dictionary
                        from_account = from_account + " account"
                        to_account = to_account + " account"
                        #convert amount value from string to float
                        amount = float(amount)

                        info = model.transfer(from_account, to_account, amount, account_num)
                        view.transfer_new_balance(info, from_account, to_account)
                    elif choice == "5":
                        yesorno, deposit = view.create_savings()
                        model.open_savings(yesorno, float(deposit), account_num)
                        view.savings_opened(float(deposit))
                    elif choice == "6":
                        view.signout()
                        return                 
        else:
            view.bad_input()

def login_withdrawal(account_num):  #see line 32
    while True:
        choice = view.withdraw()
        #Quick withdrawal 
        if int(choice) in [1,4]:
            #Quick withdrawal options
            list = [10,20,50,100]
            num = list[int(choice) - 1]
            new_balance = model_test.Accounts.withdrawal(num)
            
            #Insufficient funds
            if new_balance == False:
                view.insufficient_funds()
            view.withdraw_new_balance(num, new_balance)

    #Withdraw custom amount
        elif choice == "5":
            num = view.withdraw_custom()
            new_balance = model.withdrawal(num, account_num)
            if new_balance == False:
                view.insufficient_funds()
                return
            view.withdraw_new_balance(num, new_balance)
            return
        else: 
            view.bad_input

run()