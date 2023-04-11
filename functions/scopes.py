# Облатсть видимости и пространство имен (scopes)
# Это - технология которая опредялят контекст имени(переменые), в рамкох которого мы можем ее использовать 

# built-ins (Встроенная область видимости) -> print, len, max
# global(Глобальная) -> область одного файла 
# enclosed(не локальная (замкнутая), nonlocal)
# local(локальная) -> область внутри функции


# x = 200

# def myFunc():
#     print(x)
#     a = 300
#     print(a)

# myFunc() # -> 300
# # print(a)
# print(x)


# a = 10 # global
# print # built-in

# def hello(): # global
#     a = "hello world -" # local
#     print(a, "local inside in func!")

# hello()
# print(a, "global")


#LEGB - local enclosed global built-in
        # -------->>>>>>>>>

# ------------------------------------------------------------------
# Enclosed 
# замкнутое пространство имен - локальконое постранство, у которого есть внутреннее(вложение) локальное пространство


# x = "global"
# print(x, "1")

# def enclosed(): # global
#     x = "enclosed"
#     def local(): #local
#         x = "local"
#         print(x, "3")
#     print(x, "2")
#     local()
#     print(x, "4")

# enclosed()
# print(x, "5")


# a = 5

# def func():
#     print(a) # 5
#     a = a + 1

# func()

# global -> позволяет изменять значение глобальной переменой находясь внутри локалоной области

# nonlocal -> позволяет изменять значение не локальной(замкнутой) переменной находится внутри локальной области

# var = 0 

# def increment(): # LEGB
#     global var
#     var += 1 # var = var + 1

# print(var) # 100
# increment()
# print(var) #101
# increment()
# increment()
# increment()
# increment()
# increment()
# print(var) # 106

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment
    
# c_wash = counter() 
# c_ask = counter()
# #print(c) # <function counter.<locals>.increment at 0x103cfea60>
# print(c_wash()) # 1
# print(c_wash()) # 2
# print(c_wash()) # 3
# print(c_ask()) # 4
# print(c_ask()) # 5


# print(dir(__builtins__)) можно получить встроеное в питон
# print(len(dir(__builtins__)))


# alobals - func которая возращает все имена внутри глаболоной области видимости

# locals - функция которая возращает все имена внутри глобльной области видимости и локальной 


# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# def showStats(heroes, mobs):
#     print()
#     print(f"John Snow ты убил:\n\tЛанистеров: {heroes} \n\tСерегу: {mobs}")
#     print()

# counter_heroes = counter()
# counter_mobs = counter()
# heroes = 0
# mobs = 0
# print("Приветствую вас, KING ишак, в зип ландий!")
# while True:
#     print("Тебе доступны следующие действия:")
#     print("1-убить героя, 2-убить моба, 3-статистика, 4-выйти из игры")
#     choice = input("Введите что хотите сделать: ").strip()
#     if choice == "1":
#         heroes = counter_heroes()
#         print("John вы обезглавили Ланистера!")
#     elif choice == "2":
#         mobs = counter_mobs()
#         print("Вы убили белого Серегу!")
#     elif choice == "3":
#         showStats(heroes, mobs)
#     elif choice == "4":
#         print("Пока пока ждем еще раз!")
#         break
    















