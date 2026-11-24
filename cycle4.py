# Задание 1. Сумма всех чётных чисел от 1 до 100
total = 0

for i in range(1, 101):
    if i % 2 == 0:
        total += i

print("Сумма чётных чисел:", total)

# Задание 2. Квадраты всех нечётных чисел от 1 до 10
squares = [i ** 2 for i in range(1, 11) if i % 2 != 0]

print("Квадраты нечётных чисел:", squares)

# Задание 3. Ввод чисел до появления отрицательного
count = 0

while True:
    number = int(input("Введите число: "))

    if number < 0:
        break

    count += 1

print("Количество введённых чисел:", count)