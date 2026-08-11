# import asyncio

# async def task(name):
#     print(name, "started")

#     await asyncio.sleep(2)

#     print(name, "finished")

# async def task2():
#     print("Task 2 started")
#     await asyncio.sleep(1)
#     print("Task 2 finished")
    
# async def task3():
#     print("Task 3 started")
#     await asyncio.sleep(10)
#     print("Task 3 finished")

# async def main():
#     t1 = task("A")
#     t2 = task2()
#     t3 = task3()
#     await asyncio.gather(t2,t3,t1)


# asyncio.run(main())
import asyncio
import time

# pyrefly: ignore [missing-import]
import httpx
                                                                                                                                                                 

async def get_user():
    print("User: started")

    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://jsonplaceholder.typicode.com/users/1"
        )

    print("User: response received")
    return response.json()


async def get_joke():
    print("Joke: started")

    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://official-joke-api.appspot.com/random_joke"
        )

    print("Joke: response received")
    return response.json()


async def main():
    start = time.time()

    user , joke = await asyncio.gather(get_user(),get_joke())
   
    print("User:", user)
    print("Joke:", joke)

    print("Time:", time.time() - start)


asyncio.run(main())