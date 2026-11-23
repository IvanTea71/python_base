#Создаём переменные разных типов
num_int,num_float,text,items_list,items_tuple,data_dict,data_set = (67, 3.14, "67", [1, 2, 3], (4, 5, 6), {"a": 1},
{7, 8, 9})
# Выводим тип каждой переменной
print(f"{num_int}: {type(num_int)}", f"{num_float}: {type(num_float)}", f"{text}: {type(text)}",
      f"{items_list}: {type(items_list)}", f"{items_tuple}: {type(items_tuple)}", f"{data_dict}: {type(data_dict)}",
      f"{data_set}: {type(data_set)}")
# Строку, содержащую число, в целое число
converted_int = int(text)
print(converted_int)
# Число с плавающей точкой в строку
converted_str = str(num_float)
print(converted_str)
# Список в кортеж
converted_tuple = tuple(items_list)
print(converted_tuple)
# Целое число в список, содержащий это число
converted_list_from_int = [num_int]
print(converted_list_from_int)