from queue import Queue


class Restaurant:
    def __init__(self):
        self.queue = Queue()

    def add_order(self, order):
        self.queue.put(order)

    def complete_order(self):
        if self.queue.empty():
            raise IndexError("No orders in queue")
        order = self.queue.get()
        print(f"Order {order} completed!")

    def print_orders(self):
        temp_queue = Queue()
        while not self.queue.empty():
            order = self.queue.get()
            print(order, end=' <- ')
            temp_queue.put(order)
        print()
        self.queue = temp_queue

    def count_remaing_orders(self):
        return self.queue.qsize()

    def is_empty(self):
        return self.queue.empty()


restaurant = Restaurant()
restaurant.add_order("111")
restaurant.add_order("222")
restaurant.add_order("333")
restaurant.print_orders()
print("Orders remains: ", restaurant.count_remaing_orders())
restaurant.complete_order()
restaurant.complete_order()
restaurant.complete_order()
print("Empty: ", restaurant.is_empty())
