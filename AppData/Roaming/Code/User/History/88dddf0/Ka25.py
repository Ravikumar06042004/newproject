class ATRI:
    def _init_(self):
        self.balance = 0.0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount


class ATMController:
    def _init_(self):
        self.account = ATRI()

    def display_balance(self):
        return f"Current Balance: ${self.account.check_balance():.2f}"

    def perform_deposit(self, amount):
        self.account.deposit(amount)
        return self.display_balance()

    def perform_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self.display_balance()