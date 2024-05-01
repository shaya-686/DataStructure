import json


class Sales:
    orders_file = "orders.json"

    def __init__(self):
        self.orders = []

    def sales_statistic(self):
        with open(self.orders_file, 'r') as file:
            self.orders = json.load(file)
        print("The number of orders: ", len(self.orders))
        print("Total amount: ", sum([self.orders[i]["amount"] for i in range(len(self.orders))]))
        print(self.orders)


sales = Sales()
sales.sales_statistic()
