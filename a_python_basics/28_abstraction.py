# abstraction done at the design level
# abstract certain methods
# All derived classes must adhere to the interface
# python does not support abstract by default
# need abc module
from abc import ABC, abstractmethod

# abstract class


class Vehicle(ABC):
    def __init__(self):
        self.no_of_tyres = 2

    @abstractmethod  # you should have at least one abstractmethod
    def start(self):
        pass

# subclass must implement all abstract method or becomes abstact class


class Bike(Vehicle):
    def __init__(self):
        self.no_of_tyres = 2

    def start(self):  # must implement abstract methods
        print("start with kick")


class Scooter(Vehicle):
    def __init__(self):
        self.no_of_tyres = 2

    def start(self):  # must implement abstract methods
        print("self start")


class Car(Vehicle):
    def __init__(self):
        self.no_of_tyres = 2

    def start(self):  # must implement abstract methods
        print("start with key")


# can not instantiate abtract class
# v = Vehicle()


class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass


class CreditCardPayment(Payment):
    def pay(self):
        return "Processing credit card payment..."


class PayPalPayment(Payment):
    def pay(self):
        return "Processing PayPal payment..."


class CryptoPayment(Payment):
    def pay(self):
        return "Processing crypto payment..."


# User doesn't need to know details, just calls pay()
payment = CreditCardPayment()
print(payment.pay())  # ✅ Processing credit card payment!

"""
🟢 Benefits

✅ Hides different payment processing details.
✅ User only interacts with pay() method, regardless of payment type.
✅ Easier to extend (add new payment methods later).
"""
