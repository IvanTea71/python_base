def book_list_view(library):
    if not library:
        print("В библиотеке нет книг.")
        return

    print("Список книг в библиотеке:")

    for book in library:
        print(book)


def add_book(title, author, year):
    if title.lower() in library:
        answer = input(f"Книга \"{title}\" уже существует. Обновить информацию? (да/нет): ")

        if answer.lower() == "да":
            library[title]["author"] = author
            library[title]["year"] = year
            print(f"Информация о книге \"{title}\" успешно обновлена.")
        else:
            print("Обновление отменено.")

    else:
        library[title] = {
            "author": author,
            "year": year,
            "available": None
        }
        print(f"Книга \"{title}\" успешно добавлена.")


def remove_book(title):
    if title.lower() in library:
        del library[title]
        print(f"Книга \"{title}\" успешно удалена.")
    else:
        print(f"Книга \"{title}\" не найдена.")


def issue_book(title):
    if title in library:
        library[title]["available"] = False
        print(f"Книга \"{title}\" успешно выдана.")
    else:
        print(f"Книга \"{title}\" не найдена в библиотеке.")


def return_book(title):
    if title in library:
        library[title]["available"] = True
        print(f"Книга \"{title}\" успешно возвращена.")
    else:
        print(f"Книга \"{title}\" не найдена в библиотеке.")


def find_book(title):
    if title in library:
        print(f"Название: {title}")
        print(f"Автор: {library[title]['author']}")
        print(f"Год издания: {library[title]['year']}")

        if library[title]["available"] is None:
            print("Книга в библиотеке, но ее статус не определен")
        elif library[title]["available"] is False:
            print("Книга выдана")
        else:
            print("Книга доступна")

    else:
        print(f"Книга \"{title}\" не найдена в библиотеке.")


def show_menu():
    print("\nМеню библиотеки:")

    for number, item in menu.items():
        print(f"{number}. {item[0]}")


library = {
    "Мастер и Маргарита": {
        "author": "Михаил Булгаков",
        "year": 1967,
        "available": True
    },
    "Преступление и наказание": {
        "author": "Фёдор Достоевский",
        "year": 1866,
        "available": True
    },
    "Война и мир": {
        "author": "Лев Толстой",
        "year": 1869,
        "available": True
    }
}

menu = {
    1: ("Показать список книг", book_list_view),
    2: ("Добавить книгу", add_book),
    3: ("Удалить книгу", remove_book),
    4: ("Выдать книгу", issue_book),
    5: ("Вернуть книгу", return_book),
    6: ("Найти книгу", find_book),
    0: ("Выход", None)
}

while True:
    show_menu()

    try:
        choice = int(input("Выберите пункт меню: "))

        if choice not in menu:
            print("Такого пункта меню нет.")
            continue

        elif choice == 0:
            print("Программа завершена.")
            break

        elif choice == 1:
            menu[choice][1](library)

        elif choice == 2:
            title = input("Введите название книги: ")
            author = input("Введите автора: ")
            year = int(input("Введите год издания: "))
            menu[choice][1](title, author, year)

        else:
            title = input("Введите название книги: ")
            menu[choice][1](title)

    except ValueError:
        print("Ошибка! Введите корректное числовое значение.")