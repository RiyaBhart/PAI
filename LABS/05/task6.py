class BankAccount:
    def __init__(self,accnum,balance,doo,name):
        self.accnum=accnum
        self.balance=balance
        self.doo=doo #date of opening
        self.name=name
    def withdraw(self):
        a=int(input("Enter amount to withdraw : "))
        if(a<=self.balance):
            self.balance=self.balance - a
            print("Withdrawal Succesfull! Remaining Balance",self.balance)
        if(a>self.balance):
            print("Not enough balance!")

    def deposit(self):
        a=int(input("Enter amount to deposit : "))
        self.balance+=a
        print("Amount Deposited! New Balance : ",self.balance)

    def checkbalance(self):
        print("Balance : ",self.balance)


b=BankAccount(101,90000,"10/08/2024","abc")
b.withdraw()
b.deposit()
b.checkbalance()
