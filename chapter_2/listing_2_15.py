from asyncio import Future
import asyncio
import time


def make_request() -> Future:
    future = Future()
    asyncio.create_task(set_future_value(future))
    return future


async def set_future_value(future: Future) -> None:
    await asyncio.sleep(2)
    future.set_result(42)


async def main():
    future = make_request()
    print(f"Будущий объект готов? {future.done()}")
    value = await future
    print(f"Будущий объект готов? {future.done()}")
    print(value)


start = time.perf_counter()
asyncio.run(main())
print(time.perf_counter() - start)

"""
Будущий объект готов? False
Будущий объект готов? True
42
2.0034294000070076
"""
