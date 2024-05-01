import json
import uuid
from datetime import datetime


class Order:

    def __init__(self, amount, product):
        self.uuid = uuid.uuid4()
        self.create_date = datetime.now()
        self.amount = amount
        self.product = product

    def __str__(self):
        return (f"Order: uuid - {self.uuid}, "
                f"create date - {self.create_date}, "
                f"amount - {self.amount}, "
                f"product - {self.product}")


class Shop:
    orders_file = "orders.json"

    def __init__(self):
        self.orders = []

    def add_order(self, order: Order):
        self.orders.append(order)

    def export_to_json(self):
        data = []
        with open(self.orders_file, 'w') as file:
            for order in self.orders:
                record = {"uuid": str(order.uuid),
                          "create_date": str(order.create_date),
                          "amount": order.amount,
                          "product": order.product}
                data.append(record)
            json.dump(data, file, indent=4)


first_order = Order(100, "123456")
second_order = Order(300, "999999")
third_order = Order(500, "7624275")

shop = Shop()
shop.add_order(first_order)
shop.add_order(second_order)
shop.add_order(third_order)

shop.export_to_json()
