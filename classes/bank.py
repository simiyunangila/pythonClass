class Account:
    bank_name="Equity"
    def __init__(self,account_name,account_number,balance):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance

    def new_balance(self,deposit):
        self.deposit=deposit
        new=self.balance+self.deposit
        return new

    def rem_balance(self,withdraw):
        self.withdraw=withdraw
        if self.balance > self.withdraw:
            print(f"widthrawal of {self.withdraw} approved" )
        else:
            print("insufficient balance")

    def account_details(self):
        return f"{self.account_name} of account {self.account_number} has {self.balance}"        

