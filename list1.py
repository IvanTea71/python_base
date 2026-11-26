def create_list():
    my_list = ["one","two","three","four","five"]
    print(my_list)
    my_list[0], my_list[-1] = my_list[-1], my_list[0]
    print(my_list)


create_list()
