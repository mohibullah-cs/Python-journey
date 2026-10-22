from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def payment_details(self):
        pass


class CreditCardPayment(PaymentMethod):

    def __init__(self, card_holder):
        self.card_holder = card_holder

    def pay(self, amount):
        print(f"Processing card payment of Rs. {amount}")

    def payment_details(self):
        print("Payment method: Credit Card")
        print(f"Card holder: {self.card_holder}")


class BankTransfer(PaymentMethod):

    def __init__(self, account_name):
        self.account_name = account_name

    def pay(self, amount):
        print(f"Transferring Rs. {amount} through bank")

    def payment_details(self):
        print("Payment method: Bank Transfer")
        print(f"Account name: {self.account_name}")


def process_payment(payment_method, amount):
    payment_method.payment_details()
    payment_method.pay(amount)
    print("-" * 30)


if __name__ == "__main__":
    card = CreditCardPayment("Ali")
    bank = BankTransfer("Sara")

    process_payment(card, 5000)
    process_payment(bank, 8000)
