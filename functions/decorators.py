# Декораторы -> это функция, которая позволяет без изменения кода функции расширить ее функционал

# def decorator(func):
#     print(func)
#     func()

# def hello():
#     print("Hello stranger!")

# def john():
#     print("My name is John Snow I\'m king of Nirth!")
# №Первый вариант
# decorator(hello)
# print("!!!!!!")
# decorator(john)


# pythonic way -> @
# Cинтаксический сахар - краста кода

# def decorator(func):
#     def wrapper():
#         print(f"Мы вызволи функицию: {func.__name__}")
#         func()
#     return wrapper

# @decorator  # @decotarot == decorator(hello)
# def hello():
#     print("Hello stranger!")

# @decorator
# def john():
#     print("My name is John Snow I\'m king of Nirth!")

# hello()
# print()
# john()

# def bechmark(func):
#     def wrapper(*args, **kwargs):
#         import time 
#         start = time.time() 
#         func(*args, **kwargs)
#         finish = time.time()
#         print(f"Время выполнения функции {func.__name__}, заняло: {finish - start}")
#     return wrapper

# @bechmark
# def loop():
#     i = 0
#     range_number = 1_000_000
#     while i < range_number:
#         # print(i)
#         i += 1

# @bechmark
# def add():
#     i = 0
#     range_number = 1_000_000
#     ls = []
#     while i < range_number:
#         ls.append(i)
#         i += 1
#     print(ls)

# loop(1_000_00)
# print()
# add()

# def bold(func):
#     def wrapper(*args, **kwargs):
#         res = "<bold>" + func(*args, **kwargs) + "</bold>"
#         return res
#     return wrapper

# def div(func):
#     def wrapper(*args, **kwargs):
#         res = "<div>" + func(*args, **kwargs) + "</div>"
#         return res
#     return wrapper


# @bold
# @div
# @bold
# def str_(name):
#     return name 


# print(str_("John Snow"))

# -----------------------------------------------------------------------
# def trace(func):
#     def wrapper(*args, **kwargs):

#         print(f"Trace: вызвла {func.__name__}() \nона приняла args: {args}, kwargs: {kwargs}")
#         original_result = func(*args, **kwargs)
#         print(f"Trace: вызвла {func.__name__}() \nона вернула args: {original_result}")
#         return original_result
#     return wrapper

# @trace
# def say(name, address):
#     return f"{name} --> {address}"

# @trace
# def hello(name, last_name, country):
#     return f"Hello {name} {last_name} from {country}!"

# say("Sherlock Holms", "Bakery street 221B")
# print()
# hello("Homer", "Simpson", "Canada")








