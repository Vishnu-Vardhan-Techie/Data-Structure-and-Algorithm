class BankService:
    def make_payment(self, amount):
        print(f"Processing Payment of ${amount} through BankService")


class PaymentService:
    def pay(self, amount):
        pass


class BankServiceAdapter(PaymentService):
    def __init__(self, bank_service: BankService):
        self.bank_service = bank_service

    def pay(self, amount):
        self.bank_service.make_payment(amount)


def process_payment(payment_service, amount):
    payment_service.pay(amount)


bank_service_adapter = BankServiceAdapter(BankService())
process_payment(bank_service_adapter, 100)
