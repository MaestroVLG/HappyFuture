team_num1 = 5
print('В команде Мастера кода участников: %s!' % team_num1)
team_num2 = 6
print('Итого сегодня в командах участников: %s и %s!' % (team_num1, team_num2))
score_1 = 30
print('Команда Волшебники данных решила задач: {}!'.format(score_1))
score_2 = 40
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
team1_time = 18014.2
print('Команда Волшебники данных решила задач: {} c'.format(team1_time))
team2_time = 20000.9
print('Команда Волшебники данных решила задач: {} c'.format(team2_time))
print(f'Команды решили {score_1} и {score_2} задач!')

if score_1 > score_2 == score_2 and team1_time > team2_time:
    print("Победа команды Мастера кода!")
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    print('Победа команды Волшебники Данных!')
else:
    print('Ничья')

task_total = int(score_1 + score_2)
print(f'Сегодня было решено {task_total} задач')
all_time_for_task = int(team1_time+team2_time)
print(f'Общее время решения задач составило: {all_time_for_task} с!')
time_avg = (float(all_time_for_task) / int(task_total))
print(f"Середнее время на решении задачи: {time_avg} с!")
print(f"Сегодня было решено {task_total} задач, в среднем по {time_avg} секунды на задачу!.")





