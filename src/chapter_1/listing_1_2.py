import os
import threading


print(f'Исполняется python процесс: {os.getpid()}')

total_thread = threading.active_count()
thread_name = threading.current_thread().name

print(f'В данный момент Python исполняет {total_thread} поток(ов). Текущий поток: {thread_name}')


"""
Исполняется python процесс: 22640
В данный момент Python исполняет 1 поток(ов). Текущий поток: MainThread
"""
