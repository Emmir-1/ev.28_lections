# sentence = input("Введите предложение: ")
# # if sentence[-1] == "?":
# #     print("ДА, вопросительное!")
# # else:
# #     print("No, normal one!")
# print("ДА, вопросительно" if sentence[-1] == "?" else "No, normal one!") # в print можно записать только одно условие 

#---------------------------------------------------------------------------------------------------------------------
# Ternary operstors(Тернарный оператор - это кострукция которая по своему действию аналогичнa конструкции if/else но при это записывается в одну строчку
# number = int(input("Введите число: "))
# res = "even number" if number % 2 == 0 else "odd number"   
#        #Четное                               #не четное
# print(res)


# <Выражение если True> if <Условие> else <Выражение если False>

# ls = [55, 65, 75, 89, 100, 15, 6]
# print(ls)
# choice = input("Введите максимальное или минимальное: ")
# res = max(ls) if choice.lower().strip() == "max" else min(ls)
# print(res)
# if choice.lower().strip() == "max":
#     print(max(ls))
# elif choice.lower().strip() == "min":
#     print(min(ls))
# else:
#     print("Инвалидный код! ")

# res = max(ls) if choice.lower().strip() == "max" else min(ls) if choice.lower().strip() == "min" else "Инвалид!"
# print(res)
#---------------------------------------------------------------------------------------------------------------------
# flag = True
# symbols = "0123456789" + "-" + "." #0123456789-.
# while flag:
#     print()
#     num1 = input("Введите первое число: ")
#     is_correct_number = True # ""
#     for x in num1:
#         if x not in symbols:
#             print("Вы ввели не правильное число!")
#             is_correct_number = False
#             break
#     if not is_correct_number:
#         continue

#     num2 = input("Введите второе число: ")
#     for x in num2:
#         if x not in symbols:
#             print("Вы ввели не правильное число!")
#             is_correct_number = False
#             break
#     if not is_correct_number:
#         continue # начинать заново цикл!
    
#     num1 = float(num1) if "." in num1 else int (num1) 
#     num2 = float(num2) if "." in num2 else int (num2)    
#     # print(num1, type(num1))
#     # print(num2, type(num2))
#     operator = input("Введите оператор(+, -, *, /): ").strip()

#     if operator == "+":
#         print(f"Результат: {num1 + num2}")
#     elif operator == "-":
#         print(f"Результат: {num1 - num2}")
#     elif operator == "*":
#         print(f"Результат: {num1 * num2}")
#     elif operator == "/":
#         if num2 == 0:
#             print("На ноль делить нельзя!")
#         else:
#             print(f"Результат {num1 / num2}")
#     else:
#         print("Вы вели не верный оператор!")

#     choice = input("Хотите вы продолжить (да или нет)?: ")
#     if choice.lower().strip() != "да":
#         flag = False
#         print("Не звони сюда больше")






