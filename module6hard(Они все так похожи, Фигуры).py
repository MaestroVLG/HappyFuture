import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = [side for side in sides]
        self.__color = [int(c) for c in color]
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, radius)
        self.__radius = radius

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, a, b, c):
        super().__init__(color, a, b, c)
        self.__height = self.__get_height()

    def get_square(self):
        p = sum(self.__sides) / 2
        return math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))

    def __get_height(self):
        s = sum(self.__sides)
        return 2 * self.get_square() / s


# class Cube(Figure):
#
#     sides_count = 12
#
#     def __init__(self, color, side):
#         super().__init__(color, side * 12)
#
#     def get_volume(self):
#         return self._Figure__sides[0] ** 3

class Cube(Figure):
    sides_count = 12

    def init(self, color, *sides):
        super().init(color, sides)
        self.__sides = [sides[0]] * self.sides_count if len(sides) == len([self.sides_count]) else [1] * self.sides_count


    def get_volume(self):
        return self._Figure__sides[0] ** 3



circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
# circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
