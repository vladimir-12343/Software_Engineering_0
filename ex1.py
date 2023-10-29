def print_hi(name):

    my_list = input().split(' ')
    my_tuple = tuple(my_list)
    print("Создание кортежа", my_tuple)
    print("Создание списка", my_list)


if __name__ == '__main__':
    print_hi('PyCharm')
