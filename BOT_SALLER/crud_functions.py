import sqlite3

DATABASE_NAME = 'products.db'

def initiate_db():
    #Добавление таблицы Product
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    #Добавление таблицы Users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,  -- Добавлено уникальное ограничение
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL DEFAULT 1000
        )
    ''')
    conn.commit()
    conn.close()

def get_all_products():
    """Возвращает все записи из таблицы Products."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products

def populate_db():

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Удаление старых данных (если необходимо)
    cursor.execute('DELETE FROM Products')

    # Добавление новых данных
    products = [
        ('Product 1', 'Описание продукта 1', 100),
        ('Product 2', 'Описание продукта 2', 200),
        ('Product 3', 'Описание продукта 3', 300),
        ('Product 4', 'Описание продукта 4', 400)
    ]


    cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', products)
    conn.commit()
    conn.close()

#Добавляем нового пользователя в таблицу Users.
def add_user(username, email, age, db_name='products.db'):

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                       (username, email, age, 1000))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Пользователь с таким именем уже существует.")
    finally:
        conn.close()

#Проверка наличия пользователя в таблице Users
def is_included(username, db_name='products.db'):

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT COUNT(*) FROM Users WHERE username = ?', (username,))
        exists = cursor.fetchone()[0] > 0
    finally:
        conn.close()

    return exists

def check_table_structure():
    #Проверка структуры таблицы
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(Products);")
    columns = cursor.fetchall()
    for column in columns:
        print(column)
    conn.close()

#def reset_db():
#     #Сброс базы данных
#     conn = sqlite3.connect(DATABASE_NAME)
#     cursor = conn.cursor()
#     cursor.execute("DROP TABLE IF EXISTS Products")
#     initiate_db()
#     conn.close()

# Вызов функции для проверки структуры таблицы
#check_table_structure()

#Вызов функции для сброса базы данных по необходимости
#reset_db()
