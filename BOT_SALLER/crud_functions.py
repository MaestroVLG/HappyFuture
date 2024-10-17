import sqlite3

DATABASE_NAME = 'products.db'

def initiate_db():
    """Создает таблицу Products, если она еще не существует."""
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
    """Заполняет таблицу Products начальными данными."""
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

def check_table_structure():
    #Проверка структуры таблицы
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(Products);")
    columns = cursor.fetchall()
    for column in columns:
        print(column)
    conn.close()

def reset_db():
    #Сброс базы данных
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS Products")
    initiate_db()
    conn.close()

# Вызов функции для проверки структуры таблицы
#check_table_structure()

# Вызов функции для сброса базы данных по необходимости
#reset_db()
