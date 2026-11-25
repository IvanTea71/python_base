def can_vote():
    try:
        age = int(input("Введите ваш возраст: ").strip())
    except ValueError:
        print("Ошибка: возраст необходимо ввести целым числом!")
        return

    citizen = input("Вы гражданин страны? (да/нет): ").strip().lower()
    disqualified = input("Вы дисквалифицированы? (да/нет): ").strip().lower()

    if citizen not in ("да", "нет") or disqualified not in ("да", "нет"):
        print("Ошибка: введите только «да» или «нет»!")
        return

    if age >= 18 and citizen == "да" and disqualified == "нет":
        print("Вы можете голосовать!")
    else:
        print("Вы не можете голосовать.")


can_vote()