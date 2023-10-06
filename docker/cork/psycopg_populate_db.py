import psycopg2
import os

dbname = os.environ.get('POSTGRES_HOST')
dbuser = os.environ.get('POSTGRES_HOST')
dbpswd = os.environ.get('POSTGRES_HOST')
conn = psycopg2.connect(f'dbname={dbname} user={dbuser} password={dbpswd}')
cur = conn.cursor()

conn = psycopg2.connect()
with conn:
    with conn.cursor() as curs:
        cur.execute('INSERT INTO cork_location (name, adress, slug) VALUES (%s, %s, %s)',
                    ('Питер: Лахта', 'адрес', 'lahta'))
        cur.execute('INSERT INTO cork_location (name, adress, slug) VALUES (%s, %s, %s)',
                    ('Москва: Кисельный', 'адрес', 'kiselny'))
        cur.execute('INSERT INTO cork_location (name, adress, slug) VALUES (%s, %s, %s)',
                    ('Туапсе: Агой', 'адрес', 'agoy'))
        cur.execute('INSERT INTO cork_location (name, adress, slug) VALUES (%s, %s, %s)',
                    ('Крым: Узунджа', 'адрес', 'uzunja'))
        cur.execute('INSERT INTO cork_location (name, adress, slug) VALUES (%s, %s, %s)',
                    ('Томск', 'адрес', 'tomsk'))
        cur.execute('INSERT INTO cork_location (name, adress, slug) VALUES (%s, %s, %s)',
                    ('Удаленно', 'адрес', 'distant'))

        cur.execute('INSERT INTO cork_regualrity (name) VALUES (%s)',
                    ('Постоянно'))
        cur.execute('INSERT INTO cork_regualrity (name) VALUES (%s)',
                    ('Срочно'))
        cur.execute('INSERT INTO cork_regualrity (name) VALUES (%s)',
                    ('Единожды'))

        cur.execute('INSERT INTO cork_location (header, text, location, regularity, manager) VALUES (%s, %s, %s)',
                    ('Удаленно', 'адрес', 'distant'))

conn.close()
