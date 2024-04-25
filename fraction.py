import json


class Fraction:
    fraction_file = 'fractions.json'

    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def display_fraction(self):
        print(f"{self.nominator}/{self.denominator}")

    def add(self, other_fraction):
        result_nominator = self.nominator * other_fraction.denominator + other_fraction.nominator * self.denominator
        result_denominator = other_fraction.denominator * self.denominator
        return Fraction(result_nominator, result_denominator)

    def subtract(self, other_fraction):
        result_nominator = self.nominator * other_fraction.denominator - other_fraction.nominator * self.denominator
        result_denominator = other_fraction.denominator * self.denominator
        return Fraction(result_nominator, result_denominator)

    def multiply(self, other_fraction):
        result_nominator = self.nominator * other_fraction.nominator
        result_denominator = other_fraction.denominator * self.denominator
        return Fraction(result_nominator, result_denominator)

    def divide(self, other_fraction):
        result_nominator = self.nominator * other_fraction.denominator
        result_denominator = other_fraction.nominator * self.denominator
        return Fraction(result_nominator, result_denominator)

    @classmethod
    def save_fractions(cls, fractions):
        data = []
        for fraction in fractions:
            dct = {"nominator": fraction.nominator, "denominator": fraction.denominator}
            data.append(dct)

        with open(cls.fraction_file, 'w') as file:
            json.dump(data, file, indent=4)

    @classmethod
    def load_fractions(cls):
        with open(cls.fraction_file, 'r') as file:
            data = json.load(file)

        fractions = []
        for dct in data:
            fraction = cls(dct["nominator"], dct["denominator"])
            fractions.append(fraction)
        return fractions


first_fraction = Fraction(10, 20)
new_fraction = Fraction(5, 20)

first_fraction.display_fraction()
new_fraction.display_fraction()

result_addition = first_fraction.add(new_fraction)
result_addition.display_fraction()

result_subtraction = first_fraction.subtract(new_fraction)
result_subtraction.display_fraction()

result_multiplication = first_fraction.multiply(new_fraction)
result_multiplication.display_fraction()

result_division = first_fraction.divide(new_fraction)
result_division.display_fraction()

fractions = [first_fraction, new_fraction, result_division, result_multiplication, result_addition, result_subtraction]

Fraction.save_fractions(fractions)
Fraction.load_fractions()