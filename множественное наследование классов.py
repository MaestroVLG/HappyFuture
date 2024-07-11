class Vehile:
    def __init__(self):
        self.vehile_type = None

class Car:
    def __init__(self, powers):
        self.price = 1000000
        self.power = powers


    def hourse_powers(self):
       return self.power

class Nissan(Car, Vehile):
    def __init__(self, powers):
        super().__init__(powers)
        self.price = 99966
        self.vehile_type = None

    def hourse_powers(self):
        print('power Nissan')
        return self.power

car = Nissan(300)

print(car.hourse_powers(), car.price, car.vehile_type)






