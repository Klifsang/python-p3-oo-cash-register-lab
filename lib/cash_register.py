#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.prices = []
        self.last_count = 0

    def add_item(self, title, price, quantity=1):
        self.last_count = quantity
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.prices.extend([price] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            self.total -= self.total * (self.discount / 100)
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.prices:
            self.total -= self.prices[-1] * self.last_count
            self.prices = self.prices[:-self.last_count]
            self.items = self.items[:-self.last_count]
