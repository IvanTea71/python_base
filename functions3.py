def object_info(obj):
    try:
        length = len(obj)
        obj_type = type(obj).__name__
        return f"Объект: {obj}, Тип: {obj_type}, Длина: {length}"

    except TypeError:
        obj_type = type(obj).__name__
        return f"Объект: {obj}, Тип: {obj_type}, Длина: не определена"

text = "Python"
list = [1, 2, 3, 4, 5]
tuple = (10, 20, 30)
dict = {"name": "Ivan", "age": 25}
int = 123
objects = [text, list, tuple, dict, int]

for i in objects:
    print(object_info(i))