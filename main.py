import threading
import random
import pickle
from datetime import datetime
import os
import glob
import re

# task1

size = 100
numbers = []


def random_numbers():
    global numbers

    numbers = [random.randint(1, 999) for _ in range(size)]
    print(f"Random numbers list: {numbers}")


def suma():
    try:
        if not numbers:
            raise IndexError("List is empty")
        print(f"Sum of numbers: {sum(numbers)}")
    except IndexError as e:
        print("Message: ", e)


def mean():
    try:
        if not numbers:
            raise IndexError("List is empty")
        mean_value = sum(numbers) / size
        print(f"Mean of numbers: {round(mean_value, 2)}")
    except IndexError as e:
        print("Message: ", e)


t1 = threading.Thread(target=random_numbers, args=())
t2 = threading.Thread(target=suma, args=())
t3 = threading.Thread(target=mean, args=())

t1.start()
t1.join()

t2.start()
t3.start()

t2.join()
t3.join()

# task2
numbers_file = "numbers.pickle"
prime_numbers_file = "prime_numbers.pickle"
numbers_factorial_file = "numbers_factorial.pickle"


def save_numbers():
    print("\nStart saving numbers: ", datetime.now())
    numbers = [random.randint(1, 10) for _ in range(size)]
    write_numbers(numbers, numbers_file)
    print("\nSaving numbers ends: ", datetime.now())


def write_numbers(numbers, file):
    if not numbers:
        raise IndexError("List is empty")

    with open(file, 'wb') as pickle_file:
        pickle.dump(numbers, pickle_file)


def read_numbers(file):
    with open(file, 'rb') as pickle_file:
        read_num = pickle.load(pickle_file)
    return read_num


def is_prime():
    print("\nStart searching for prime numbers numbers: ", datetime.now())
    prime_num = []
    read_num = read_numbers(numbers_file)
    print("Origin list: ", read_num)
    for item in read_num:
        if item <= 1:
            continue
        prime = True
        for i in range(2, int(item ** 0.5) + 1):
            if item % i == 0:
                prime = False
                break
        if prime:
            prime_num.append(item)
    write_numbers(prime_num, prime_numbers_file)
    print("Prime numbers: ", read_numbers(prime_numbers_file))
    print("\nEnd searching for prime numbers numbers: ", datetime.now())


def factorial_save():
    print("\nStart calculating factorial: ", datetime.now())
    num_factorial = []
    read_num = read_numbers(numbers_file)
    print("Origin list: ", read_num)
    for item in read_num:
        num_factorial.append(factorial(item))
    write_numbers(num_factorial, numbers_factorial_file)
    print("Factorials: ", read_numbers(numbers_factorial_file))
    print("\nEnd calculating factorial: ", datetime.now())


def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


t1 = threading.Thread(target=save_numbers, args=())
t2 = threading.Thread(target=is_prime, args=())
t3 = threading.Thread(target=factorial_save, args=())

t1.start()
t1.join()

t2.start()
t3.start()

t2.join()
t3.join()

# task3
dir_path = "hw_files"
concatenate_file = "concatenate_file.txt"
forbidden_words_file = "forbidden_words.txt"
files = glob.glob(os.path.join(dir_path, '*'))


def concatenate_files():
    print("\nStart concatenate file: ", datetime.now())
    with open(concatenate_file, 'w') as result_file:
        for file in files:
            with open(file, 'r') as f:
                file_content = f.read()
                result_file.write(file_content + "\n")
    print("\nEnd concatenate file: ", datetime.now())


def remove_words():
    print("\nStart remove words: ", datetime.now())
    with open(forbidden_words_file, 'r') as forbidden_file:
        forbidden_words = list(forbidden_file.read().split())
    with open(concatenate_file, 'r') as result_file:
        content = result_file.read()
    for word in forbidden_words:
        if word in content:
            content = re.sub(r'\b{}\b'.format(re.escape(word)), '', content)
    with open(concatenate_file, 'w') as result_file:
        result_file.write(content)
    print("\nEnd remove words: ", datetime.now())


t1 = threading.Thread(target=concatenate_files, args=())
t2 = threading.Thread(target=remove_words, args=())

t1.start()
t1.join()

t2.start()
t2.join()
