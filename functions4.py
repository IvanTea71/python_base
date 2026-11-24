def max_number(a, b):
    if a >= b:
        return a
    else:
        return b

def empty_function():
    pass

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

assert max_number(5, 10) == 10, "Ошибка: ожидалось 10"
assert max_number(20, 7) == 20, "Ошибка: ожидалось 20"
assert max_number(-5, -2) == -2, "Ошибка: ожидалось -2"
assert max_number(0, 10) == 10, "Ошибка: ожидалось 10"
assert max_number(7, 7) == 7, "Ошибка: одинаковые числа обработаны неправильно"

for number in even_numbers(10):
    print(number)
