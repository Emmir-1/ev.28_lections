# dict() - Это у нас словарь -> упорядочанная колекция элементов (python 3.7 -> ordered) 
# Каждый элемент внутри словаря хранятся в виде пары:--> {ключа значение}
# Ассоциативный массив, hash table, object(js), structure == dictionary(py)

# Ключами могут быть только не изменяймые типы данных и в словаре сохраняются только уникальные ключи.
# тогда как значениями могут выступать любые типы данных.

# thisdict = {
#     "brand" :"Ford",
#     "model" : "Mustang",
#     "year" : 1967
# }

# print(thisdict)
# print(type(thisdict))
# print(thisdict["brand"], thisdict["model"])
# print(thisdict["year"])

# thisdict["motor"] = "GTE Turbo"
# thisdict["brand"] = "tesla"
# print(thisdict)

# a = {}
# b = dict()

# ------------------------------------------------------------

# # items - выводит все содержимое ключ и элемент, keys - выводит содержимое ключей, values - выводит содержимое элемент
# user_info = {
#     "first_name" : "John",
#     "last_name": "Snow", 
#     "age" : 24,
#     "email" : "johnsnow@gmail.com",
#     "role": "admin",
#  }

# ls = user_info.keys()
# ls = list(ls)
# print(ls[2:])

# ls = list(user_info.values())
# print(ls)

# items = user_info.items()
# print(items)
# print(user_info)
# for value in user_info.values():
#     print(value)

# for key in user_info.keys():
#     print(key)

# print(user_info)
# for key, value in user_info.items():
#     print(f"keys: {key}, values: {value}")

# dict_ = {"name":"Jack", "age":17}
# print(dict_)
# dict_["name"] = "John"
# dict_["age"] = 24
# dict_["address"] = "WinterFell"
# print(dict_)
# dict_.update({"age": 25, "address":"BlackCastle"})
# print(dict_)

# ------------------------------------------------------------

# Получение данных со словаря 
# dict_ = {1: "Pizza", 2: "Burger", 3: "Steak"}
# print(dict_[2], "!!!")
# print(dict_.get(2))
# #setdefault - работает так же как get, но если нет такого ключа то он создает новую пару из этого ключа 
# dict_ = {1: "Pizza", 2: "Burger", 3: "Steak"}
# print(dict_.setdefault(4, "Riba"))
# print(dict_.get(4))
# print(dict_)

#--------------------------------------------------------------------------------
# создания словаря - fromkeys
# ls = list(range(1, 100))
# new_dict = dict.fromkeys(ls, "value")
# print(new_dict)
# ------------------------------------------------------------

# удаление элемнтов 
# pop, popitem
# pop(<key>) - удоляет пару по ключу
# dict_ = {"name" : "John", "last_name" : "Snow"}
# print(dict_)
# removed = dict_.pop("name")
# print(dict_)
# print(removed)

# popitem - удоляет последнию пару

# dict_ = {"name" : "John", "last_name" : "Snow"}
# removed = dict_.popitem()
# print(dict_)
# print(removed)

# ------------------------------------------------------------
# roles = {
#     0: "Admin",
#     1: "Customer",
#     2: "Vendor",
# }
# users = {
#     55: {
#     "id" : 1, "role" : roles[2], "username" : "Tirion",
#     },
#     2: {
#     "id" : 2, "role" : roles[0], "username" : "John Snow",
#     },
#     3:{
#     "id" : 3, "role" : roles[1], "username" : "Raychel",
#     }
# }
# print(users)

# product = {
#     "id": 1,
#     "title" : "Samsung Galaxy A51",
#     "description" : "Lorem Ipsum",
#     "price" : 250
# }
# print(product)
# id_user = int(input("Введите id: ")) # 55
# if users [id_user]["role"] == roles[0]:
#     product["description"] = input("Введите описание: ")
# else:
#     print("You do not have permissions!")

# print(product)
# list_ = [1, 2, 3, 4, 5]
# new_list = list_.split(',', '')
# print(new_list)


