# PostgreSQL - Система управление базами данных(СУБД/DBMS)
# Это ряд программ и инструментов позволяющих создавать БД, управлять ею и манипулировать данными внутри(CRUD)

# Postgres - сама база данных, она обектно реалиционая, то есть данные хранятся в виде таблиц, и имеют связь между собой

# SQL (Stuctured Query Language) - декларативный язык структированных запросов, он применяется для создания и получение данных при помощи запросов БД 

# -- -- -- -- -- -- -- -- -- -- -- -- 
# Команда для входа в БД через юзера postgres:
# sudo -u postgres psql

# команда для входа 
# exit

# команда входа в своего юзера
# psql

# команда для выхода 
# \q

# Создание юзре
#CREAT ROLE 'username' SUPERUSER LOGIN PASSWORD '1';  #CREATE DATABASE admin;

# изменение пароля 
# ALTER USER 'username' WITH PASSWORD '1';

# создание БД 
# CREAT DATABASE 'name';

# \l - список всех БД

# \du - все юзеры

# \dt - все таблицы (нужно поключится к БД заранее)

# \d 'name' - подробная информация к БД

# \c 'name' - команда для поключение БД

# psql -U <username> -d <dbname> - подключение под выбранным username к dbname

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Типы полей postgres

# Numeric type(числовы типы)
        # a. smallint(2 bytes) -> 32767 to 32767
        # b. integer(4 bytes) -> 2.147... to 2.147...
        # c. bigin(8 bytes) -> ... to ...
        # d. real(4 bytes) -> число с плавающей точкой, вещественное
        # f. double precsion (8 bytes) -> real но с двойной точностью
        # d. serial (4 bytes) -> integer, auto-increment 


# Character Types(Символьные строки(строковые)):
    # a. varchar(кол-символов) -> если мы укажем 50 символов, а заполним только 10 то остальные будут свободны. Макс255
    # b. char(кол-символов) -> если мы укажем 50 символов, а заполним только 10, то остальные будут заполнены пробелами. Макс 255
# 'John'
# 'John _ _ _ _ '
    # c. text() -> неограниченое количество символов.

# Boolen Type
    # a. boolean (1 bytes) -> True/False

# date -> календарная дата (год, месяц, день)

# location -> координатная точка (x, y) - (245, -12)

# enumerate types:
    # ("a", "b", "c")
    # CREAT TYPE <aby name> AS ENUM ("Happy", "Sad", "Mad");


# - - - - - - - - - - - -- - - - - - - 
# Команда для создания таблицы 
# CREAT TABLE <tableName> (
#     <column> <type>,
# )

# CREATE TABLE films (
    # code char(5), 
    # title varchar(100),
    # date date,
    # genre varchar(50),
    # budget integer,
    # country varchar(50),
    # id serial
    # );

# DROP TABLE <name> - удаление таблиц

# Команда для добавление данных в таблицу 
# INSERT INTO <tablename> [(columns)] VALUES (data), (data);

# INSERT INTO films(code, title, date, genre, budget, country) VALUES 
# ('AU56', 'Game of Thrones', '2015-05-31', 'Fantasy', 1000000, 'USA');
# ('het5', 'Lord of The Rings', '2001-06-12', 'Fantasy', 1200000, 'USA');

# Команда для получение данных
# SELECT (colums)* FROM <table>;

# Команда для обнавление данных
# UPDATE <table> SET <column> = <new_value> WHERE <column> = <value>;


# Команда для удаление данных
# DELET FROM <table> WHERE <column> = <value>;

# ORDER BY: Он позволяет нам сортировать выводящие данные по убыванию или по возрастанию. ASC(по возрастанию) и DESC(по убыванию)
# Синтаксис: SELECT <row> FROM <tabelname> ORDER BY <row> = [ASC/DESC];

# WHERE: Используется для фильтраций по полям будут выводится только те данные которые соответсвуют условию оператору WHERE 
# Синтаксис: SELECT <row> FROM <tabelname> WHERE <row> = "Чему либо";


# BERWEEN: условие между
# Синтакси: SELECT * FROM products WHERE id BETWEEN 3 and 8

# LIKE: Выводит результат который соответсвует введеному шаблону для сторк. Чуствителен к ригистру 
# ILEKE: Тоже самое но не зависит от ригистра
# Синтаксис: SELECT <row> FROM <tabelname> WHERE <row> = LIKE/ILIKE 'чему либо';

# AND: Оператор и, для множественых условий 
# IN: WHERE <row> in (1, 2, 3, 4, 5);

# LIMIT: Ставит ограниечение в кол-во получаемых данных

# GROUP BY: разделяет данные котрые мы получаем в SELECT, при этом группируя их по
# определеному признаку. И теперь для каждой группы можно использовать функцию

# HAVING: ставит условия при помощи которго данные отбираются в группировка

# Агрегатные функций: AVG(), COUNT(), MIN(), MAY(), SUM()

# Экспорт БД(дамп): 
# pg_dump -U <username> -d 'dbname' > 'file.sql'

# Импорт:
# psql -U <username> -d <dbname> -f <filename>

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Связи между таблицами(relations)
    # 1.Один к одному (One to One) - человек и пасорт
            # в одну из таблиц добавляется поле fk и дается ограничение unique
    # 2. Один ко многим (One to Many) - человек и банковские карты  
            # в таблицу много(банковских карты) доб. поле fk
    # 3. Много ко многим (Many to Many) - Студенты и преподы
            # создается вспомогательня третья таблица со связями


# Ограничения :
    # 1. NOT NULL - обезятельное к заполнению 
    # 2. UNIQUE - то что будут хранится уникальные данные 
    # 3. CHECK - CHECK age > 0 - ограничение проверки на условие 
    # 4. PRIMERY KEY(для установки индетификатора данных в таблице)
    # 5. FOREIGN KEY(для установки связей между таблицами)
    # 6. ON DELET - для установки поведение при удаление данных которые были связоны 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# JOIN выборака данных из двух таблиц тоесть так назывемое соедине таблиц

# LEFT JOIN выборак будет содержать все строки из левой таблицы 

# RIGHT JOIN выборак будет содержать все строки из правой таблицы 

# SELECT p1.title, p1.price, o1,quantity, p1.price * o1.quantity as
# total_sum FROM products p1, orders o1 WHERE p1.id = o1.product_id;
# - Запрос сразу две 

# SELECT p1.title, p1.price, o1,quantity, p1.price * o1.quantity as
# total_sum FROM products p1 JOIN orders o1 WHERE p1.id = o1.product_id ;




