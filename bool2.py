def print_number():
    try:
        age = int(input("Введите число от 1 до 5: ").strip())
    except ValueError:
        print("Ошибка: необходимо число!")
        return

    numbers = { 1: "one",
                2: "two",
                3: "three",
                4: "four",
                5: "five" }

    if age >= 1 and age <= 5:
        print(numbers[age])


print_number()