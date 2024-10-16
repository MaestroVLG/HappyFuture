import sqlite3

def initiate_db(db_name='products.db'):
    #Создает таблицу Products, если она еще не создана.
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


    # SQL запрос для создания таблицы
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

def get_all_products(db_name='products.db'):

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # SQL запрос для получения всех продуктов
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    conn.close()
    return products

def populate_db(db_name='products.db'):

    #Заполняет таблицу Products
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    #Добавление данных в таблицу
    products = [
        ('Product1', 'Описание продукта 1', 100),
        ('Product2', 'Описание продукта 2', 200),
        ('Product3', 'Описание продукта 3', 300),
        ('Product4', 'Описание продукта 4', 400),
    ]

    #Вставка данных в таблицу
    cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', products)

    conn.commit()
    conn.close()
