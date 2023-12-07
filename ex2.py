def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            if not content:
                raise ValueError("Файл пустой")
            else:
                print("Информация из файла:")
                print(content)
    except ValueError as ve:
        print(f"Исключение: {ve}")


if __name__ == "__main__":
    # Попробуем считать данные из пустого файла
    print("Попытка считать данные из пустого файла:")
    read_file("empty_file.txt")

    print("\n" + "-"*30 + "\n")

    # Попробуем считать данные из непустого файла
    print("Попытка считать данные из непустого файла:")
    read_file("non_empty_file.txt")
