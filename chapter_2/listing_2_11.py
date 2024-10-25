import asyncio
from asyncio import CancelledError
import time

from util import delay


async def main() -> None:
    start = time.perf_counter()

    long_task = asyncio.create_task(delay(10))

    seconds_elapsed = 0

    while not long_task.done():
        print("Задача не закончилась, следующая проверка через секунду.")
        time.sleep(1)
        await asyncio.sleep(1)
        seconds_elapsed += 1
        if seconds_elapsed == 5:
            long_task.cancel()

    try:
        await long_task
    except CancelledError:
        print("Наша задача была снята")
    print(time.perf_counter() - start)

asyncio.run(main())


"""
Засыпаю на 2 с
Timed out!
Задача была снята? True
1.0090352999977767
"""
