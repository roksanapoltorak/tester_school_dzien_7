""" """

class BankAccount():

    def __init__(self, balance):
        if balance <= 0:
            raise ValueError('Balance less than 0.')
        self.balance = balance

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError('You have too little money.')
        if amount < 0:
            raise ValueError('You can`t withdraw less than 0...')
        return self.balance - amount

    def deposite(self, amount):
        if amount < 0:
            raise ValueError('You cant`t deposit less than 0...')
        return self.balance + amount




account = BankAccount(1500)
print("Your balance after withdraw: ", account.withdraw(600))
print("Your balance after deposite: ", account.deposite(1800))

second = BankAccount(-500)
print("Your balance after withdraw: ", second.withdraw(100))
print("Your balance after deposite: ", second.deposite(1200))