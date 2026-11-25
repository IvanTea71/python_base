def prepare_text(text):
    new_text = ""
    symbols = ".,-!?;:()\"'"
    text = text.lower()

    for letter in text:
        if letter not in symbols:
            new_text += letter

    text = new_text.split()
    return text

def count_words(words):
    print("Количество слов:", len(words))

def longest_word(words):
    if words:
        longest_word = words[0]

        for word in words:
            if len(word) > len(longest_word):
                longest_word = word

        print("Самое длинное слово:", longest_word)
    else:
        print("Текст не содержит слов")

def count_vowels(text):
    vowels = "аеёиоуыэюя"
    vowel_count = 0

    for letter in text:
        if letter in vowels:
            vowel_count += 1

    print("Количество гласных:", vowel_count)

def count_word(words):
    word_count = {}

    for word in words:
        word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print("Повторения слов:")

    for word, count in word_count.items():
        print(word, "-", count)

text = input("Введите текст: ")
prepared_text = prepare_text(text)
count_words(prepared_text)
longest_word(prepared_text)
count_vowels(text)
count_word(prepared_text)

