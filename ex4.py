def main():
    my_list = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
    my_list1 = []
    for item in my_list:
        if item != 2:
            if item == 3:
                item = 4
            my_list1.append(item)
    print(my_list1)

if __name__ == "__main__":
    main()
