from asyncio import Future
import time

my_future = Future()
print(f"my_future готов? {my_future.done()}")

my_future.set_result(42)
print(f"my_future готов? {my_future.done()}")
print(f"Какой результат хранится в my_future? {my_future.result()}")


"""
my_future готов? False
my_future готов? True
Какой результат хранится в my_future? 42
"""
