grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_studens = sorted(students)

sredniy_bal = {}

for i in range(len(sorted_studens)):
    student_grade = sum(grades[i]) / len(grades[i])
    student_name = sorted_studens[i]
    sredniy_bal[student_name] = student_grade

print(sredniy_bal)























#sredniy_bal = sum(grades[idx]) / len(students[idx])



