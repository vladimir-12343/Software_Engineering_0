def main():
    my_list = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]
    copy_list = my_list.copy()
    leng = len(my_list)
    my_list.sort()
    print("Три лучшие результата -", my_list[0:3])
    print("Три худшие результата -", my_list[leng-3:leng])
    print("Все результаты начиная с 10 -", copy_list[10:])

if __name__ == "__main__":
    main()
