
import asyncio


async def hellow_world_message() -> str:
    await asyncio.sleep(1)
    return 'Hello World!'


async def main() -> None:
    message = await hellow_world_message()
    print(message)

asyncio.run(main())

'''
Hello World!
'''
