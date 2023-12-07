def fib(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Пример использования функции для генерации чисел Фибоначчи
if __name__ == "__main__":
    n = 200

    # Генерация n чисел Фибоначчи
    fibonacci_sequence = list(fib(n))

    # Вывод числа Фибоначчи под номером 200
    print(f"Число Фибоначчи под номером {n}: {fibonacci_sequence[-1]}")
