
async def couroutine_add_one(number: int) -> int:
    return number + 1


def add_one(number: int) -> int:
    return number + 1


function_result = add_one(1)
coroutine_result = couroutine_add_one(1)


print(f'Результат функции равен {function_result}, а его тип равен {type(function_result)}')
print(f'Результат корутины равен {coroutine_result}, а его тип равен {type(coroutine_result)}')

'''
Результат функции равен 2, а его тип равен <class 'int'>
Результат корутины равен <coroutine object couroutine_add_one at 0x00000291499FC880>, а его тип равен <class 'coroutine'>
sys:1: RuntimeWarning: coroutine 'couroutine_add_one' was never awaited

'''
