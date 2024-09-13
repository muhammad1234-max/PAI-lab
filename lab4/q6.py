class bankAccount:
    def __init__(self,acc_num,date_opening,name,balance=0):
        self.acc_num = acc_num
        self.balance = balance
        self.date_opening = date_opening
        self.name = name
        
    def deposit(self, amount):
        self.balance += amount
        print(f"the ammount {amount} was deposited\nnew amount is {self.balance}")
        
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"the amount {amount} was withdrawn")
        else:
            print("Insufficient balance")
            
    def check_balance(self):
        print(f"account number {self.acc_num} has balance {self.balance}")
        

hbl = bankAccount(234,"31-10-2003","Muhammad",1000000000)

hbl.deposit(5000000)
hbl.withdraw(250000)
hbl.check_balance()
