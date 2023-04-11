"Sting - строки"
"Hello world true 5 Nano"

"""
Hello world 
My name Emmir
"""

'''
Hello World s vami Kani
'''

# Строки - Набор последовательных сисволов которые мы используем для храниение и представление текстовой информации



# Индексация в строке 
# name = "John"
#         # J = 0 =- 4
#         # o = 1 =- 3
#         # h = 2 =- 2
#         # n = 3 =- 1 
# print(name)
# print(name[1])
# str1 = "kani"
# print(str1[-1], str1[0])

# str1 = "birthday"
# # print (str1[5], str1[6], str1[7])
# # print (str1[0], str1[1], str1[2], str1[3], str1[4])

# print (str1[5] + str1[6] + str1[7])
# print (str1[0] + str1[1] + str1[2] + str1[3] + str1[4])

# Срезы по индексам 
# # [start: end: <step>]
# str1 = "birthday"
# print(str1[5:])
# print(str1[:5])


# text = "Hello world! My name is Emmir! I'm King of North!"
# # print(text[:13])
# print(text[::])
# print(text[::-1])

# Конкатенация сторк(соеденение)
# a = "Hello"
# b = "world"
# c = " "
# print(a + c + b)

# Экранирование - способы записи символов в строку в которые невазможно ввести с клавиатуры

# \n -> Перенос строки 
# \t -> горизантальная табуляция
# \v -> вертикальная табуляция
# ------------------------------
# \f -> перевод станицы 
# \r -> возрат указателя 
# print("\vHello world!\nMy name Emmir")

# Форматирование сторк 
# 1. спомощью %
# 2. с использование .format()
# 3. Интерполяция строк (приборазование, f-stroki)


# %
# name = input("Введите имя: ")
# last_name = input("Введите Фамилию: ")
# print("Добро пожалоавть к нам " + name + "" + last_name + "!")
# print("Hello mr/ms %s %s!" %(name, last_name))

# .format
# name = input("Введите имя: ")
# last_name = input("Введите Фамилию: ")
# print("Приветствую вас, {} {}, в наш клуб!".format(name, last_name))

# # f-stroki
# a = input("Введите число: ")
# name = input("Введите имя: ")
# last_name = input("Введите Фамилию: ")
# print(f"Hello {a} {name} {last_name}! Welcome to the parthy! ")

# text = "Запомни Питтер, с большой силой приходит и большая овтетсвенность."
# reversed_text = text[::-1]
# # print(reversed_text)
# i = 0
# count_t = 0
# len_text = len(reversed_text)
# # print(len(reversed_text))
# while i < len_text:
#     symbol = reversed_text[i]
#     if symbol == "т" or symbol == "Т":
#         count_t += 1 
#     # print(symbol)
#     i += 1
# print(f"В тексте 'Т' встретилась {count_t} раз!")


