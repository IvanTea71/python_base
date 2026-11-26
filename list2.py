def sum_list():
    my_list1 = [1,2,3,4,]
    my_list2 = [6,7,8,9,10]
    my_list3 = []
    max_length = max(len(my_list1), len(my_list2))

    for i in range(max_length):
        num1 = my_list1[i] if i < len(my_list1) else 0
        num2 = my_list2[i] if i < len(my_list2) else 0
        my_list3.append(num1 + num2)

    print(my_list3)

sum_list()