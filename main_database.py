import random
import sqlite3
from sqlite3 import Error

connection = sqlite3.connect("test_base.db")
cursor = connection.cursor()

"""Класс создает исходную базу данных и заполняет таблицы случайными значениями"""


class CreateDatabase:
    """Метод объединяет создание таблиц и заполнение"""

    def create_database(self):
        self.create_test_tables()
        self.inserting_data_into_test_tables()
        print("База создана")

    """Метод создает таблицы в базе"""

    def create_test_tables(self):
        try:
            sql_create_weapons_table = '''
                CREATE TABLE IF NOT EXISTS weapons 
                ('weapon' text PRIMARY KEY NOT NULL, 
                'reload speed' integer,
                'rotational speed' integer, 
                'diameter' integer,
                'power volley' integer, 
                'count' integer)
            '''
            cursor.execute(sql_create_weapons_table)
            connection.commit()

            sql_create_hulls_table = '''
                CREATE TABLE IF NOT EXISTS hulls 
                ('hull' text PRIMARY KEY NOT NULL, 
                'armor' integer,
                'type' integer, 
                'capacity' integer)
            '''
            cursor.execute(sql_create_hulls_table)
            connection.commit()

            sql_create_engines_table = '''
                CREATE TABLE IF NOT EXISTS engines 
                ('engine' text PRIMARY KEY NOT NULL, 
                'power' integer,
                'type' integer)
            '''
            cursor.execute(sql_create_engines_table)
            connection.commit()

            sql_create_ships_table = '''       
                CREATE TABLE IF NOT EXISTS ships 
                ('ship' text PRIMARY KEY NOT NULL, 
                'weapon' text,
                'hull' text,
                'engine' text,
                FOREIGN KEY (weapon)
                    REFERENCES weapons (weapon),
                FOREIGN KEY (hull)
                    REFERENCES hulls (hull),
                FOREIGN KEY (engine)
                    REFERENCES engines (engine))
            '''
            cursor.execute(sql_create_ships_table)
            connection.commit()
        except Error:
            print("Ошибка при создании таблиц в исходной базе")

    """Заполняем созданные таблицы данными"""

    def inserting_data_into_test_tables(self):
        try:
            records_weapons = [
                [f'Weapon-{row_count}',
                 random.randint(1, 20),
                 random.randint(1, 20),
                 random.randint(1, 20),
                 random.randint(1, 20),
                 random.randint(1, 20)
                 ] for row_count in range(1, 21)
            ]
            cursor.executemany('INSERT INTO weapons VALUES (?, ?, ?, ?, ?, ?);', records_weapons)
            connection.commit()

            records_hulls = [
                [f'Hull-{row_count}',
                 random.randint(1, 5),
                 random.randint(1, 5),
                 random.randint(1, 5)
                 ] for row_count in range(1, 6)
            ]
            cursor.executemany('INSERT INTO hulls VALUES (?, ?, ?, ?);', records_hulls)
            connection.commit()

            records_engines = [
                [f'Engine-{row_count}',
                 random.randint(1, 6),
                 random.randint(1, 6),
                 ] for row_count in range(1, 7)
            ]
            cursor.executemany('INSERT INTO engines VALUES (?, ?, ?);', records_engines)
            connection.commit()

            for row in range(1, 201):
                cursor.execute(
                    f'INSERT INTO ships VALUES("Ship-{row}", (SELECT weapon FROM weapons ORDER BY RANDOM() LIMIT '
                    f'1), (SELECT hull FROM hulls ORDER BY RANDOM() LIMIT 1), (SELECT engine FROM engines '
                    f'ORDER BY RANDOM() LIMIT 1))')
                connection.commit()

        except Error:
            print("Ошибка при заполнении таблиц")

    """Метод для печати полученых таблиц - метод для отладки"""

    def printing_tables(self):
        try:
            cursor.execute('SELECT * FROM weapons')
            weapon_rows = cursor.fetchall()

            for row in weapon_rows:
                print(row)

            cursor.execute('SELECT * FROM hulls')
            hulls_rows = cursor.fetchall()

            for row in hulls_rows:
                print(row)

            cursor.execute('SELECT * FROM engines')
            engines_rows = cursor.fetchall()

            for row in engines_rows:
                print(row)

            cursor.execute('SELECT * FROM ships')
            ships_rows = cursor.fetchall()
            for row in ships_rows:
                print(row)
        except Error:
            print('Ошибка при выводе таблиц')


main_db = CreateDatabase()
main_db.create_database()
