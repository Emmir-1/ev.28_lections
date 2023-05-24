import peewee 
from models import Category, Product
import random


def add_category(name):
    try: 
        obj = Category(title=name.lower().strip())
        obj.save()
        print(f'Сохранили категорию {obj} - {obj.title}')
    except (peewee.IntegrityError, peewee.InternalError):
        print(f'{name.lower().strip()} - эта категория уже существут')

# add_category('laptops')
# add_category('   computers   ')
# add_category('Sony Playstations')
# add_category('Tablets')
# add_category('earphones')


def add_product(name, price, category_name):
    category_name = category_name.lower().strip()
    try:
        category = Category.get(title = category_name)
        # print(category, category.title, category.created_at)
    except peewee.DoesNotExist:
        print(f'Категории {category_name} не существует!')
    else:
        obj = Product(title = name, price = price, category_id = category)
        obj.save()
        print(f'Сохранили товар {obj} - {obj.title}')


# add_product('Sony Playstation 5', 1000, 'sony playstations')
# add_product('assus megabook', 1000, 'laptops')
# add_product('Acer Swift', 1000, 'laptops')
# add_product('Iphone 14 pro', 1500, 'смартфоны')
# add_product('Samsung S23', 1400, 'смартфоны')
# add_product('Airpod Pro', 500, 'earphones')
# add_product('MacBook', 1000, 'Laptops')

import peewee 
from models import Category, Product
import random


def add_category(name):
    try:
        obj = Category(title=name.lower().strip())
        obj.save()
        print(f'сохранили категорию {obj} - {obj.title}')
    except (peewee.IntegrityError, peewee.InternalError):
        print(f'{name.lower().strip()} - эта категория уже существует')

# add_category('laptops')
# add_category('computers')
# add_category('earphones')
# add_category('Sony Playstation')
# add_category('Tablets')


def add_product(name, price, category_name):
    category_name = category_name.lower().strip()
    try:
        category = Category.get(title=category_name)
        # print(category, category.title, category.created_at, '!!!!!')
    except peewee.DoesNotExist:
        print(f'Категории {category_name} не существует!')
    else:
        obj = Product(title=name, price=price, category_id=category)
        obj.save()
        print(f'сохранили товар {obj} - {obj.title}')

# add_product('PS 5', 700, 'sony playstation')

# add_product('asus megabok', 1000, 'laptops')
# add_product('acer swift', 1100, 'laptops')
# add_product('iphone 14 promax', 1300, 'smartphones')
# add_product('Samsung s22', 1000, 'smartphones')
# add_product('airpods 2', 200, 'earphones')
# add_product('Macbook air m1', 900, 'Laptops')
# add_product('Toshiba ZT', 400, 'laptops')
# add_product('HP nv', 800, 'laptops')

# ----------------------------
# добавление новых данных

add_category('smartphones')


# with open ('files/cars.txt', 'r') as file:
#     ls = file.readlines()
#     print(ls)
#     for x in ls:
#         name = x.strip()
#         price = random.randint(5_000, 20_000)
#         add_product(name, price, 'cars')


with open ('files/telefon.txt', 'r') as file:
    ls = file.readlines()
    for x in ls:
        print(x)
        name = x.strip()
        price = random.randint(5_000, 20_000)
        add_product(name, price, 'smartphones')


