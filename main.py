import bintrees
from datetime import datetime
import random


class Person:
    def __init__(self, code, name, city):
        self.code = code
        self.name = name
        self.city = city

    def __str__(self):
        return (f'name - {self.name},'
                f'code - {self.code},'
                f'city - {self.city}')

    def update(self, name, city):
        if name is None and city is None:
            raise ValueError("No data to update")

        if name is not None:
            self.name = name

        if city is not None:
            self.city = city


class Fine:
    fine_types = {"1001": 100, "1002": 200, "1003": 300}

    def __init__(self, fine_id, fine_type, person: Person):
        if fine_type not in self.fine_types:
            raise ValueError("Unknown fine type")
        self.type = fine_type
        self.amount = self.fine_types[fine_type]
        self.person = person
        self.create_date = datetime.now()
        self.payment_state = False
        self.payment_date = None
        self.id = fine_id

    def __str__(self):
        return (f'Fine info: '
                f'id - {self.id}, type - {self.type}, amount - {self.amount}, '
                f'creation date - {self.create_date}, payment state - {self.payment_state}, '
                f'payment date - {self.payment_date}')

    def pay_fine(self):
        if self.payment_state:
            raise ValueError("Fine has already payed")
        else:
            self.payment_state = True
            self.payment_date = datetime.now()


class TaxInspection:

    def __init__(self):
        self.tree = bintrees.AVLTree()

    def add_taxpayer(self, person: Person):
        if person.code in self.tree:
            raise ValueError("Person already exists in tax inspection DB")
        self.tree[person.code] = {"person": person, "fines": []}

    def update_tax_payer(self, person, name, city):
        if person.code not in self.tree:
            raise ValueError("Taxpayer not found")
        self.tree[person.code]["person"].update(name, city)

    def add_fine(self, fine: Fine):
        if fine.person.code not in self.tree:
            raise ValueError(f"Person with code {fine.person.code} not found")
        self.tree[fine.person.code]["fines"].append(fine)

    def pay_taxpayer_fine(self, fine: Fine):
        if fine.person.code not in self.tree:
            raise ValueError(f"Person with code {fine.person.code} not found")
        if fine not in self.tree[fine.person.code]["fines"]:
            raise ValueError(f"Fine {fine} not found")
        fine.pay_fine()

    def remove_fine(self, fine):
        if fine.person.code not in self.tree:
            raise ValueError(f"Person with code {fine.person.code} not found")
        if fine not in self.tree[fine.person.code]["fines"]:
            raise ValueError(f"Fine {fine.id} not found")

        self.tree[fine.person.code]["fines"].remove(fine)

    def display_all_fines(self):
        if not self.tree:
            raise IndexError("Tree is empty")
        for value in self.tree.values():
            person = value["person"]
            fines = value["fines"]
            if not fines:
                print(f"No fines found for {person}")
            else:
                print(f"Person: {person}")
                for fine in fines:
                    print(str(fine))
            print()

    def display_taxpayer_fines(self, person: Person):
        if person.code not in self.tree:
            raise ValueError("Unknown taxpayer")
        fines = self.tree[person.code]["fines"]
        if not fines:
            print("Taxpayer doesn't have fines")
        else:
            print(f"Person: {person}")
            for fine in fines:
                print(str(fine))
            print()

    def display_fines_by_type(self, fine_types):
        fines_found = False
        for value in self.tree.values():
            for fine in value["fines"]:
                if fine.type in fine_types:
                    print(str(fine))
                    fines_found = True
        if not fines_found:
            print("No fines of the specified types found")
        print()

    def display_fines_by_city(self, cities):
        fines_found = False
        for value in self.tree.values():
            person = value["person"]
            if person.city in cities:
                print(f"Person: {person}")
                for fine in value["fines"]:
                    print(str(fine))
                    fines_found = True
        if not fines_found:
            print("No fines of the specified types found")
        print()


tax_inspection = TaxInspection()
# for statistic
names = ["Mary", "Alex", "Arthur", "David", "Emma"]
cities = ["Kyiv", "Lviv", "Dnipro", "Kharkiv", "Odessa"]
fine_types = ["1001", "1002", "1003"]

for i in range(len(names)):
    person = Person(random.randint(10000000, 99999999), random.choice(names), random.choice(cities))
    tax_inspection.add_taxpayer(person)

    for _ in range(random.randint(1, 3)):
        fine_type = random.choice(fine_types)
        fine = Fine(random.randint(1000, 9999), fine_type, person)
        tax_inspection.add_fine(fine)

print("All fines: ")
tax_inspection.display_all_fines()

print("Fines with codes ['1001', '1002']: ")
tax_inspection.display_fines_by_type(["1001", "1002"])

print("Persons with cities ['Kyiv', 'Lviv']: ")
tax_inspection.display_fines_by_city(["Kyiv", "Lviv"])

# to check other methods
new_person = Person(603200000, "Olga", "Lviv")
new_fine = Fine(10000, "1001", new_person)
tax_inspection.add_taxpayer(new_person)
tax_inspection.add_fine(new_fine)
tax_inspection.display_taxpayer_fines(new_person)
tax_inspection.pay_taxpayer_fine(new_fine)
tax_inspection.display_taxpayer_fines(new_person)
tax_inspection.update_tax_payer(new_person, None, "Kyiv")
tax_inspection.display_taxpayer_fines(new_person)
tax_inspection.remove_fine(new_fine)
tax_inspection.display_taxpayer_fines(new_person)
