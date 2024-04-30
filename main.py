import threading
import pickle


#task1 - task2
def max_number(arr):
    if not arr:
        raise IndexError("List is empty")
    print(f"Max number: {max(arr)}")


def min_number(arr):
    if not arr:
        raise IndexError("List is empty")
    print(f"Min number: {min(arr)}")


def suma(arr):
    if not arr:
        raise IndexError("List is empty")
    print(f"Sum of numbers: {sum(arr)}")


def mean(arr):
    if not arr:
        raise IndexError("List is empty")
    size = len(arr)
    mean_value = sum(arr) / size
    print(f"Mean of numbers: {round(mean_value, 2)}")


try:
    numbers = list(map(int, input("Enter numbers divided by spaces: ").split()))
    print(numbers)
    t_max = threading.Thread(target=max_number, args=(numbers,))
    t_min = threading.Thread(target=min_number, args=(numbers,))
    t_sum = threading.Thread(target=suma, args=(numbers,))
    t_mean = threading.Thread(target=mean, args=(numbers,))

    t_max.start()
    t_min.start()
    t_sum.start()
    t_mean.start()

    t_max.join()
    t_min.join()
    t_sum.join()
    t_mean.join()

except Exception as e:
    print("Message: ", e)



# task3
file_numbers = "numbers.pickle"
file_even_numbers = "even_numbers.pickle"
file_odd_numbers = "odd_numbers.pickle"


def write_numbers(numbers, file):
    if not numbers:
        raise IndexError("List is empty")

    with open(file, 'wb') as pickle_file:
        pickle.dump(numbers, pickle_file)


def read_numbers(file):
    with open(file, 'rb') as pickle_file:
        read_num = pickle.load(pickle_file)
    return read_num


def even_numbers():
    read_num = read_numbers(file_numbers)
    even_num = []
    for num in read_num:
        if num % 2 == 0:
            even_num.append(num)
    write_numbers(even_num, file_even_numbers)
    read_num = read_numbers(file_even_numbers)
    print(read_num)


def odd_numbers():
    read_num = read_numbers(file_numbers)
    odd_num = []
    for num in read_num:
        if num % 2 != 0:
            odd_num.append(num)
    write_numbers(odd_num, file_odd_numbers)
    read_num = read_numbers(file_odd_numbers)
    print(read_num)


try:
    numbers = list(map(int, input("Enter numbers divided by spaces: ").split()))
    write_numbers(numbers, file_numbers)
    t_even = threading.Thread(target=even_numbers, args=())
    t_odd = threading.Thread(target=odd_numbers, args=())

    t_even.start()
    t_odd.start()

    t_even.join()
    t_odd.join()

except Exception as e:
    print("Message: ", e)
