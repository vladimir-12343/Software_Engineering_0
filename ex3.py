def print_hi(name):

    my_dic = {}
    #Убираем повторные числа путем проверки, если ключ уже есть в my_dic, то пропускаем, иначе добавляем.
    for num in name:
        if num not in my_dic.keys():
            my_dic[int(num)] = int(name.count(num))
    #Сортируем по значениям. В качестве ключа сортировки мы используем лямбда-функцию lambda x: x[1], которая указывает, что мы хотим сортировать по второму элементу
    sortedValue_dic = sorted(my_dic.items(), key=lambda x: x[1])[-3:]
    # Сортируем по Ключу из оставшихся 3-х
    sortedKey_dic = sorted(sortedValue_dic)
    print("(Цифра(Key), Count(Values))", sortedKey_dic)



if __name__ == '__main__':
    print_hi('000000000000000213')
