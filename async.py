import asyncio

async def task(name):
    print(name, "started")

    await asyncio.sleep(2)

    print(name, "finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")
    
async def task3():
    print("Task 3 started")
    await asyncio.sleep(10)
    print("Task 3 finished")

async def main():
    t1 = task("A")
    t2 = task2()
    t3 = task3()
    await asyncio.gather(t2,t3,t1)


asyncio.run(main())