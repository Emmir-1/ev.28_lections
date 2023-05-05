from views import CreateMixin, ReadMixin, UpdateMIxin, DeleteMixin
import json
class Product(CreateMixin, ReadMixin, UpdateMIxin, DeleteMixin):
    def save(self):
        with open("data.json", "w") as file:
            json.dump(self.objects, file, indent=4)
        return "Saved!"
    
class Comment(CreateMixin, ReadMixin, DeleteMixin):
    pass


smartphones = Product()
print(smartphones.post(title="Redmi Not 10", description="The best phone", qty = 5, price = 500))
print(smartphones.post(title="Redmi Not 20", description="The Good phone", qty = 10, price = 250))
print(smartphones.post(title="Iphone 14 Pro Max", description="Super Phone", qty = 6, price = 750))
print(smartphones.post(title="Samsung S23", description="Nice Good Phone", qty = 3, price = 700))
print(smartphones.post(title="Iphone 13 Pro Max", description="Super nice Phone", qty = 5, price = 650))
print()
print()
print(smartphones.list())
print()
print(smartphones.detail(4))
print(smartphones.detail(14))
print()
print(smartphones.patch(1, title="Redmi Note 9"))
print()
print(smartphones.list())
print()
print(smartphones.delete(-1))
print(smartphones.delete(1))
print(smartphones.save())
