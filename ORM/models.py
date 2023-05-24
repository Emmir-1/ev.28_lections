import peewee 
from playhouse.migrate import migrate, PostgresqlMigrator
from main import db 
from datetime import datetime


class Category(peewee.Model):
    id = peewee.PrimaryKeyField()
    title = peewee.CharField(max_length = 20, unique = True)
    created_at = peewee.DateTimeField(default=datetime.now())
    

    class Meta:
        database = db
        db_tabble = 'categories'
        order_by = ('created_at',)

class Product(peewee.Model):
    id = peewee.PrimaryKeyField()
    title = peewee.CharField(max_length=500)
    price = peewee.DecimalField(max_digits=10, decimal_places=2, default = 100)
    category_id = peewee.ForeignKeyField(Category, to_field='id', 
                                         related_name='products')
    created_at = peewee.DateTimeField(default=datetime.now())



    class Meta:
        database = db
        db_tabble = 'products'
        order_by = ('created_at',)


db.connect()    
# Category.create_table()
Product.create_table()

# - - - - - - - - - - - - - - - - migrate(изменение БД)

# migrator = PostgresqlMigrator(db)
# migrate(
#     migrator.alter_column_type('product', 'title', peewee.TextField())
# )





