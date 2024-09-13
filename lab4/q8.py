class Account:
    def __init__(self,acc_num,acc_bal,sec_code):
        self.__acc_num = acc_num
        self.__acc_bal = acc_bal
        self.__sec_code = sec_code
        
    def display_info(self):
        print("Account Number:", self.__acc_num)
        print("Account Balance:",self.__acc_bal)
        print("Security Code:", self.__sec_code)
        
hbl = Account("Muhammad",100000,3110)
hbl.display_info()
