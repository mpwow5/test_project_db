from main_database import cursor, connection
import pytest


@pytest.mark.parametrize('row', [i for i in range(1, 201)])
def test_weapon(temp_database, row):

    #  Получаем строку из исходной таблицы с weapon и из измененной

    sql_select_row_from_first_table_weapon = f'''
    SELECT 
    ships.weapon, "reload speed", "rotational speed", diameter, "power volley", count  
    FROM ships 
    JOIN weapons ON ships.weapon = weapons.weapon where ships.ship = 'Ship-{row}'
    '''
    cursor.execute(sql_select_row_from_first_table_weapon)
    first_table_weapon = cursor.fetchone()
    connection.commit()

    sql_select_row_from_second_table_weapon = f'''
    SELECT 
    ships.weapon, "reload speed", "rotational speed", diameter, "power volley", count  
    FROM temp_db.ships 
    JOIN temp_db.weapons ON temp_db.ships.weapon = temp_db.weapons.weapon WHERE temp_db.ships.ship = 'Ship-{row}' 
    '''

    cursor.execute(sql_select_row_from_second_table_weapon)
    second_table_weapon = cursor.fetchone()
    connection.commit()

    weapon_parameters = [f"Weapon-{row}", "reload speed", "rotational speed", "diameter", "power volley", "count"]

    for n in range(0, len(first_table_weapon)):
        if n == 0:
            assert first_table_weapon[0] == second_table_weapon[0], \
                f'Ship-{row}, {first_table_weapon[0]} ' \
                f'expected {second_table_weapon[0]} was {first_table_weapon[0]}'
        else:
            assert first_table_weapon[n] == second_table_weapon[n], \
                f'Ship-{row}, {first_table_weapon[0]} {weapon_parameters[n]}: ' \
                f'expected {first_table_weapon[n]}, was {second_table_weapon[n]} '


@pytest.mark.parametrize('row', [i for i in range(1, 201)])
def test_hull(temp_database, row):

    #  Получаем строку из исходной таблицы с hull  и из измененной

    sql_select_row_from_first_table_hull = f'''
    SELECT ships.hull, armor, type, capacity
    FROM ships 
    JOIN hulls on ships.hull = hulls.hull WHERE ships.ship = 'Ship-{row}'
    '''
    cursor.execute(sql_select_row_from_first_table_hull)
    first_table_hull = cursor.fetchone()
    connection.commit()

    sql_select_row_from_second_table_hull = f'''
    SELECT ships.hull, armor, type, capacity 
    FROM temp_db.ships 
    JOIN temp_db.hulls ON temp_db.ships.hull = temp_db.hulls.hull WHERE temp_db.ships.ship = 'Ship-{row}' 
    '''

    cursor.execute(sql_select_row_from_second_table_hull)
    second_table_hull = cursor.fetchone()
    connection.commit()

    hull_parameters = [f"Hull-{row}", "armor", "type", "capacity"]

    for n in range(0, len(first_table_hull)):
        if n == 0:
            assert first_table_hull[0] == second_table_hull[0], \
                f'Ship-{row}, {first_table_hull[0]} ' \
                f'expected {second_table_hull[0]} was {first_table_hull[0]}'
        else:
            assert first_table_hull[n] == second_table_hull[n], \
                f'Ship-{row}, {first_table_hull[0]} {hull_parameters[n]}: ' \
                f'expected {first_table_hull[n]}, was {second_table_hull[n]} '


@pytest.mark.parametrize('row', [i for i in range(1, 201)])
def test_engine(temp_database, row):

    #  Получаем строку из исходной таблицы с engine и из измененной

    sql_select_row_from_first_table_engine = f'''
    SELECT ships.engine, power, type 
    FROM ships 
    JOIN engines ON ships.engine = engines.engine WHERE ships.ship = 'Ship-{row}'
    '''
    cursor.execute(sql_select_row_from_first_table_engine)
    first_table_engine = cursor.fetchone()
    connection.commit()

    sql_select_row_from_second_table_engine = f'''
    SELECT ships.engine, power, type 
    FROM temp_db.ships 
    JOIN temp_db.engines ON temp_db.ships.engine = temp_db.engines.engine WHERE temp_db.ships.ship = 'Ship-{row}'
    '''

    cursor.execute(sql_select_row_from_second_table_engine)
    second_table_engine = cursor.fetchone()
    connection.commit()

    engine_parameters = [f"Weapon-{row}", "reload speed", "rotational speed", "diameter", "power volley", "count"]

    for n in range(0, len(first_table_engine)):
        if n == 0:
            assert first_table_engine[0] == second_table_engine[0], \
                f'Ship-{row}, {first_table_engine[0]} ' \
                f'expected {second_table_engine[0]} was {first_table_engine[0]}'
        else:
            assert first_table_engine[n] == second_table_engine[n], \
                f'Ship-{row}, {first_table_engine[0]} {engine_parameters[n]}: ' \
                f'expected {first_table_engine[n]}, was {second_table_engine[n]} '
