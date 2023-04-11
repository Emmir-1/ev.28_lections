# Обробатка исключения
# операторы  try..except

# Errors -> связаны с кодом
    # SyntaxError
    # IndentationError
    # TabError

# Исключения execptions -> связаны с неправельными данными передаются в код 
    # ZeroDivisionError
    # ArithmeticError
    # NameError
    # IndexError
    # KeyError
    # BaseException # прорадитель всех исключений

# try:
#     a = int(input("Enter the number: "))
# except:
#     print("неправильные данные")
# else:
#     print(a * 5)

# try:
#     <body>
# except:
#     <body>
# else:
#     <body> если нет ошибки
# finally:
#     <body> сработает в любом случае

# ls = ["John", "Snow", "Tirion"]
# print(ls)
# try:
#     i = int(input("Vvedite index: "))
#     print(ls[i])
# except ValueError:
#     print("Вы ввели не правельные данные!")
# except IndexError:
#     print("Вы ввели неправельный индекс!")

# -------------------------------------------------------------------------------
# отображение ошибки 
# Exception as e (error)

# dict_ = {"1": "one", "2": "two", "name":"John",}
# try:
#     key = input("Введите key: ")
#     print(dict_[key])
# except Exception as e:
#     print(f"opps {e.__class__} error!")

# try:
#     num1 = int(input("Enter num1: "))
#     num2 = int(input("Enter num2: "))
#     result = num1 / num2
# except ValueError:
#     print("Invalid input")
# except ZeroDivisionError:
#     print("Na 0 delit nelzya")
# else:
#     print(result)
# finally:
#     print("The end!")







