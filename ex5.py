import copy


def print_hi(name):

    str = input()
    my_list = []
    my_list1 = []
    for num in str:
        #Проверяю по символьно на число или нет, если число, то добавляю элемент в my_list.
        if num.isdigit():
            #Проверяем на четность нечетность
            if int(num) % 2 == 0:
                my_list.append(int(num))
                my_list.sort()
            else:
                my_list1.append(int(num))
                my_list1.sort()
    #Конкатенация списков
    print(my_list + my_list1)

if __name__ == '__main__':
    print_hi('PyCharm')
