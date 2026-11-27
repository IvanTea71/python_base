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

find_book("Война и мир")