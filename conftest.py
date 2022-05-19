from main_database import cursor
from main_database import connection
import random
import pytest


@pytest.fixture(scope='session')
def temp_database():
    # Прикрепляем временную базу данных в соединение
    cursor.execute('ATTACH DATABASE ":memory:" as "temp_db"')
    sql_create_weapons_table = '''
            CREATE TABLE IF NOT EXISTS temp_db.weapons 
            ('weapon' text PRIMARY KEY NOT NULL, 
            'reload speed' integer NOT NULL,
            'rotational speed' integer NOT NULL, 
            'diameter' integer NOT NULL,
            'power volley' integer NOT NULL, 
            'count' integer)
        '''
    cursor.execute(sql_create_weapons_table)
    connection.commit()
    cursor.execute('INSERT INTO temp_db.weapons SELECT * FROM weapons')
    connection.commit()

    sql_create_hulls_table = '''
                    CREATE TABLE IF NOT EXISTS temp_db.hulls 
                    ('hull' text PRIMARY KEY NOT NULL, 
                    'armor' integer NOT NULL,
                    'type' integer NOT NULL, 
                    'capacity' integer NOT NULL)
                '''
    cursor.execute(sql_create_hulls_table)
    connection.commit()
    cursor.execute('INSERT INTO temp_db.hulls SELECT * FROM hulls')
    connection.commit()

    sql_create_engines_table = '''
                    CREATE TABLE IF NOT EXISTS temp_db.engines 
                    ('engine' text PRIMARY KEY NOT NULL, 
                    'power' integer NOT NULL,
                    'type' integer NOT NULL)
                '''
    cursor.execute(sql_create_engines_table)
    connection.commit()
    cursor.execute('INSERT INTO temp_db.engines SELECT * FROM engines')
    connection.commit()

    sql_create_ships_table = '''       
                    CREATE TABLE IF NOT EXISTS temp_db.ships 
                    ('ship' text PRIMARY KEY NOT NULL, 
                    'weapon' text NOT NULL,
                    'hull' text NOT NULL,
                    'engine' text NOT NULL,
                    FOREIGN KEY (weapon)
                        REFERENCES weapons (weapon),
                    FOREIGN KEY (hull)
                        REFERENCES hulls (hull),
                    FOREIGN KEY (engine)
                        REFERENCES engines (engine))
                '''
    cursor.execute(sql_create_ships_table)
    connection.commit()
    cursor.execute('INSERT INTO temp_db.ships SELECT * FROM ships')
    connection.commit()

    # Вносим случайные правки в копию таблицы
    for row in range(1, 21):
        random_num = random.randint(1, 5)
        if random_num == 1:
            column_name = 'reload speed'
            new_value = random.randint(1, 20)
            cursor.execute(
                f'UPDATE temp_db.weapons SET "{column_name}" = {new_value} WHERE weapon = "Weapon-{row}"')
        if random_num == 2:
            column_name = 'rotational speed'
            new_value = random.randint(1, 20)
            cursor.execute(
                f'UPDATE temp_db.weapons SET "{column_name}" = {new_value} WHERE weapon = "Weapon-{row}"')
        if random_num == 3:
            column_name = 'diameter'
            new_value = random.randint(1, 20)
            cursor.execute(
                f'UPDATE temp_db.weapons SET "{column_name}" = {new_value} WHERE weapon = "Weapon-{row}"')
        if random_num == 4:
            column_name = 'power volley'
            new_value = random.randint(1, 20)
            cursor.execute(
                f'UPDATE temp_db.weapons SET "{column_name}" = {new_value} WHERE weapon = "Weapon-{row}"')
        if random_num == 5:
            column_name = 'count'
            new_value = random.randint(1, 20)
            cursor.execute(
                f'UPDATE temp_db.weapons SET "{column_name}" = {new_value} WHERE weapon = "Weapon-{row}"')
        connection.commit()

    for row in range(1, 6):
        random_num = random.randint(1, 3)
        if random_num == 1:
            column_name = 'armor'
            new_value = random.randint(1, 20)
            cursor.execute(f'UPDATE temp_db.hulls SET "{column_name}" = {new_value} WHERE hull = "Hull-{row}"')
        if random_num == 2:
            column_name = 'type'
            new_value = random.randint(1, 20)
            cursor.execute(f'UPDATE temp_db.hulls SET "{column_name}" = {new_value} WHERE hull = "Hull-{row}"')
        if random_num == 3:
            column_name = 'capacity'
            new_value = random.randint(1, 20)
            cursor.execute(f'UPDATE temp_db.hulls SET "{column_name}" = {new_value} WHERE hull = "Hull-{row}"')
        connection.commit()

    for row in range(1, 7):
        random_num = random.randint(1, 2)
        if random_num == 1:
            column_name = 'power'
            new_value = random.randint(1, 20)
            cursor.execute(
                f'UPDATE temp_db.engines SET "{column_name}" = {new_value} WHERE engine = "Engine-{row}"')
        if random_num == 2:
            column_name = 'type'
            new_value = random.randint(1, 20)
            cursor.execute(
                f'UPDATE temp_db.engines SET "{column_name}" = {new_value} WHERE engine = "Engine-{row}"')
        connection.commit()

    for row in range(1, 201):
        random_num = random.randint(1, 3)
        if random_num == 1:
            column_name = 'weapon'
            new_value = 'Weapon-' + str(random.randint(1, 20))
            cursor.execute(
                f'UPDATE temp_db.ships SET "{column_name}" = "{new_value}" WHERE ship = "Ship-{row}"')
        if random_num == 2:
            column_name = 'hull'
            new_value = 'Hull-' + str(random.randint(1, 5))
            cursor.execute(
                f'UPDATE temp_db.ships SET "{column_name}" = "{new_value}" WHERE ship = "Ship-{row}"')
        if random_num == 3:
            column_name = 'engine'
            new_value = 'Engine-' + str(random.randint(1, 6))
            cursor.execute(
                f'UPDATE temp_db.ships SET "{column_name}" = "{new_value}" WHERE ship = "Ship-{row}"')
        connection.commit()

    yield temp_database

    connection.close()
    print("Соединение закрыто")
