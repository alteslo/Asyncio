import threading
import time


def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    print(f'fib({number}) равно {fib(number)}')


def fibs_with_threads():
    fortieth_thread = threading.Thread(target=print_fib, args=(40,))
    fortyfirst_thread = threading.Thread(target=print_fib, args=(41,))

    fortieth_thread.start()
    fortyfirst_thread.start()

    fortieth_thread.join()
    fortyfirst_thread.join()


start = time.time()
fibs_with_threads()
end = time.time()

print(f'Многопоточное выполнение заняло: {end - start:.4f} с.')

"""
fib(40) равно 63245986
fib(41) равно 102334155
Многопоточное выполнение заняло: 28.3557 с.
"""
