age = int(input("Введите ваш возраст: "))
citizen = input("Вы гражданин страны? (да/нет): ")
disqualified = input("Вы дисквалифицированы? (да/нет): ")

if age >= 18 and citizen == "да" and disqualified == "нет":
    print("Вы можете голосовать!")
else:
    print("Вы не можете голосовать.")