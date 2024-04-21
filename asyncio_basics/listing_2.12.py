import asyncio
import time

from util import delay


async def main() -> None:
    start = time.perf_counter()

    delay_task = asyncio.create_task(delay(2))

    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Timed out!")
        print(f"Задача была снята? {delay_task.cancelled()}")
    print(time.perf_counter() - start)

asyncio.run(main())


"""
Задача не закончилась, следующая проверка через секунду.
Засыпаю на 10 с
Задача не закончилась, следующая проверка через секунду.
Задача не закончилась, следующая проверка через секунду.
Задача не закончилась, следующая проверка через секунду.
Задача не закончилась, следующая проверка через секунду.
Задача не закончилась, следующая проверка через секунду.
Наша задача была снята
"""
