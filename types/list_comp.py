# list comprehension - это генераторы списка 
# list comprehension - упрощенный подход к созданию списков , который задействует в себе цикл for , 
# а также конструкцию if для определения того, что бы итоге попадет в наш список.

# list ->  0 - 200 -> num % 2 == 0

# ls =[]
# for x in range(0, 201):
#     if x % 2 == 0:
#         ls.append(x)
# print(ls)

# ls = [x for x in range(0, 201) if x % 2 !=0]
# print(ls)

# list: 0 - 300 - -> num % 2 == 0, num % 3 == 0
# ls = []
# for x in range(0, 301):
#     if x % 2 == 0 and x % 3 == 0:
#         ls.append(x)
# print(ls)

# ls = [i for i in range(0, 300) if i % 2 == 0 and i % 3 == 0]
# print(ls)
# ls = [x for x in range(0,201) if x % 2 != 0]
# print(ls)

# list: 0 - 300 -> num % 2 == 0, num % 3 == 0
# ls = []
# for x in range(0, 301):
#     if x % 2 == 0 and x % 3 == 0:
#         ls.append(x)
# print(ls)

# ls = [i for i in range(0,301) if i % 2 == 0 and i % 3 == 0]
# print(ls)

# list: 0 - 100 -> x % 2 == 0 : x ** 2, i % 3 == 0: x ** 3
# ls = []
# for x in range(0,101):
#     if x % 2 == 0:
#         ls.append(x ** 2)
#     elif x % 3 == 0:
#         ls.append(x ** 3)
# print(ls)
# print(5 if input() == "yes" else 7)

# ls = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(0, 101)if x % 2 ==0 or x % 3 == 0]
# print(ls)

# -------------------------------------------------------------------------------------------------
# newlist = [expression for item in intarabel <if condition == True>] Синтаксис цикла for в ком-не.

# ls = [str(i * 2) for i in range (0, 11)]
# print(ls)

# ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# #reualt = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# res = []
# for x in ls:
#     for item in x:
#         res.append(item)
# print(res)

# ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# res = [item for x in ls for item in x]
# print(res)

# -------------------------------------------------------------------------------------------------

# from datetime import datetime
# start = datetime.now() #19.55.43
# ls = [x for x in range(0, 100_000_000)]
# # ls = []
# # for x in range(0, 100_000_000):
# #     ls.append(x)
# finish = datetime.now() # 19.57.46
# print(finish - start)

# -------------------------------------------------------------------------------------------------

#set compehensions
# set_ = {x for x in range(1, 100)}
# print(set_, type(set_))

# -------------------------------------------------------------------------------------------------

# dict compehensions
# dict = {
#     key : value,
#     key : value
# }
# dict_ = {x: x ** 2 for x in range(0, 16)}
# print(dict_)

# names = ["John", "Tirion", "Eygan", "Sansa", "Ramsi"]
# dict_ = {x: len(x) for x in names}
# print(dict_)

# -------------------------------------------------------------------------------------------------


# dict1 = {
#     'Soke': {'history': 99, 'fizik': 95, 'math': 94},
#     'Omke': {'history': 84, 'math': 86, 'fizik': 68},
#     'Jonh': {'history': 100, 'math': 90, 'fizik': 87}
# }
# res = {}
# for key, value in dict1.items():
#     for inner_key, inner_value in value.items():
#         if max(value.values()) == inner_value:
#             res[key] = inner_key
# print(dict1)
# print(res)

# dict1 = {
#     'Soke': {'history': 99, 'fizik': 95, 'math': 94},
#     'Omke': {'history': 84, 'math': 86, 'fizik': 68},
#     'Jonh': {'history': 100, 'math': 90, 'fizik': 87}
# } 
# res = {key: inner_key for key, value in dict1.items() for inner_key, inner_value in value.items() if inner_value == max(value.values())}
# print(res)


# -------------------------------------------------------------------------------------------------

# try:
#     n = int(input("Введите число: "))
# except ValueError:
#     print("invalid nomber")
# else:
#     dict_ = {x: x ** 2 for x in range(1, 501) if x % n == 0 }
#     print(dict_)