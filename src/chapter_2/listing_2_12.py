import asyncio
import time

from src.util import delay


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
Засыпаю на 2 с
Timed out!
Задача была снята? True
1.0079315999755636
"""
