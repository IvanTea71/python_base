text = input("Введите текст: ")
text = text.lower()

for symbol in ".,!?;:()\"'":
    text = text.replace(symbol, "")

words = text.split()

# 1. Количество слов
print("Количество слов:", len(words))

# 2. Самое длинное слово
if words:
    longest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    print("Самое длинное слово:", longest_word)
else:
    print("Текст не содержит слов")

# 3. Количество гласных
vowels = "аеёиоуыэюя"
vowel_count = 0

for symbol in text:
    if symbol in vowels:
        vowel_count += 1

print("Количество гласных:", vowel_count)

# 4. Частота появления каждого слова
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Повторения слов:")

for word, count in word_count.items():
    print(word, "-", count)