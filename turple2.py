def book_list_view(library):
    if not library:
        print("В библиотеке нет книг.")
        return

    print("Список книг в библиотеке:")

    for book in library:
        print(book)

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

book_list_view(library)