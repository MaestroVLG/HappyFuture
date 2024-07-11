class House:
    numberOfFloors = 10

    def __init__(self):
        pass

house = House()

for floor in range(1, house.numberOfFloors + 1):
    print(f"Текущий этаж равен {floor}")