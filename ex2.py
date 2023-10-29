def print_hi(name):

    str = input()
    my_list = []
    for num in str:
        #Проверяю по символьно на число или нет, если число, то добавляю элемент в my_list.
        if num.isdigit():
            my_list.append(int(num))

    # Удаляем последний элемент в my_list по индексу и сохраняем его в number
    number = my_list.pop(len(my_list)-1)
    # Обработка исключения на случай, если не нужно будет удалять первое
    try:
        # Удаляем первое входение в my_list
        my_list.remove(number)
        # созданием кортеж из итерируемого объекта списка.
        my_tuple = tuple(my_list)
        print(my_tuple)
    except:
        # созданием кортеж из итерируемого объекта списка.
        my_tuple = tuple(my_list)
        print("Вывод кортежа", my_tuple)




if __name__ == '__main__':
    print_hi('PyCharm')
