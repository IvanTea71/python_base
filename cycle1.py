def timer():
    try:
        number = int(input("Введите положительное число: ").strip())
    except ValueError:
        print("Ошибка: необходимо число!")
        return

    if number > 0:
        while number >= 0:
            print(number)
            number -= 1
    else:
        print("Введено отрицательное число или 0")

timer()