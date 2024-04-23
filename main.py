import pickle
import gzip
import random


class Number:

    def __init__(self):
        self.numbers = [random.randint(1111, 9999) for _ in range(100)]

    def add_number(self, number, file):
        if not isinstance(number, int):
            raise ValueError("Number should be int")
        new_numbers_list = self.read_numbers(file)
        self.numbers = new_numbers_list
        self.numbers.append(number)
        self.write_numbers(file)

    def remove_number(self, number, file):
        if not isinstance(number, int):
            raise ValueError("Number should be int")
        if number in self.numbers:
            self.numbers.remove(number)
            self.write_numbers(file)
        else:
            raise ValueError("Number not found")

    def write_numbers(self, file):
        with open(file, 'wb') as pickle_file:
            pickle.dump(self.numbers, pickle_file)

    def write_gzip_numbers(self, file):
        with gzip.open(file, 'wb') as gzip_file:
            serialized = pickle.dumps(self.numbers)
            gzip_file.write(serialized)

    def read_numbers(self, file):
        with open(file, 'rb') as pickle_file:
            read_numbers = pickle.load(pickle_file)
        print(f"Origin list = {self.numbers} \nPickle list = {read_numbers}")
        return read_numbers

    def read_gzip_numbers(self, file):
        with gzip.open(file, 'rb') as gzip_file:
            serialized = gzip_file.read()
            read_numbers = pickle.loads(serialized)
        print(f"Origin list = {self.numbers} \nPickle list = {read_numbers}")
        return read_numbers


num = Number()

print("Numbers from pickle: ")
num.write_numbers('numbers.pickle')
num.read_numbers('numbers.pickle')

print("Updated list: ")
num.add_number(9999999, 'numbers.pickle')
num.read_numbers('numbers.pickle')

print("Numbers from gzip: ")
num.write_gzip_numbers('numbers.gz')
num.read_gzip_numbers('numbers.gz')

print("Numbers after remove: ")
num.remove_number(9999999, 'numbers.pickle')
num.read_numbers('numbers.pickle')


class Login:

    def __init__(self):
        self.logins = {"test": "12345", "test1": "123dd"}

    def add_login(self, login, password, file):
        new_login_dict = self.read_login(file)
        self.logins = new_login_dict
        self.logins[login] = password
        self.write_login(file)

    def remove_login(self, login, file):
        if login in self.logins:
            del self.logins[login]
            self.write_login(file)
        else:
            raise ValueError("Login not found")

    def find_login(self, login):
        if login in self.logins:
            print(f"Login: {login}, password: {self.logins[login]}")
        else:
            print("Login not found")

    def change_password(self, login, password, file):
        if login in self.logins:
            self.logins[login] = password
            self.write_login(file)
        else:
            print("Login not found")

    def write_login(self, file):
        with open(file, 'wb') as pickle_file:
            pickle.dump(self.logins, pickle_file)

    def write_gzip_login(self, file):
        with gzip.open(file, 'wb') as gzip_file:
            serialized = pickle.dumps(self.logins)
            gzip_file.write(serialized)

    def read_login(self, file):
        with open(file, 'rb') as pickle_file:
            read_logins = pickle.load(pickle_file)
        print(f"Origin list = {self.logins} \nPickle list = {read_logins}")
        return read_logins

    def read_gzip_login(self, file):
        with gzip.open(file, 'rb') as gzip_file:
            serialized = gzip_file.read()
            read_logins = pickle.loads(serialized)
        print(f"Origin list = {self.logins} \nPickle list = {read_logins}")
        return read_logins


new_login = Login()
print("Numbers from pickle: ")
new_login.write_login('new_login.pickle')
new_login.read_login('new_login.pickle')

print("Login from gzip: ")
new_login.write_gzip_login('new_login.gz')
new_login.read_gzip_login('new_login.gz')

print("Updated dict: ")
new_login.add_login("test5", "122222", 'new_login.pickle')
new_login.read_login('new_login.pickle')

print("Dict after remove: ")
new_login.remove_login("test5", 'new_login.pickle')
new_login.read_login('new_login.pickle')

print("Change password: ")
new_login.change_password("test", "44444", 'new_login.pickle')
new_login.read_login('new_login.pickle')

print("Find login: ")
new_login.find_login("test")
