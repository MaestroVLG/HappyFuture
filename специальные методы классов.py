class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)

house = House()
print(f"Изначальное количество этажей: {house.numberOfFloors}")

house.setNewNumberOfFloors(input("Введите этаж, "))
print(f"Новое количество этажей: {house.numberOfFloors}")