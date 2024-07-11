def draw_area():
    for i in area:
        print(*1)

area[["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
print("Добро пожаловать в крестики-нолики")
print("----------------------------------")
draw_area()
for turn in range(1, 10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char == "0"
        print("Ходят нолики")
    else:
        turn_char = "X"
        print("Ходят крестки")
row = int(input("Введите номер строки (1, 2, 3) ")) - 1
column = int(input("Введите номер столбца (1, 2, 3")) - 1
if area[row][column] == "*":
    area[row][column] = turn_char
else:
    print("Ячейка занята, вы пропускаете ход")
    continue

draw_area()

