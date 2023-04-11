# lists() -> (Списки, массив) - изменяемый, последовательный тип данных, который предстоваляет из себя колекцию каких либо обьектов (значения).

# my_list = [1, "string", False, None, [1,2,3,4,5]]
# print(my_list, type(my_list))

# range() - возращает последовательность элементо(чисел)
# ls = range(1, 101)
# my_list = list(ls)
# print(my_list)

# list()

# my_list =list("Hello world")
# ls = list["hello world"]
# print(my_list)
# print(ls)

# tuple_ = ("Banana","apple","cherry")
# print(tuple_, type(tuple_))
# ls = list(tuple_)
# print(ls, type(ls))

# Индексация в списках 
# ls = [1, 2, 3, 4, 5, "string", [True, False, None]]
# # print(ls, len(ls))
# # print(ls[1],ls[2])
# print(ls[4:]) # [5,"string", [True, False, None]]


# ls = [1, 2, 3, 4, 5, "string", [True, False, None], 4, 5, 6]
# print(ls[6][:2])

# ls = list(range(1, 11))
# print(ls)
# for num in ls:
#     print("HEllo world")



# ls = ["John", "Sansa", "Tririon", "eddart", "Serseya", "Jamie"]
# print(ls, len(ls))
# for x in ls:
#     print(f"Hello mr/mrs {x}! Welcome to the club!")
#     print("1")

# print("2")


# ls -> 1, 21 - для четных чисел вытащить квадрат числа а нечетных чисел куб числа
# ls =list(range(1, 21))
# print(ls)
# for num in ls:
#     if num % 2 == 0:
#      print(f"Число четное {num}, квадрат: {num**2}")
#     else:
#      print(f"Число нечетное {num}, куб: {num**3}")



#--------------------------------------------------------------------------------
# методы списков 
# print(dir([]))
# append(element) - добовляет элемент в конец списка

# ls =[1, 2, 3]
# print(ls)
# ls.append(4)
# ls.append("Hello")
# ls.append([True, False])
# print(ls)

# extend(object) - расширает список

# ls = [1, 2, 3]
# ls.append("hello")
# print(ls)
# ls.extend("hello")
# ls.extend(str(56))
# ls.extend([1, 2, 3])
# print(ls)

# ls = [1, 2, 3]
# ls1 = [4, 5, 6]
# print(ls + ls1)

# sort() - сортирует список если передать reverse = True, то список отсортируется в убывающем порядке
# from random import randint 

# ls = []
# for x in range(0, 100):
#     num = randint(0, 1000)
#     ls.append(num)
    
# print(ls)
# ls.sort(reverse=True)
# print("After:")
# print(ls)


# ls = ["John", "Emmir", "Aizirek", "Deyneris", "azalya"]
# ls.sort(key=len, reverse=True)
# print(ls)

# insert(index, element) - добовляет элемент по указанному index

# ls = ["String", 2, 3, False]
# ls.insert(1, 1)
# print(ls)

# remove(element,[start], [end]) - удоляет element из списка, если его нет, выводится ошибка
# pop([index]) - удоляет и возрощает элемент из списка по index не передать, то удаляет последний элеиент

# ls = [5, 1, 2, 4, 4, 5, 5, 5]
#  ls.remove(5)
#  print(ls)
#  print(5 in ls)
# while 5 in ls:
#     ls.remove(5)
# print(ls)


# ls = [5, 1, 2, 4, 5, 5]
# # print(ls.pop(0)) # 5
# # print(ls.remove(5)) # None
# deleted = ls.pop()
# print(ls)
# print(deleted)


# update ------------------------------------------------------------

# ls = [1, "h", 3]
# print(ls)
# ls[1] = 2
# print(ls)
# ls.reverse()
# print(ls)
# print(ls[::-1])


# pizza = ["first_item", "seconde_item", "third_item", "forth_item", "fifth_item", "sixth_item"]
# spisok =[]
# for x in pizza:
#     if not x.startswith("f"):
#         spisok.append(x)

# print(spisok)


