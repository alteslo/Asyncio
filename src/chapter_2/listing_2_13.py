import asyncio
import time

from src.util import delay


async def main() -> None:
    start = time.perf_counter()

    task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(task), timeout=5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Задача заняла более 5с, скоро она закончится!")
        result = await task
        print(result)
    print(time.perf_counter() - start)

asyncio.run(main())


"""
Засыпаю на 10 с
Задача заняла более 5с, скоро она закончится!
сон в течении 10 с закончился
10
10.020697300031316
"""
