def object_info(obj):
    length = len(obj)
    obj_type = type(obj)
    return length, obj_type

text = "Python"
list = [1, 2, 3, 4, 5]
tuple = (10, 20, 30)
dict = {"name": "Ivan", "age": 25}

print(object_info(text))
print(object_info(list))
print(object_info(tuple))
print(object_info(dict))