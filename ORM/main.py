# ORM(Object-Relation Mapping)- технология програмирование благодоря которой разработчики могут использовать язык програмирование для взаимо действия с реаляционой базой данных (PostgresSQL, MySQL и.т.д)
# Вместо того чтобы писать сырые запросы (операторы SQL), вы будете писать код на языке программироание. Это очень сильно ускоряет разработку приложение и БД, особенно на начальных этапах.

from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'orm_db',
    user ='admin',
    password ='1',
    host ='localhost', # 127.0.0.1 
    port =5432
)

# a = db.connect()
# print(a)






