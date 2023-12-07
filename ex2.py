def fib(n):
    a, b = 1, 1
    count = 0
    with open("fib.txt", "w") as file:
        while count < n:
            file.write(f"{a}\n")
            yield a
            a, b = b, a + b
            count += 1

# Пример использования функции для генерации чисел Фибоначчи и записи их в файл
if __name__ == "__main__":
    n = 200

    # Генерация n чисел Фибоначчи и запись их в файл
    list(fib(n))

    print(f"Число Фибоначчи под номером {n}: записано в файл 'fib.txt'")
