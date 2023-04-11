"""
Встроеные функции
"""
"""
Анонимные функции - lambda (Обычная функция с одной особенностью, у нее нет имени)
Принимает сколько угодно параметров, но всегда возрощает одно выражение
"""


# x = lambda : "hello" # return под копотом
# print(x())

# x = lambda a, b, c: (a * b) % c
# print(x(5, 5, 2))

# x = lambda num1, num2, degreen = None: (num1 * num2) ** degreen if degreen else num1 * num2
# print(x(2, 2, 3))
# print(x(5, 5))

# def myFunc(n):
#     return lambda num: num * n

# my_double = myFunc(2)
# print(my_double(50))


# list_ = ["hello", "bil", "John", "Ayana"]
# a = sorted(list_, key = len, reverse=True)
# print(a)


# dict_ = {
#     "john": 500,
#     "tirion":160_000,
#     "tom": 150,
#     "sanchar": 20,
#     "Ayana": 100_000,
# }
# print(dict_.items())
# new_dict = dict(sorted(dict_.items(), key = lambda x: x[1], reverse = True))
# print(new_dict)

"""
map(function, iterable) - применяет к каждому элементу внтури intrable функцию, которую мы ей передаем в function, 
закидываем в результате те данные, которые возращает функция. 
В результате мы получаем mapobject(iterator), в котором
хранятся все наши данные.
"""

# ls = ["1", "2", "3"]

# new_list = list(map(lambda x: x.capitalize(), ls)) # map проходит по циклу и меняет его - передает функцию 
# print(new_list)

# new_list = list(map(int, ls))
# print(new_list)


# names = ["john", "Ayana", "baku", "bakberdi", "lilo"]
# name = list(map(lambda x: f"hello mr/mrs {x}", names))
# print(name)

"""
Функция высшего порядка - функия, которая принимает в качестве аргумента другю функицию
"""

"""
filter(function, interable) - применяет ко всем элементам interable функицию, которую мы пременяем и
возращаем filterobject(итератор) только с тем элементами, для которых функция вернуля True
"""
# ls = ["one", "lili", "oleg", "billi"]
# res = list(filter(lambda x: len(x) >= 4, ls))
# print(res)


"""
enumerate(inteable) - пронумеровывает каждый элемент внутри iterable ее собственным индексом
"""

# ls = ["str1", "str2", "str3"]
# new_list = list(enumerate(ls))
# print(new_list)



