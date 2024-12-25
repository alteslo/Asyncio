import asyncio
import time

from src.util import delay


async def main() -> None:
    start = time.perf_counter()

    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))
    sleep_twice_more = asyncio.create_task(delay(3))

    await sleep_for_three
    await sleep_again
    await sleep_once_more
    await sleep_twice_more

    print(time.perf_counter() - start)


asyncio.run(main())

"""
Засыпаю на 3 с
Засыпаю на 3 с
Засыпаю на 3 с
Засыпаю на 3 с
сон в течении 3 с закончился
сон в течении 3 с закончился
сон в течении 3 с закончился
сон в течении 3 с закончился
3.0077947999961907
"""