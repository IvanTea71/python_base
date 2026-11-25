def sum_numbers():
    total = 0

    for i in range(1, 101):
        if i % 2 == 0:
            total += i

    print("Сумма чётных чисел:", total)

def squares_numbers():
    squares = [i ** 2 for i in range(1, 11) if i % 2 != 0]
    print("Квадраты нечётных чисел:", squares)

def input_numbers():
    count = 0
    number = 0

    while number >= 0:
        number = int(input("Введите число: "))
        count += 1

    print("Количество введённых чисел:", count)