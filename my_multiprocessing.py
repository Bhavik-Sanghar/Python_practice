from multiprocessing import Process

counter = 0


def increment():
    global counter
    counter += 1
    print("Child:", counter)


if __name__ == "__main__":
    p1 = Process(target=increment)
    p2 = Process(target=increment)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Main:", counter)