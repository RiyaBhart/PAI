class Account:
    def setaccno(self, accno):
        self.__accno = accno

    def getaccno(self):
        return self.__accno

    def setaccbal(self, accbal):
        self.__accbal = accbal

    def getaccbal(self):
        return self.__accbal

    def setasc(self, sc):
        self.__sc = sc

    def getsc(self):
        return self.__sc

    def printdata(self):
        print("Account Number:", self.getaccno())
        print("Account Balance:", self.getaccbal())
        print("Security Code:", self.getsc())

A = Account()
A.setaccbal(2000)
A.setaccno(123)
A.setasc("0000")
A.printdata()
