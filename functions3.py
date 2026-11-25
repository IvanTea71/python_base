def object_info(obj):
    try:
        length = len(obj)
    except TypeError:
        length = "не определена"
    finally:
        obj_type = type(obj).__name__
        print(f"Объект: {obj}, Тип: {obj_type}, Длина: {length}")


my_text = "Python"
my_list = [1, 2, 3, 4, 5]
my_tuple = (10, 20, 30)
my_dict = {"name": "Ivan", "age": 25}
my_int = 123
my_objects = [my_text, my_list, my_tuple, my_dict, my_int]

for i in my_objects:
    object_info(i)