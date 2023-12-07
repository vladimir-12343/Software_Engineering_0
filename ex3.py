def add_two_and_input():
    try:
        user_input = input("Введите число: ")
        # Пробуем преобразовать введенное значение в число
        user_number = float(user_input)

        # Складываем 2 и введенное число
        result = 2 + user_number
        print(f"Результат сложения 2 и введенного числа: {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")



if __name__ == "__main__":
    # Тест с корректным вводом числа
    add_two_and_input()

    # Тест с вводом строки
    add_two_and_input()
