import time

class ExecutionTimeDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция {self.func.__name__} выполнилась за {execution_time:.4f} секунд")
        return result

# Примеры функций, к которым мы применим наш декоратор
@ExecutionTimeDecorator
def example_function_1():
    print("Выполняется функция 1")
    time.sleep(2)

@ExecutionTimeDecorator
def example_function_2():
    print("Выполняется функция 2")
    time.sleep(1)

if __name__ == "__main__":
    print("Пример работы собственного декоратора")

    print("\nВызов функции 1:")
    example_function_1()

    print("\nВызов функции 2:")
    example_function_2()
