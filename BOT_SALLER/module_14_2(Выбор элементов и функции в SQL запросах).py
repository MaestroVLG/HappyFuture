import sqlite3

# Создание и подключение к базе данных
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Создание таблицы Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Заполнение таблицы 10 записями
users_data = [
    ('User1', 'example1@gmail.com', 10, 1000),
    ('User2', 'example2@gmail.com', 20, 1000),
    ('User3', 'example3@gmail.com', 30, 1000),
    ('User4', 'example4@gmail.com', 40, 1000),
    ('User5', 'example5@gmail.com', 50, 1000),
    ('User6', 'example6@gmail.com', 60, 1000),
    ('User7', 'example7@gmail.com', 70, 1000),
    ('User8', 'example8@gmail.com', 80, 1000),
    ('User9', 'example9@gmail.com', 90, 1000),
    ('User10', 'example10@gmail.com', 100, 1000)
]

cursor.executemany("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", users_data)

# Обновление balance у каждой 2-й записи начиная с 1-й
cursor.execute("UPDATE Users SET balance = balance - 500 WHERE id % 2 = 1")

# Удаление каждой 3-й записи начиная с 1-й
cursor.execute("DELETE FROM Users WHERE id % 3 = 1")

# Выборка всех записей по возрасту
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
records = cursor.fetchall()

# Вывод записей в заданном формате
# for record in records:
#     username, email, age, balance = record
#     print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

# Удаление записи с id = 6
cursor.execute("DELETE FROM Users WHERE id = 6")

# Подсчет общего количества записей
cursor.execute("SELECT COUNT(*) FROM Users")
total_records = cursor.fetchone()[0]
print(f"Общее количество записей: {total_records}")

# Подсчет суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
total_balance = cursor.fetchone()[0]
print(f"Сумма всех балансов: {total_balance}")

# Вычисление среднего баланса
if total_records > 0:
    average_balance = total_balance / total_records
else:
    average_balance = 0

print(f"Средний баланс всех пользователей: {average_balance}")
# Сохранение изменений и закрытие соединения
connection.commit()
connection.close()
