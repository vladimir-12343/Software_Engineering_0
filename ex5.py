def main():
    list_1 = [1, 1, 3, 3, 1]
    list_1.sort()
    list = []
    number = list_1[0]
    str1 = ""
    for item in list_1:
        if number == item:
            number = item
            str1 += str(item)
            list.append(str1)
        else:
            number = item
            str1 = ''
            str1 += str(item)
            list.append(str1)
    for item in list:
        if len(item) == 1:
            list.remove(item)
            list.insert(0, int(item))
    print("Вывод программы -", list)

if __name__ == "__main__":
    main()
