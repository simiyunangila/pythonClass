class Account:
    bank_name = "Equity"
    
    def __init__(self, account_name, account_number, balance):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance

    def new_balance(self, deposit):
        self.deposit = deposit
        new = self.balance + self.deposit
        return f"Hello {self.account_name} of account {self.account_number} you deposited ksh{self.deposit} and your new account balance  is ksh{new}."

    def rem_balance(self, withdraw):
        self.withdraw = withdraw
        if self.balance > self.withdraw:
            self.balance -= self.withdraw
            print(f"Withdrawal of {self.withdraw} is successful and your new account balance is {self.balance}")
            return self.balance
        else:
            print(f"You have insufficient balance in your account please top up to ksh{self.balance} to complete the transaction")

    def account_details(self):
        return f"Hello {self.account_name} of account {self.account_number} you have a balance of ksh{self.balance} in your account."

my_account = Account("Rebecca", 35674829, 1000)
print(my_account.rem_balance(500))
print(my_account.account_details())
print(my_account.new_balance(3000))
