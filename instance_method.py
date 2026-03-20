class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}'s balance: ${self._balance}")
        else:
            print("Deposit amount must be positive")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5

account1 = BankAccount("Theo", 500)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))