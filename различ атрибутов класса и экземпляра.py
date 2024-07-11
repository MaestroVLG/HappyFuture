class Building:
    total = 0  # Атрибут класса для подсчета общего количества объектов

    def __init__(self):
        Building.total += 1  # Увеличиваем общий счетчик при создании нового объекта
        self.id = Building.total  # Присваиваем объекту уникальный идентификатор

    def __repr__(self):
        return f"Building(id={self.id})"  # Возвращаем строковое представление объекта


# Создаем 40 объектов класса Building в цикле и выводим их на экран
buildings = [Building() for _ in range(40)]
for building in buildings:
    print(building)