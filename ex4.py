def print_hi(name):

    str = input()
    my_list = []
    my_list1 = []
    count = 0
    for num in str:
        #Проверяю по символьно на число или нет, если число, то добавляю элемент в my_list.
        if num.isdigit():
            my_list.append(int(num))
            if str[len(str)-2] == num:
                my_list1.append(count)
            count += 1
    try:
        my_list.pop(len(my_list) - 1)
        print(tuple(my_list[my_list1[0]:my_list1[1]+1]))
    except:
        print(())


if __name__ == '__main__':
    print_hi('PyCharm')
