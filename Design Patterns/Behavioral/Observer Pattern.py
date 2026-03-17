from typing import List


class Subject:
    def add_observer(self, observer):
        raise NotImplementedError()

    def remove_observer(self, observer):  # Fixed typo: removed 'er'
        raise NotImplementedError()

    def notify_observer(self):
        raise NotImplementedError()


class Stock(Subject):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.observers: List = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observer(self):
        for observer in self.observers:
            # This line requires all observers to have an .update() method
            observer.update(self)

    def set_price(self, new_price):
        if self.price != new_price:  # Optional: only notify if price actually changes
            self.price = new_price
            self.notify_observer()


class Observer:
    def update(self, stock):
        raise NotImplementedError("Subclasses must implement update()")


class Dashboard(Observer):
    def update(self, stock):
        print(f"📈 Dashboard updated: {stock.name} is now ${stock.price}")


class EmailAlert(Observer):
    def update(self, stock):  # Must be named 'update'
        self.send_email(stock)

    def send_email(self, stock):
        print(f"📧 Email Alert: {stock.name} is now ${stock.price}")


class SMSAlert(Observer):
    def update(self, stock):  # Must be named 'update'
        self.send_SMS(stock)

    def send_SMS(self, stock):
        print(f"📱 SMS Alert: {stock.name} is now ${stock.price}")


# --- Execution ---
apple_stock = Stock("iPhone", 150)
tesla_stock = Stock("Tesla", 200)

dashboard = Dashboard()
email_alerts = EmailAlert()
sms_alerts = SMSAlert()

apple_stock.add_observer(dashboard)
apple_stock.add_observer(email_alerts)
apple_stock.add_observer(sms_alerts)

tesla_stock.add_observer(dashboard)
tesla_stock.add_observer(email_alerts)

# This will now trigger all observers correctly
print("--- Updating Tesla Price ---")
tesla_stock.set_price(500)

print("\n--- Updating Apple Price ---")
apple_stock.set_price(300)
