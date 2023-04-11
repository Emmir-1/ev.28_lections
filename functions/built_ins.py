#zip(itrebles) - она соединяет каждый элемент интерируемых объектов между собой в тип данных tuple и возвращает итератор

# ls1 = [1, 2, 3]
# ls2 = [100, 200, 300]

# res = dict(zip(ls1, ls2)) # list, tuple
# print(res)


# ls1 = [1, 2, 3, 4, 5]
# ls2 = [100, 200, 300, 400, 500, 600]
# ls3 = [10, 20, 30]
# res =list(zip(ls1, ls2, ls3))
# print(res)


# zip для создания словарей 
# d_keys = ["hostname", "location", "vendor", "model", "IP"]
# data = {
#     "oktbr": ["Bishkek_oktbr", "Gorkaya 212", "Vefa", "Cisco", "10.255.0.12"],
#     "1may": ["Bishkek_1may", "Jibek-jolu 212", "Belyi Dom", "Clok", "11.233.0.24"],
#     "Alarcha": ["Bishkek_Alarcha", "Bokonbaeva 99", "Magazin", "Apple", "14.293.0.69"]
# }

# Bishkek_data = {}

# for k in data:
#     Bishkek_data[k] = dict(zip(d_keys, data[k]))


# print(Bishkek_data)


# -----------------------------------------------------------------------------------------------
# all(), any()

# all(iterable) - Возращает True, если все элементы итерируемого объекта истина, иначе False

# ls = [5 ,6, 7, [2]]
# print(all(ls)) #-> True 

# ip = "10.255.0.155" # True
# ip1 = "10.125.0y.202" # False


# result = all(x.isdigit() for x in ip.split("."))
# print(result)

# any - Возращает True, если хотябы один элемент истинна 

# ls = (0, 0, [1], 0)
# print(any(ls))

# ignore = ["rm - rf", "sudo", "reset", "poweroff"]
# command = input("Введите команду: ") # rm dir test
#             # False, False, False
# if any(x in command for x in ignore):
#     raise Exception("Block you!")

# print("OK!")

# -----------------------------------------------------
# from random import choices 
# from string import ascii_letters, digits
# from itertools import repeat

# symbols = "_()+-@!#%"
# q_pass = int(input("Введите количество паролей: "))

# result = {
#     f(choices(ascii_letters, k = 15), choices(digits, k = 6), choices(symbols, k = 2))
#     for f in repeat(lambda x, y, z: "".join(set(x + y + z)), q_pass)
# }

# print(result)
# print(f"Quantity of password: {len(result)}")

# from statistics import mean 

# print(f"Средняя длина паролей: {mean(len(x)for x in result)}")



