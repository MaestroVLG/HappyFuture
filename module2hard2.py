#Задача на треугольник

a = input("Введите первое число ", )
b = input("Введите второе число ", )
c = input("Введите третье число ", )
print(a, b, c)

if a == b == c:
   print('Равносторонний треугольник')

elif a == b or b == c or a == c:
    print("Равнобердренный треугольник")

else:
    print("Разносторонний треугольник")


#Задача на серединное число

a = input("Введите число ", )
b = input("Введите число ", )
c = input("Введите число ", )

if a < b < c or c < b < a:
    sred_znach = b
elif b < a < c or c < a < b:
    sred_znach = a
else:
    sred_znach = c

print("Серединное значение ", sred_znach)

#Задача на смешение цветов
color1 = input("Введите букву первого цвета (а=красный, b=синий, c=жёлтый): ")
color2 = input("Введите букву второго цвета (а=красный, b=синий, c=жёлтый): ")

a = "красный"
b = "синий"
c = "жёлтый"

if (color1 == 'a' and color2 == 'b') or (color1 == 'b' and color2 == 'a'):
    color = "фиолетовый"
elif (color1 == 'a' and color2 == 'c') or (color1 == 'c' and color2 == 'a'):
    color = "оранжевый"
elif (color1 == 'b' and color2 == 'c') or (color1 == 'c' and color2 == 'b'):
    color = "зелёный"
else:
    color = "Такая комбинация невозможна"

print(color)

#Звёздный треугольник

n = int(input("Введите натуральное число: "))

for i in range(n, 0, -1):
    print('*' * i)

#Фрагмент таблицы умножения

a, b, c, d = map(int, input("Введите четыре натуральных числа через пробел: ").split())

print('\t'.join([''] + [str(j) for j in range(c, d + 1)]))
for i in range(a, b + 1):
    print('\t'.join([str(i)] + [str(i * j) for j in range(c, d + 1)]))


#Численный треугольник
n = int(input("Введите натуральное число: "))
counter = 1

for i in range(1, n + 1):
    for j in range(i):
        print(counter, end=' ')
        counter += 1
    print()







