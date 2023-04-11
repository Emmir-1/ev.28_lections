# Типы данных числа -> int, float 

# = -> оператор присваивания
# variable(переменная)
# num = 5
# print(num) # 5
# num = 79 #переопределение
# print(num) # 79

# abc -> нижний ригистр 
# ABC -> верхний ригистр

# PEP8 прочитать
# tomorrow_day = "10.03.2023" # Snake case
# tomorrowDay = "10.03.2023" #Camel case

# num1 = 5
# num2 = 15 
# result = num1 + num2
# print("Summa:", result)

# - 

# num1 = input("Enter the num1:" ) # -> "5"
# num2 = input("Enter the num2:" ) # -> "7"
# num1 = int(num1)
# num2 = int(num2)
# print(num2, "-", num1, "=", num2 - num1)

# * 
# num1 = int(input("Enter the num1: "))
# num2 = int(input("Enter the num2: "))
# print(num2, "*", num1, "=", num1 * num2)

# / and // and %
# / - обычное деление
# // - деление без остатка
# % - модульное деление(получение остатка от деления)

# num1 = 2.9
# num2 = 2
# print("/", num1 / num2)
# print("//", num1 // num2)
# print("%", num1 % num2)


# ** -> возведение в степень
# print(5 ** 2)
# print(16 ** 55)

# print(9 ** 0.5) # квадратные корень 

# pow - возведение в степень 
# pow(num1, num2, <mod>)
# print(pow(5, 10, 65))
# print(5 ** 10 % 65)

# a = 5 
# b = 2 
# res = pow (a, b, 12) 
#          #5 ** 2 = 25 % 12 = 1 
# print(res)

# round() - округление числа с плавающей точкой 
# a = 5.368232
# print (round(a, 2))

# abs() - абсолютное значение числа -> abs(-5) -> 5
#                                         |-5| -> 5
# a = abs(-16)
# b = abs(15)
# print(a, b)

# divmod(a, b) -> Она выводит два числа, первое число это результат целочисленого деление(//) a на b, а второе это модульное деление(%)

# res = divmod(5, 2)
# print(res)
# print((5 // 2, 5 % 2))

# import math

# a = 5
# print(round(math.sqrt(a), 2))
# res = math.sqrt(a)
# print(round(res, 2))


# множественое присваивание 
# опрератор присваивание 
# a = 5
# b = 15
# c = None

# print("a:", a, "b:", b)

# # c = a 
# # a = b
# # b = c
# a, b = b, a
#        #15, 5
# print("a:", a, "b:", b)


# num1, num2, num3 = input("Num1: "), input("Num2: "), input("Num3: ")
# print(num1)
# print(num2)
# print(num3)
# from math import pi 

# import math
# print (math.pi)
# print(pi, type(pi))

# r = int(input("Vvedite radius: "))
# res_P = 2 * r * pi
# res_S = pi * (r ** 2) 
# print ("S okruznosti", round(res_S, 2))
# print ("P okruznosti", round (res_P, 2))


# from random import randint 

# # print(randint(1, 10))
# name = input('Vvediti svoe imya:')
# last_name = input('Vvedite svou familiu:')
# num = randint(1_000_000, 9_999_999)
# # print(name, last_name, num)
# res = name + last_name + str(num)
# print(res)


# from random import randint 
# num = randint(1, 10)
# print(num)
# i = 0 
# while i < 3:
#     guess = int(input('Угодай число: '))
#     if guess == num:
#         print('Ты победил: ')
#         break 
#     # i = i + 1
#     i += 1 # Инкримент 


# inp1=int(input()) inp2=int(input()) inp3=int(input()) res=inp1*inp2%inp3 print(res)

    