# Задача - есть функция, которая возвращает результат возведения числа a в степень b.
# Нужно ускорить ее, чтобы она не делала повторные вычисления.

def memorise_func(f):
    mem = {}

    def wrapper(*args):
        print(f'Выполнение функции с аргументами={args}, внутренняя память={mem}')
        if args not in mem:
            mem[args] = f(*args)
            return f'Функция выполнилась, ответ = {mem[args]}'
        else:
            return f'Функция уже была выполнена раньше, ответ = {mem[args]}'

    return wrapper

@memorise_func
def func(a, b):
    print(f'Выполняем функцию с аргументами ({a}, {b})')
    return a ** b


print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 2), '\n')
print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 5), '\n')
