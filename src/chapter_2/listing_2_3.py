
import asyncio


async def couroutine_add_one(number: int) -> int:
    return number + 1

result = asyncio.run(couroutine_add_one(1))

print(result)
