
# 1. Сложение
try:
    num1 = float(input("Введите первое число для сложения: "))
    num2 = float(input("Введите второе число для сложения: "))
    print("Результат сложения:", num1 + num2)
except ValueError:
    print("Ошибка! Необходимо вводить числа.")

# 2. Вычитание
try:
    num1 = float(input("\nВведите первое число для вычитания: "))
    num2 = float(input("Введите второе число для вычитания: "))
    print("Результат вычитания:", num1 - num2)
except ValueError:
    print("Ошибка! Необходимо вводить числа.")

# 3. Умножение
try:
    num1 = float(input("\nВведите первое число для умножения: "))
    num2 = float(input("Введите второе число для умножения: "))
    print("Результат умножения:", num1 * num2)
except ValueError:
    print("Ошибка! Необходимо вводить числа.")

# 4. Деление
try:
    num1 = float(input("\nВведите первое число для деления: "))
    num2 = float(input("Введите второе число для деления: "))
    print("Результат деления:", num1 / num2)
except ValueError:
    print("Ошибка! Необходимо вводить числа.")
except ZeroDivisionError:
    print("Ошибка! Деление на ноль невозможно.")
