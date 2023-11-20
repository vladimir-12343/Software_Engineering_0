# Определение базового класса
class Person:
    def __init__(self, name, age):
        self.__name = name  # Приватный атрибут
        self.__age = age  # Приватный атрибут

    # Метод для вывода информации о человеке
    def show_info(self):
        print(f"Имя: {self.__name}, Количество лет: {self.__age}")


# Определение класса-наследника
class Employee(Person):
    def __init__(self, name, age, position):
        # Вызов конструктора базового класса
        super().__init__(name, age)
        # Дополнительный атрибут для класса-наследника
        self.position = position

    # Метод для изменения приватных атрибутов
    def update_info(self, new_name, new_age):
        self.__name = new_name
        self.__age = new_age

    def show_info(self):
        # Вызов метода базового класса
        super().show_info()
        print(f"Position: {self.position}")


class Manager(Person):
    def __init__(self, name, age, department):
        # Вызов конструктора базового класса
        super().__init__(name, age)
        # Дополнительный атрибут для класса-наследника
        self.department = department

    def show_info(self):
        # Вызов метода базового класса
        super().show_info()
        print(f"Department: {self.department}")


# Создание объектов разных классов
person1 = Person("Анна Иванова", 30)
employee1 = Employee("Иван Иванов", 25, "Software Developer")
manager1 = Manager("Мария Петрова", 35, "Human Resources")

# Функция, использующая полиморфизм
def display_info(person):
    person.show_info()

# Вызов функции с разными объектами
display_info(person1)
display_info(employee1)
display_info(manager1)11
