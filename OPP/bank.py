# Create a class BankAccount with methods for deposit, withdrawal, and balance inquiry.


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def balanceInquiry(self):
        return self.balance


b = BankAccount(1000)
b.deposit(500)
b.withdraw(200)
print(b.balanceInquiry())  # 1300
b.withdraw(2000)  # Insufficient funds
print(b.balanceInquiry())  # 1300
b.deposit(1000)