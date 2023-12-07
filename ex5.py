class CustomException(Exception):
    pass

def validate_positive_number(value):
    try:
        if value < 0:
            raise CustomException("Значение не может быть отрицательным")
        else:
            print("Значение корректно:", value)
    except CustomException as ce:
        print(f"Перехвачено собственное исключение: {ce}")

def process_integer_value(value):
    try:
        if not isinstance(value, int):
            raise CustomException("Ожидалось целочисленное значение")
        else:
            print("Функция выполнена успешно")
    except CustomException as ce:
        print(f"Перехвачено собственное исключение: {ce}")

if __name__ == "__main__":
    print("Пример использования собственного исключения")

    # Первый фрагмент кода
    print("\nВызов функции 1:")
    validate_positive_number(5)

    print("\nВызов функции 1 с отрицательным значением:")
    validate_positive_number(-3)

    # Второй фрагмент кода
    print("\nВызов функции 2 с корректным значением:")
    process_integer_value(10)

    print("\nВызов функции 2 с некорректным значением:")
    process_integer_value("abc")
