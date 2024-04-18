import time
from queue import Queue
import uuid
from datetime import datetime
import random


class Passenger:
    def __init__(self):
        self.ticket_id = uuid.uuid4()
        self.start_date = None
        self.end_date = None

    def __str__(self):
        return f'Passenger - {self.ticket_id}, arrival date - {self.start_date}, departure date - {self.end_date}'


class Boat:
    def __init__(self, number, free_places):
        self.boat_number = number
        self.free_places = free_places

    def __str__(self):
        return f'Boat number: {self.boat_number}, number of free places - {self.free_places}'


class Pier:
    def __init__(self):
        self.queue = Queue()
        self.stat_queue = Queue()

    def add_passenger(self, passenger: Passenger):
        passenger.start_date = datetime.now()
        self.queue.put(passenger)

    def pick_up(self, boat: Boat):
        if self.queue.empty():
            raise IndexError("Pier is empty")
        i = boat.free_places
        while i > 0:
            if self.queue.empty():
                break
            passenger = self.queue.get()
            passenger.end_date = datetime.now()
            print(f"Passenger - {passenger.ticket_id} left the pier at {passenger.end_date} on {boat.boat_number}")
            self.stat_queue.put(passenger)
            i -= 1

    def print_queue(self):
        temp_queue = Queue()
        print("Original queue: ")
        while not self.queue.empty():
            passenger = self.queue.get()
            print("Passenger: " + str(passenger.ticket_id) + ": " + str(passenger.start_date), end='\n')
            temp_queue.put(passenger)
        print()
        self.queue = temp_queue

    def print_stat(self):
        temp_queue = Queue()
        print("Stat queue: ")
        while not self.stat_queue.empty():
            passenger = self.stat_queue.get()
            print(str(passenger.ticket_id) + ": " + "Arrival date: " + str(
                passenger.start_date) + "Departure date: " + str(passenger.end_date), end='\n')
            temp_queue.put(passenger)
        print()
        self.stat_queue = temp_queue


pier = Pier()
passengers_arrival = {"morning": 2, "evening": 1, "afternoon": 3, "night": 2}
boats_arrival = {"morning": 3, "evening": 2, "afternoon": 2, "night": 3}
time_of_day_duration = 6
try:
    for key, value in passengers_arrival.items():
        t = 0
        while t < time_of_day_duration:
            time.sleep(value)
            passenger = Passenger()
            pier.add_passenger(passenger)
            print(passenger)
            t += value

    for key, value in boats_arrival.items():
        t = 0
        while t < time_of_day_duration:
            time.sleep(value)
            boat = Boat(f"{random.randint(1111, 9999)}", random.randint(0, 2))
            print(boat)
            pier.pick_up(boat)
            t += value


except Exception as e:
    print("Message: ", e)

pier.print_queue()
pier.print_stat()
