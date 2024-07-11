class Road:
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance

class Warehouse:
    def __init__(self, name, content=0):
        self.name = name
        self.content = content
        self.set_road_out = None
        self.queue_in = []
        self.queue_out = []

    def __str__(self):
        return 'Склад {} груза {}'.format(self.name, self.content)

    def set_road_out(self, road):
        self.set_road_out = road

    def truck_arrived(self, truck):
        self.queue_in.append(truck)
        print('{} прибыл грузовик'.format(self.name, self.truck))

    def get_next_truck(self):
        if self.queue_in:
            truck = self.queue_out.pop()
            return truck

    def truck_ready(self, truck):
        self.queue_out.append(truck)
        print('{} грузовик готов'.format(self.name, self.truck))

    def act(self):
        while self.queue_out:
            truck = self.queue_out.pop()
            truck.go_to(road=self.road_out)

class Vehicle:
    fuel_rate = 0
    total_fuel = 0

    def __init__(self, model):
        self.model = model
        self.fuel = 0

    def __str__(self):
        return '{} топливо {}'.format(*args self.model, self.fuel)

    def tunk_up(self):
        self.fuel += 1000
        vehicle.total_fuel += 1000
        print('{} заправился '.format(self.model)

    def act(self):
            if self.fuel <= 10:
                self.tunk_up()
                return False
            return True

class Truck(Vehicle):
        fuel_rate = 50
        dead_time = 0

    def __init__(self,model, body_space=1000):
        super(self).__init__(model = model)
        self.body_space = body_space
        self.cargo = 0
        self.velocity = 100
        self.place = None
        self.distance_to_target = 0

    def __str__(self):
        res = super().__str__()
        return  res + 'груза {}'.format(self.cargo)

    def ride(self):
        self.fuel -= self.fuel_rate
        if self distance_to_target > self.velocity:
            self.distance_to_target -= self.velocity
            print('{} едет по дороге, осталось {}'.format(self.model, self.distance_to_target))
        else:
            self.place = self.place.end
            self.place.truck_arriver(self)
            print('{} доехал'.format(self.model)


    def go_to(self, road):
        self.place = road
        self.distance_to_target = road.distance
        print('{} выехал в путь'.format(self.model))

    def act(self):
        super().act()
            if isinstance(self.place, Road):
                self.ride()
            else:
                Truck.dead_time += 1



class AutoLoader(Vehicle):
    fuel_rate = 30

    def __init__(self, model, bucket_capacity=100, warehouse=None, role='loader'):
        super().__init__(model = model)
        self.bucket_capacity = bucket_capacity
        self.warehouse = warehouse
        self.role = role
        self.truck = None

    def __str__(self):
        res = super().__str__()
        return res + 'груза {}'.format(self.truck)

    def act(self):
        super().act()
        if self.truck is None:
            self.truck = self.warehouse.get_next_truck()
            print('{} взял в работу {}'.format(self.model, self.truck ))
        elif self.role == 'loader':
            self.load()
        else:
            self.unload()
            if self.truck is None:
                Truck.dead_time +=1

    def load(self):
        self.fuel -= self.fuel_rate
        truck_cargo_rest = self.truck.body_space - self.truck.cargo
        if truck_cargo_rest >= self.bucket_capacity:
            self.warehouse.content -= self.bucket_capacity
            self.truck.cargo += self.truck.bucket.capacity
        else:
            self.warehouse.content -= truck_cargo_rest
            self.truck.cargo += truck_cargo_rest
        print('{} грузил {}'.format(self.model, self.truck))
        if self.truck.cargo = self.truck.body_space:
            self.warehouse.truck_ready(self.truck)
            self.truck = None

    def unload(self):
        self.fuel -= self.fuel_rate
        if self.truck_cargo >= self.bucket_capacity:
            self.warehouse.content -= self.bucket_capacity
            self.truck.cargo += self.truck.bucket.capacity
        else:
            self.warehouse.content -= self.truck_cargo
            self.truck.cargo += self.truck_cargo
        print('{} разгружал {}'.format(self.model, self.truck))
        if self.truck.cargo == 0:
            self.warehouse.truck_ready(self.truck)
            self.truck = None

TOTAL_CARGO = 10000

moscow = Warehouse(name='Москва', content=TOTAL_CARGO)
piter = Warehouse(name='Питер', content=0)

moscow_piter = Road(start=moscow, end=piter, distance=715)
piter_moscow = Road(start=piter, end=moscow, distance=780)

moscow.set_road_out(moscow_piter)
piter.set_road_out(piter_moscow)

loader_1 = AutoLoader(model='hellcat', bucket_capacity=1000, warehouse=moscow, role='loader')
loader_2 = AutoLoader(model='volvo', bucket_capacity=500, warehouse=piter, role='unloader')

trucks = []
for number in range(5):
    moscow.truck_arrived()
    truck_1 = Truck(model='Камаз #{}'.format(number), body_space=5000)
    moscow.truck_arrived(truck)
    trucks.append(truck)

# truck_2 = Truck(model='Газель', body_space=2000)
# truck_3 = Truck(model='BMW', body_space=5000)

# moscow.truck_arrived(truck_1)
# moscow.truck_arrived(truck_2)
# moscow.truck_arrived(truck_3)

hour = 0
while piter.content < TOTAL_CARGO:
    hour += 1
    cprint('.................ЧАС {} ............'.format(hour), color = 'red')
    for truck in trucks:
        truck.act
    # truck_1.act()
    # truck_2.act()
    # truck_3.act()
    loader_1.act()
    loader_2.act()
    moscow.act()
    piter.act()
    for truck in trucks:
        cprint(truck, color = 'green')
    cprint(truck_1, color = 'green')
    cprint(truck_2, color='green')
    cprint(truck_3, color='green')
    cprint(loader_1, color='green')
    cprint(loader_2, color='green')
    cprint(moscow, color='green')
    cprint(piter, color='green')



cprint('всего затрачено топлива {}'.format(Vehicle.total_fuel), color='yellow')