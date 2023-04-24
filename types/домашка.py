# print("Введите ноль чтобы завершит работу программы")
# while True:
#     s = input("Знак (+, -, *, **, //, %, /): ")
#     if s == '0':
#         break
#     if s in ('+', '-', '*', '**', '//', '%', '/'):
#         x = float(input("x ="))
#         y = float(input("y = "))
#         if s == '+':
#             print(" %.2f " % (x + y))
#         elif s == '-':
#             print(" %.2f " % (x - y))
#         elif s == '*':
#             print(" %.2f " % (x * y))
#         elif s == '**':
#             print(" %.2f " % (x ** y))
#         elif s == '//':
#             print(" %.2f " % (x // y))
#         elif s == '%':
#             print(" %.2f " % (x % y))
#         elif s == '/':
#             if y != 0:
#                 print(" %.2f " % (x / y))
#             else:
#                 print("Деление на ноль!")
#     else:
#         print("Неверный знак операции!")

# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon'] 
# letter = input("Enter the first letter of the word you're looking for: ") 
# matching_words = [] 
# for word in list_: 
#     if word.startswith(letter):
#      matching_words.append(word) 
# print(matching_words)

# list_ = [1, 2, 3, 4, 5]
# new_list = list_.append(
# print(new_list)


# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max_list = max(lists, key = len)
# min_list = None
# if lists:
#     min_list = min(lists, key = len)
# if max_list == min_list :
#     min_list=None
# print(max_list)
# print(min_list)

# lists = [ [13],[13]] 
# max_ = max([x for x in lists], 
#            key=len) 
# min_ = None 
# if len(lists) > 1: 
#     min_ = min([x for x in lists],
#                key=len) 
# if max_ == min_: 
#     min_ = None 
# print(f'max_list {max_}') 
# print(f'min_list {min_}')

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max_ = max(lists, key = len)
# min_ = None
# if lists:
#     min_ = min(lists, key = len)
# if max_ == min_:
#     min_ = None
# print(f'max_list {max_}') 
# print(f'min_list {min_}')

# ----------------------------------------------------------------------------
# import random
# guesses_made = 0
# name = input('Привет! Как тебя зовут?\n')
# number = random.randint(1, 30)
# print ('Отлично, {0}, я загадал число между 1 и 30. Сможешь угадать?'.format(name))
# while guesses_made < 6:
#     guess = int(input('Введи число: '))
#     guesses_made += 1
#     if guess < number:
#         print ('Твое число меньше того, что я загадал.')
#     if guess > number:
#         print ('Твое число больше загаданного мной.')
#     if guess == number:
#         break
# if guess == number:
#     print ('Ух ты, {0}! Ты угадал мое число, использовав {1} попыток!'.format(name, guesses_made))
# else:
#     print ('А вот и не угадал! Я загадал число {0}'.format(number))

#-----------------------------------------------------------
# Таск 22

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max_list = max(lists, key=len)
# min_list = min(lists, key=len)
# if len(max_list) == len(min_list):
#     min_list = None
# print("max_list", max_list)
# print("min_list", min_list)
# 16-------
# def to_fahrenheit(k:int) -> float: 
#     assert k >= 0,'Холоднее абсолютного нуля!' 
#     res=(k-273.15)*9/5+32 
#     return res 
# print(to_fahrenheit(3))

# try: 
#     import lamabimgo
# except ModuleNotFoundError: 
#     print('Такого модуля нет')
# def filter_comment(comment: str, banlist=[]) -> None: 
#     words = comment.lower().split() 
#     for word in words:
#         word = word.strip(",.!?") 
#         if word in banlist: 
#             raise ValueError("Ваш комментарий отправлен на перепроверку, так как, возможно, содержит неблагоприятный контекст")

# try:
#     num = 100_000_000 
#     for i in range(0,num): 
#         print('Nope') 
# except KeyboardInterrupt: 
#     print('Nope')
# def collect_all_possibles(list_:
# list, num: 
# int) -> list: 
# result=[] 
# for x in list_:
#     try: 
#         result.append(x*num) 
#         result.append(x+num) 
#         result.append(x-num) 
#         result.append(x**num) 
#         result.append(x//num) 
#     except TypeError: 
#      continue 
# return result

# try: inp1 = input('enter1: ') inp2 = input('enter2: ') print(int(inp1) + int(inp2)) except: print(inp1+inp2)
# inp1=input() res=inp1.split(' ') try: list_=[int(x) for x in res] except ValueError: raise ValueError('Данный элемент не является числом!')


#--------------------------------------------------------------------------------
#  Напишите функцию, которая принимает список чисел и возвращает их произведение
# def num(numbers):
#     result = 1
#     for num in numbers:
#         result *= num
#     return result

# my_numbers = [2, 3]
# print(num(my_numbers))
#--------------------------------------------------------------------------------
# def sq(func):
#     def wrapper(num): # обертка функции
#         # print(num)
#         nums = func(num)
#         return list(map(lambda x: x ** 2, nums))
#     return wrapper 

# @sq 
# def func(num: int):
#     return list(range(1, num))

# @sq
# def func2(num):
#     return list(range(1, num, 2))

# # print(func(5))
# print(func2(6))

#--------------------------------------------------------------------------------

# ls = [1 ,2, 3, 4, 5]
# new_ls = list(map(lambda x: x ** 2 if x % 2 == 0 else x, ls))
# print(new_ls)


# if elif else Условные операторы

# def func21(a:list,b:str)->list: 
#     result=list() 
#     for i in a: 
#         if b.lower() == i['category'].lower(): 
#             result.append(i) 
#             return result

with open('file.txt', 'r') as file:
    lines = file.readlines()
    num_lines = len(lines) 
    num_chars = 0 
    num_words = 0 
    for line in lines:
        num_chars += len(line)
        words = line.split()
        num_words += len(words)
        print(f"Количество символов в строке: {len(line)}. Количество слов в строке: {len(words)}")
    print(f"Количество строк в файле: {num_lines}. Количество символов в файле: {num_chars}. Количество слов в файле: {num_words}")


