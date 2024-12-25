import asyncio
import time

from src.util import delay


async def hello_every_second():
    for i in range(2):
        await asyncio.sleep(1)
        print('пока я жду исполняется другой код!')


async def main() -> None:
    start = time.perf_counter()

    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))

    await hello_every_second()
    await first_delay
    await second_delay

    print(time.perf_counter() - start)


asyncio.run(main())

"""
Засыпаю на 3 с
Засыпаю на 3 с
Засыпаю на 3 с
пока я жду исполняется другой код!
пока я жду исполняется другой код!
сон в течении 3 с закончился
сон в течении 3 с закончился
сон в течении 3 с закончился
3.0160130000003846
"""

