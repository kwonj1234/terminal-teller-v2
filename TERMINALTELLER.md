## Week 1 Weekend Project: Terminal Teller

* Write an interactive terminal application simulating an automatic teller machine.

* It should be divided into model.py, view.py, controller.py as discussed in lecture.

### requirements

* The model will be a collection of bank accounts. Each account has, at a minimum, an account number, a pin, and a balance. These values should be saved in a permanent file.

    * What other data might a consumer bank account track?

* The application should support the following features:

    * An initial menu that allows a user to create an account, log in with an account # an pin, or exit

    * A main menu where a user can check their account balance, make a deposit, make a withdrawal, or exit

    * What other features do ATMs (or personal banking websites) have?

### example output:

```
Welcome to Terminal Teller!:

    1) create account
    2) log in
    3) quit

Your choice: 1

Account creation

    First Name : Nathan
    Last Name  : Smith
    PIN: 1234
    confirm PIN: 1234

account created, your account number is 432876.

Welcome to Terminal Teller!:

    1) create account
    2) log in
    3) quit

Your choice: 2

    Account number: 432876
    PIN: 1234


Hello, Nathan Smith (432876)

    1) Check balance
    2) Withdraw funds
    3) Deposit funds
    4) sign out

Your choice: 1

    Your balance is $0.00

Hello, Nathan Smith (432876)

    1) Check balance
    2) Withdraw funds
    3) Deposit funds
    4) sign out

Your choice: 3

    How much to deposit: $3.50

Hello, Nathan Smith (432876)

    1) Check balance
    2) Withdraw funds
    3) Deposit funds
    4) sign out

Your choice: 2

    How much to withdraw: $4.00

!! INSUFFICIENT FUNDS !!

Hello, Nathan Smith (432876)

    1) Check balance
    2) Withdraw funds
    3) Deposit funds
    4) sign out

Your choice: 2

    How much to withdraw: $2.00

Hello, Nathan Smith (432876)

    1) Check balance
    2) Withdraw funds
    3) Deposit funds
    4) sign out

Your choice: 1


    Your balance is $1.50

Hello, Nathan Smith (432876)

    1) Check balance
    2) Withdraw funds
    3) Deposit funds
    4) sign out

Your choice: 4


Welcome to Terminal Teller!:

    1) create account
    2) log in
    3) quit

Your choice: 3

    Goodbye!
```

### Suggestions for improvements:

    * Hide password entry:

    <https://stackoverflow.com/questions/9202224/getting-command-line-password-input-in-python>

    * Have the generated account number be a valid credit card # (see the Luhn algorithm assignment)

    * Users can have multiple accounts with labels like 'savings' or 'checking', users can transfer money between accounts

    * Users can transfer money to other users' accounts

    * encrypt your data storage format (good luck!)

        * There's a whole world of ways to do this, but maybe start looking here <https://github.com/isislovecruft/python-gnupg>. This is going to involve some research on your part.
