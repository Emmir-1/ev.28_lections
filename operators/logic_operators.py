# Операторы сравнения
# Условие оператора и логические операторы

#  операторы сравнения
# <, >, ==(равно), !=(не равно), <=, >=

# 1 < 5 -> true 
# 7 < 9 -> false

# Условные операторы 
#  if
#  elif
# # else 

# if <condition>:
#     <body if> # Сработает если в condition if придет true
# [elif] <condition>:
#     <body elif>
# [else]
#     <body else> #сработает если во всех выше стоящих условиях пришо False

# string = input("enter smt: ")

# if string.lower() == "hello": 
#     print("hello it\'s me\nI was wondering if after all these years you\'d like to meet")
# elif string.lower() == "john":
#     print("zaibis John Snow! The king")
# elif string.lower() == "abra-kadabra":
#     print("Salamon Kadabra")
# else:
#     print("Своподение не найдено!")

# print("Registration Form")
# email = input("Enter your email: ")
# password = input("Enter the password: ")
# if len(password) < 8: 
#     raise ValueError("Password is too short!\nNeed to be 8 sumbols or more!")
# elif password.isdigit():
#     raise ValueError("Password is invalid!\nPassword must contain symbols too!")
# elif password.isalpha():
#     raise ValueError("Password is invalid!\nPassword must contain number or speial symbols too!")

# password2 = input("Enter password confirmation: ")

# if password != password2:
#     raise ValueError("Password did not match!")
# print(f"Succesfully registred! Hello Mr\]/Mrs {email}!")



# age = input("Enter you age: ")
# if age.isdigit():
#     age = int(age)
# else:
#     raise Exception("Invalid value for age!")

# if age < 18:
#     print(f"Access Denied! Come again after {18 - age} year!")
# else:
#     print("You can pass! Welcome to KZ!")

# and -  логическое и
# or - логическое или
# not - логическое отрицание

# money = 1_000_200
# status = "premium"

# if money > 1_000_100 and status == "premium":
#     print("You\'re president of our club!")
# elif money > 1_000_100 or status == "premium":
#     print("You\'re ministr of our club!")
# else:
#     print("You\'re honorable number of our club!")

# str1 = "Hello world"
# print(str1)
# symbol = input("Enter the symbol: ")

# # if symbol not in str1:
# #     print(f"The symbol: {symbol} does not exists!")
# # else:
# #     print(f"The symbol: {symbol} exists")

# if symbol in str1:
#     print(f"The symbol: {symbol} exists!")
# else:
#     print(f"The symbol: {symbol} does not exists!")

# Разрешаем доступ если он юзер гитa или гугла и его возраст больше 21 или у него есть деньги(10000)

# user = "john"
# is_google_user =False
# is_yandex_user = True
# age = 19 
# user_coins = 11000

# if (is_yandex_user or is_google_user) and (age > 21 or user_coins > 10000):
#     print(f"You can enter the system Mr/Mrs {user}!")
# else:
#     print("Sorry, you couldh\'t enter!")







