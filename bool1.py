def input_data():
    age = input("Введите ваш возраст: ").strip()
    citizen = input("Вы гражданин страны? (да/нет): ").strip().lower()
    disqualified = input("Вы дисквалифицированы? (да/нет): ").strip().lower()
    validation(age,citizen,disqualified)


def validation(age,citizen,disqualified):
    try:
        age = int(age)
    except ValueError:
        print("Ошибка: возраст необходимо ввести целым числом!")
        return
    if citizen not in ("да", "нет") or disqualified not in ("да", "нет"):
        print("Ошибка: введите только «да» или «нет»!")
        return
    can_vote(age,citizen,disqualified)


def can_vote(age,citizen,disqualified):
    if age >= 18 and citizen == "да" and disqualified == "нет":
        print("Вы можете голосовать!")
    else:
        print("Вы не можете голосовать.")

input_data()