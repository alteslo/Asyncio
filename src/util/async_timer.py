import functools
import time
from typing import Callable, Any


def async_timed() -> Callable:
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args: Any, **kwargs: Any) -> Any:
            print(f'выполняется {func} с аргументами {args} и {kwargs}')
            start = time.perf_counter()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.perf_counter()
                total = end - start
                print(f'{func} завершилось за {total:.4f} секунд')
        return wrapped
    return wrapper
