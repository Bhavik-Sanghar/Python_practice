# import time

# def task():
#     for i in range(5):
#         print("Task:", i)
#         time.sleep(1)

# print("Program started")

# task()

# print("Program finished")

# import threading
# import time

# def task():
#     for i in range(5):
#         print("Task:", i)
#         time.sleep(1)


# print("Program started")

# thread = threading.Thread(target=task)

# thread.start()

# print("Program finished")


import threading
import time

def task(name):
    for i in range(5):
        print(name, i)
        time.sleep(1)


thread1 = threading.Thread(target=task, args=("Thread 1",))
thread2 = threading.Thread(target=task, args=("Thread 2",))

thread1.start()
thread2.start()

# thread1.join()
thread2.join()

print("Both threads finished")