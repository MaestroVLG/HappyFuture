num = int(input("Введите число от 3 до 20: "))

result = ""

for i in range(1, num + 1):
    for j in range(1, num + 1):
        if num % (i + j) == 0 and i != j and i < j:
            result += str(i) + str(j)

print(result)












