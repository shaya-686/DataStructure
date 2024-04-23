import pickle
import gzip

data = {"login": "some_login", "password": "123456"}


#
# serialized = pickle.dumps(data)
#
# print(serialized)
#
# read_data = pickle.loads(serialized)
# print(type(read_data), read_data)
# with open('data.pickle', 'wb') as file:
#     pickle.dump(data, file)
#
# with open('data.pickle', 'rb') as file:
#     read_data = pickle.load(file)
#
# print(type(read_data), read_data)
# with gzip.open('data.gz', 'wb') as file:
#     serialized = pickle.dumps(data)
#     file.write(serialized)

# with gzip.open('data.gz', 'rb') as file:
#     serialized = file.read()
#     read_data = pickle.loads(serialized)
#
# print(serialized)
# print(type(read_data), read_data)


# task1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f'name: {self.name} with age {self.age}')


person = Person("Anna", 31)
# with open('person.pickle', 'wb') as file:
#     pickle.dump(person, file)
#
# with open('person.pickle', 'rb') as file:
#     read_person = pickle.load(file)
#
# print(type(read_person))
# read_person.print_info()

with gzip.open('person.gz', 'wb') as file:
    person_serialized = pickle.dumps(person)
    file.write(person_serialized)

with gzip.open('person.gz', 'rb') as file:
    read_data = file.read()
    person_read = pickle.loads(read_data)

print(type(person_read))
person_read.print_info()
