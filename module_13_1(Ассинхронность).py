import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 11):
        print(f'Силач {name} поднял {i} шар')
        await asyncio.sleep(1 / power)
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Артём', 7))
    task2 = asyncio.create_task(start_strongman('Денис', 10))
    task3 = asyncio.create_task(start_strongman('Коля', 9))

    await task1
    await task2
    await task3

asyncio.run(start_tournament())