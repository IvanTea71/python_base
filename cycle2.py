password = "python123"
user_password = ""

while user_password != password:
    user_password = input("Введите пароль: ")

    if user_password == password:
        print("Пароль верный! Доступ разрешён.")
    else:
        print("Неверный пароль. Попробуйте ещё раз.")