def max_number(a, b):
    type_a = type(a).__name__
    type_b = type(b).__name__
    try:
        if type(a) in (int, float) and type(b) in (int, float):
            if a >= b:
                return a
            else:
                return b
    except:
        print(f"Недопустимый тип для сравнения: {a}:{type_a} {b}:{type_b}")

def empty_function():
    pass

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

def test_max_number():
    assert max_number(5, 10) == 10, "Ошибка: результат сравнения (5, 10) false"
    assert max_number(-5, -2) == -2, "Ошибка: результат сравнения (-5, -2) false"
    assert max_number(0, 10) == 10, "Ошибка: результат сравнения (0, 10) false"
    assert max_number(7, 7) == 7, "Ошибка: результат сравнения (7, 7) false"
    assert max_number("5", 10) is None
    assert max_number([1, 2], [3, 4]) is None

for number in even_numbers(10):
    print(number)

test_max_number()