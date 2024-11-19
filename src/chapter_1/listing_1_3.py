import threading


def hello_from_thread():
    print(f'Привет от потока: {threading.current_thread()}!')


hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'В данный момент Python исполняет {total_threads} поток(ов)')
print(f'Текущий поток: {thread_name}')

hello_thread.join()