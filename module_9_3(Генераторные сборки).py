first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(first[i]) - len(second[i])) for i in range(len(first)))

second_result = (first[i] == second[i] for i in range(len(first)))

print(list(first_result))
print(list(second_result))