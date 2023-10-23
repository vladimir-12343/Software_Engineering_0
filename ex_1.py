"""
В это строке мы ипортируем datetime из datetime
"""
from datetime import datetime

"""
В это строке мы ипортируем sqrt из модуля math
"""
from math import sqrt

"""
В это строке создаем функцию main
"""
def main(**kwargs):
    """
    перебираем все значения представленные в словаре kwargs
    """
    for key in kwargs.items():
        """
            формула Пифагора для вычисления длины гипотенузы
        """
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
        """
            Возвращаем результат
        """
        print(result)


"""
   Делаем проверку в каком контексте мы находимся 
"""
if __name__ == "__main__":
    """
        Записываем в переменную start_time текущую дату и время 
    """
    start_time = datetime.now()
    """
        Передаем в main именнованные аргументы 
    """
    main(
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )
    """
        Присваиваем time_costs время выполнения программы 
    """
    time_costs = datetime.now() - start_time
    """
        Вывод времени выполнения прграммы 
    """
    print(f"Время выполнения программы - {time_costs}")
