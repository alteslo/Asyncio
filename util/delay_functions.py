import asyncio


async def delay(delay_seconds: int):
    print(f'Засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течении {delay_seconds} с закончился')
    return delay_seconds

