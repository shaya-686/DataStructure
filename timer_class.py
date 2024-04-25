import json
import time


class Timer:
    timer_file = 'timer.json'

    def __init__(self):
        self.start_time = None
        self.stop_time = None

    def start(self):
        if not self.start_time:
            self.start_time = time.time()
        elif not self.stop_time:
            print("Timer is already started")
        else:
            self.start_time = self.stop_time

    def save(self):
        time.sleep(1)
        self.stop_time = time.time()
        dct = {"start_time": self.start_time, "stop_time": self.stop_time}
        with open(self.timer_file, 'w') as file:
            json.dump(dct, file, indent=4)

    def load(self):
        with open(self.timer_file, 'r') as file:
            dct = json.load(file)
            self.start_time = dct["start_time"]
            self.stop_time = dct["stop_time"]

    def print_info(self):
        print(f"Timer: {self.start_time}, {self.stop_time}")


timer = Timer()
timer.start()
timer.print_info()
timer.save()
timer.print_info()
timer.load()
timer.print_info()
timer.start()
timer.print_info()
