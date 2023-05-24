from models import Product, Category
 
# query = Product.update(price = 1_000_000).where(Product.id == 5)
# print(query)
# query.execute()

# query = Product.update(title = 'Airpod Pro').where(Product.title == 'Airpods Pro')
# print(query, '!!!')
# query.execute()


# query = Product.update(price =(Product.price * 1.5))
# query.execute() # Увеличиваем всем товарам


# Удаление данных

# product = Product.get(Product.id == 5)
# print(product, product.title)
# product.delete_instance()
# print(product)

#postgres(__---__---__)
# query = Category.delete().where(Category.id == 6)
# query.execute()



