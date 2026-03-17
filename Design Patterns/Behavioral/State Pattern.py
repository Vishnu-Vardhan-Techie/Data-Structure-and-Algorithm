from abc import ABC, abstractmethod


class VendingMachine:
    def __init__(self):
        self.snacks = 5
        self.ideal_state = IdealState()
        self.has_money_state = HasMoneyState()
        self.out_of_stock = OutOfStock()
        self.state = self.ideal_state

    def handle(self, action):
        self.state.handle(self, action)


class State(ABC):
    @abstractmethod
    def handle(self, action):
        pass


class IdealState(State):
    def handle(self, machine: VendingMachine, action: str):
        if action == "insert_coin":
            machine.state = machine.has_money_state
            print("Coin Inserted. You can select a snack")
        else:
            print("Insert a coin first")


class HasMoneyState(State):
    def handle(self, machine: VendingMachine, action: str):
        if action == "select_snack":
            if machine.snacks > 0:
                machine.snacks -= 1
                machine.state = machine.ideal_state
                print("Dispensing your Snack. Thank You!")
            else:
                machine.state = machine.out_of_stock
                print("Out of Stock! Refund instantiated.")
        else:
            print("Please select a Snack.")


class OutOfStock(State):
    def handle(self, machine: VendingMachine, action: str):
        print("Sorry! No stock left. Refund your coin.")


machine = VendingMachine()
machine.handle("insert_coin")
machine.handle("select_snack")
