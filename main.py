import threading
import queue
import multiprocessing as mp


# def print_info(info):
#     print(info)
#
#
# def sort_array(arr):
#     print(sorted(arr))
#
#
# t3 = threading.Thread(target=print_info, args=([2, 5, 3, 4, 8, 7],))
# t4 = threading.Thread(target=print_info, args=([2, 5, 9, 7],))
# t1 = threading.Thread(target=print_info, args=("Thread1",))
# t2 = threading.Thread(target=print_info, args=("Thread2",))
#
# t3.start()
# t4.start()
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# t3.join()
# t4.join()

# global_number = 0
# global_list = []
# lock = threading.Lock()


# def append():
#     for _ in range(100000):
#         global global_list
#         lock.acquire()
#         global_list.append(1)
#         lock.release()
#
#
# def remove():
#     for _ in range(100):
#         global global_list
#         lock.acquire()
#         global_list.pop()
#         lock.release()
#
#
# t1 = threading.Thread(target=append, args=())
# t2 = threading.Thread(target=remove, args=())
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print("Final result: ", global_list)


# tasks = queue.Queue()
# num_threads = 5


# def worker(tasks, thread_num):
#     while True:
#         task = tasks.get()
#
#         if task is None:
#             break
#         print(f"Thread: {thread_num} works with {task}")
#         tasks.task_done()
#
#
# for i in range(10):
#     tasks.put(f"Task {i + 1}")
#
# for _ in range(num_threads):
#     tasks.put(None)
#
# threads = []
#
# for i in range(num_threads):
#     t = threading.Thread(target=worker, args=(tasks, i+1,))
#     threads.append(t)
#
# for t in threads:
#     t.start()
#
# for t in threads:
#     t.join()

##multiproxessing

# def print_info(info):
#     for _ in range(10):
#         print(info)
#
#
# def sort_array(arr):
#     for _ in range(10):
#         print(sorted(arr))
#
#
# if __name__ == "__main__":
#     print("Max number of processes:", mp.cpu_count())
#     p1 = mp.Process(target=print_info, args=("Process1",))
#     p2 = mp.Process(target=sort_array, args=([2, 5, 9, 7],))
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()


def mean(arr):
    suma = sum(arr)
    return suma / len(arr)


def get_parts(arr, num=mp.cpu_count()):
    n = len(arr)
    part_len = n // num
    return [arr[(part_len * k):part_len * (k + 1)] for k in range(num)]


def get_arr(len=100_000):
    return list(range(len))


if __name__ == "__main__":
    arr = get_arr()
    parts = get_parts(arr)
    with mp.Pool() as pool:
        results = pool.map(func=mean, iterable=parts)
    print("Results of pool: ", results)
    print("Final mean result: ", mean(results))

