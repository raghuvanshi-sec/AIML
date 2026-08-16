class BankAccount:
    def __init__(self,name,balance):
        self.name = name #public
        self.__balance = balance #private
    def get_balance(self): #getter
        return self.__balance


    def set_balnce(self,new_balance):  #setter
        self.__balance = new_balance

acc1 = BankAccount("Rahul Kumar",50000)

acc1.set_balnce(60000)
print(acc1.name,acc1._BankAccount__balance)   
