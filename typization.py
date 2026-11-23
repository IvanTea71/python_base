a = "1"
b = 2
c = int(a) + b
print(f"Успешное преобразование: {c}, тип результата: {type(c)}")

string = "число"
try:
    d = int(string)
except ValueError as e:
    print(e)

x = 67
print(f"Сначала x = {x}, тип: {type(x)}")

x = "строка"
print(f"Теперь x = {x}, тип: {type(x)}")

