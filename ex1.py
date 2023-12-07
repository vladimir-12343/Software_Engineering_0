class Tomato:
    states = {'Отсутствует': 0, 'Цветение': 1, 'Зеленый': 2, 'Красный': 3}

    def __init__(self, index):
        self._index = index
        self._state = self.states['Отсутствует']

    def grow(self):
        if self._state < len(self.states) - 1:
            self._state += 1

    def is_ripe(self):
        return self._state == len(self.states) - 1


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(1, num_tomatoes + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print("Сбор урожая!")
            self._plant.give_away_all()
        else:
            print("Пока не все томаты созрели. Продолжаем ухаживать.")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:\nСледите за растением, помогайте ему расти и ухаживайте за плодами.\n"
              "Когда все томаты созреют, можно собирать урожай!")


# Тесты
if __name__ == "__main__":
    # Справка по садоводству
    Gardener.knowledge_base()

    # Создаем куст с 5 томатами
    tomato_bush = TomatoBush(5)

    # Создаем садовника, который ухаживает за кустом
    gardener = Gardener("Василий", tomato_bush)

    # Садовник работает и ухаживает за растением
    gardener.work()
    # Садовник пытается собрать урожай, но томаты еще не созрели
    gardener.harvest()

    # Продолжаем ухаживать за растением
    gardener.work()
    # Собираем урожай
    gardener.harvest()
