password = "python123"

while True:
    user_password = input("Введите пароль: ")

    if user_password == password:
        print("Пароль верный! Доступ разрешён.")
        break
    else:
        print("Неверный пароль. Попробуйте ещё раз.")