class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.__balance += amount
        print(f"Deposited Rs. {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrawn Rs. {amount}")

    def get_balance(self):
        return self.__balance

    def display_account(self):
        print(f"Account holder: {self.owner}")
        print(f"Current balance: Rs. {self.__balance}")


if __name__ == "__main__":
    account = BankAccount("Mohib", 10000)

    account.deposit(2500)
    account.withdraw(3000)
    account.withdraw(20000)

    account.display_account()
