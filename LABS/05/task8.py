class Account:
    def __init__(self, accnum, balance, scode):
        self.__account_no = accnum
        self.__account_bal = balance
        self.__security_code = scode

    def set_data(self, accnum, balance, scode):
        self.__account_no = accnum
        self.__account_bal = balance
        self.__security_code = scode

    def print_data(self):
        print(f"Account Number: {self.__account_no}")
        print(f"Account Balance: {self.__account_bal}")
        print(f"Security Code: {self.__security_code}")


account = Account(123, 100000, '080')
account.print_data()
