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
    book = library.get(title)

    if book is None:
        library[title] = {
            "author": author,
            "year": year,
            "available": None
        }
        print(f'Книга "{title}" успешно добавлена.')
        return

    answer = input(
        f'Книга "{title}" уже существует. Обновить информацию? (да/нет): '
    )

    if answer.lower() != "да":
        print("Обновление отменено.")
        return

    book["author"] = author
    book["year"] = year
    print(f'Информация о книге "{title}" успешно обновлена.')


add_book("Дубровский", "Александр Пушкин", 1833)