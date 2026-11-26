def sum_list():
    my_list1 = [1,2,3,4,5]
    my_list2 = [6,7,8,9,10]
    my_list3 = []

    for i in range(len(my_list1)):
        my_list3.append(my_list1[i] + my_list2[i])

    print(my_list3)

sum_list()