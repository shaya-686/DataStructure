import json

data = {"name": "Jhon", "age": 42, "info": {"city": "Kharkiv", "birthday": "2001"}}

# with open("data.json", 'w') as file:
#     json.dump(data, file)

with open("data.json", 'r') as file:
    read_data = json.load(file)

print(read_data)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, self.age)

    def save(self, filename='person.json'):
        dct = {"name": self.name, "age": self.age}
        with open(filename, 'w') as file:
            json.dump(dct, file)

    def load(self, filename='person.json'):
        with open(filename, 'r') as file:
            dct = json.load(file)
            self.name = dct["name"]
            self.age = dct["age"]

    @classmethod
    def load_person(cls, filename='person.json'):
        with open(filename, 'r') as file:
            dct = json.load(file)
        return cls(name=dct["name"], age=dct["age"])

    @classmethod
    def save_persons(cls, persons, filename='person3.json'):
        data = []

        for person in persons:
            dct = {"name": person.name, "age": person.age}
            data.append(dct)
            # data = [{"name": person.name, "age": person.age} for person in persons]
            # data = [person.person_get_dict() for person in persons]

            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)

    @classmethod
    def load_persons(cls, filename='person3.json'):
        with open(filename, 'r') as file:
            data = json.load(file)

        persons = []
        for dct in data:
            person = cls(dct["name"], dct["age"])
            persons.append(person)
        return persons

    def person_get_dict(self):
        return {"name": self.name, "age": self.age}

    def birthday(self):
        self.age += 1


person = Person("Max", 16)
# person.birthday()
# person.birthday()
# person.birthday()
person.save()
person.load()
person.print_info()

new_person = Person.load_person()
new_person.print_info()
person1 = Person("Alla", 25)
person2 = Person("Al", 15)
person3 = Person("HAlla", 35)
Person.save_persons([person1, person2, person3])

for read_data in Person.load_persons():
    read_data.print_info()
