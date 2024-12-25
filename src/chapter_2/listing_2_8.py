import asyncio
from src.util import delay


async def main() -> None:
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))
    result = await sleep_for_three
    print(result)

# async def main() -> None:
#     sleep_for_three = delay(3)
#     print(type(sleep_for_three))
#     result = await sleep_for_three
#     print(result)


# async def main() -> None:
#     sleep_for_three = await delay(3)
#     print(sleep_for_three)


asyncio.run(main())

"""
<class '_asyncio.Task'>
Засыпаю на 3 с
.
.
.
сон в течении 3 с закончился
3
"""

"""
<class 'coroutine'>
Засыпаю на 3 с
.
.
.
сон в течении 3 с закончился
3
"""