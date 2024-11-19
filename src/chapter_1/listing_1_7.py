import time

import requests


def read_example() -> None:
    response = requests.get('https://www.example.com')
    print(response.status_code)


start = time.time()
read_example()
read_example()
end = time.time()

print(f'Синхронное выполнение заняло: {end - start:.4f} с.')

"""
200
200
Синхронное выполнение заняло: 2.3072 с.
"""
