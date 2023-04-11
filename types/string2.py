# str 
# ''
# 'hello'
# str(5)

# print(dir(str))
# print(dir(int))

# a = 'hello'
# b = 'john'
# # print(a != b)
# # print('abc' == 'abc')
# print(a > b)
# print(b < a)

# print('a') # 97 -> 1100001
# print('a' > 'b') # 97 > 98
# print('h' > 'c') # 104 > 99 
# print("hello" > "harry") # True
# print("abc" > "abc") # False

# len() - возращает количество символов в строке

# a = 'Hello'
# b = 'John Snow'
# print(len(a) < len(b))
# print(len(a), len(b))

# >, <, ==, !=, >=, <=

# Методы сторк
# replace(old, new, [count]) - меняет в строке символы old на new, если вы укажите count, то замеенит count раз

# text ='ha ha ha ha'
# result = text.replace('a', 'e', 2) 
# print(text)
# print(f'result after replace: {result}')

# str1 = ("hello world! my name is john snow")
# res = str1.replace("john snow", "emmir")
# print(res)

# strip - он убирает пробельные символы в начале и в конце сторки 
# rstrip, lstrip

# a = '   Hello   '
# print(len(a))
# print(a)
# res = a.strip()
# print(res)
# print(len(res))
# print(dir(str))

# isdigit   -          Проверяет
# isnumeric - ->  состоит ли наша строка
# isdecimal -      полностью из чисел 

# num = input("Ведите число: ")
# print(f"Введено число: {num.isdigit()}")

# num = input("Ведите число: ")
# if num.isdigit():
#     num = int(num)
#     print(f"{num} * 5 = {num * 5}")
# else:
#     print("Вы ввели не числа!")

# text = "\u0031"
# print(text)
# print(text.isnumeric())
# print(text.isdecimal())
# print(text.isdigit())


# isalnum() -> проверяет состоит ли наша сторка из чисел и символов латинского алфавита и киррилицы
# str1 = "56你好"
# print(str1.isalnum())
# str2 = "56_a"
# print(str2.isalnum())

# isalpha -> состоит ли наша строка полностью из символов алфавита

# text = "hello world"
# res = text.replace(" ", "")
# print(res)
# print(res.isalpha())


# islower() -> Находит нижний ригстры
# isupper() -> Находит все верхний ригистры
# istitle() -> Нахоит верхний ригистры

# str1 = "Ms. My Name"
# print(str1.islower())
# print(str1.istitle())
# str2 = "RTY UIOP"
# print(str2.isupper())


# index(value, [start], [end]) -> выводит индекс значение value, которые передаем, в нашей строке.

# text = "hello John Snow"
# print(text.index("John"))

# text = "Hello world! My name is John Snow!"
# # print(text.index("John"))
# res = text.index("o")
# print(res) #4
# res = text.index("o", res + 1)
# print(res) #7
# res = text.index("o", res + 1)
# print(res) #25
# res = text.index("o", res + 1)
# print(res)#31

# count(value, [star]) - считает количество вхождений value в нашу строку

# text = "hello o o o hello"
# print(text.count("o"))
# print(text.count("hello"))

# split(separator) - дробит нашу строку на несколько частей по разделителю, все части строк сохраниются в в типе list

# text = "Let me speak by my hearth in English! Cause my name John Snow!"
# res = text.split(" ")
# print(res)
# print(len(res))


# a = "#hello#hello#hello#hello"
# res = a[1:].split("#") #a[1:] - срез начлао с 1
# print(res)

# "connector".join(list) -> соединяет по connector строки которые находились в list

# text = "Let me speak by my hearth in English! Cause my name John Snow!"
# res = text.split(" ")
# print(res)
# str1 = " ".join(res)
# print(str1)


# find(value [start], [end]) -> Делает то же самое что и index но если не нашел возрощает -1

# text = "helo"
# print(text.find("l"))
# print(text.find("lytui"), type(text.find("lytui")))
# print("John Snow")

# swapcase() - переводит все символы в противоположний регистр
# upper() - переводит все в верхний регистр
# lower() - перводит все в нижний регистр

# text = "Hello WorLD, JOHN snow"
# print(f"Original: {text}")
# print(text.upper())
# print(text.lower())
# print(text.swapcase())


# copitalize() - переводит самый первый сивол в верхний регистр
# titlle() - переводит первые символ все слов в верхний регистр
          # john.capitalize() -> John
# name = input("Введите имя:").capitalize()
# print(name)
# print(f"Hello! Mr/Mrs {name}!")

# fio = "JOHN edart snow"
# print(fio.title())
# print(fio.capitalize())

# print(dir(str))