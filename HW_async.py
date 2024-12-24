import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(5):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i + 1}')
    print(f'{name} закончил соревнование')


async def start_tournament():
    st1 = asyncio.create_task(start_strongman('Denis', 3))
    st2 = asyncio.create_task(start_strongman('Viktor', 4))
    st3 = asyncio.create_task(start_strongman('Vladimir', 5))
    await st1
    await st2
    await st3


asyncio.run(start_tournament())
