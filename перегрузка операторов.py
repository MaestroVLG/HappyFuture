# class Buiding:
#     def __init__(self):
#         self.numberOfFloors = 0
#         self.buildingType = "0"
#
#     def __eq__(self, other):
#         return
#     other.numberOfFloors == self.buildingType


class Building:
    def __init__(self, numberOfFloors: int, buildingType: str):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        if isinstance(other, Building):
            return (self.numberOfFloors == other.numberOfFloors and
                    self.buildingType == other.buildingType)
