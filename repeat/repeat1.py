# num1 = 1

# while num1 >= 0:
#     num1 = input("Введите число: ") #int("54") # 54t
#     if num1[0] == "-" and num1[1:].isdigit(): # -51
#         num1 = int(num1)
#     else:
#         num1 = 1
# print("Встретилось отрицатильное число")       

#--------------------------------------------------------------------------------
# from random import randint

# ls = []
# for x in range(0, 100):
#     ls.append(randint(0, 100))

# ls.sort()
# print(ls, len(ls))


# res = []
# for x in ls: 
#     if x not in res:
#         res.append(x)
       
# print(res, len(res))

#--------------------------------------------------------------------------------

# x1 = int(input("gde: "))
# y1 = int(input('chto: '))
# ladya = [x1, y1] #2, 5

# x2 = int(input("gde: "))
# y2 = int(input('chto: '))
# target = [x2, y2] #4, 6

# if x1 == x2 or y1 == y2:
#     print(True)
# else:
#     print(False)

#--------------------------------------------------------------------------------

# import random
# ls = ["plov", "besh-barmak", "kuurdak", "oromo", "lagman"]
# p = 0
# b = 0
# k = 0
# o = 0
# l = 0

# for x in range(0, 1_000_000):
#     meal = random.choice(ls)
#    # print(meal)
#     if meal.lower() == "plov":
#         p += 1
#     elif meal.lower() == "besh-barmak":
#         b += 1 
#     elif meal.lower() == "kuurdak":
#         k += 1 
#     elif meal.lower() == "oromo":
#         o += 1 
#     else:
#         l += 1

        
# print("Результат голодных игр")        
# # print(f"plow: {p}\nbesh-barmak: {b}\nkurdak: {k}\noromo{o}\nlagman{l}")
# dict_ = {"plov": p, "besh-barmak": b, "kuurdak": k, "oromo": o, "lagman": l}

# print(dict_)
# res = sorted(dict_.items(), key = lambda x: x[1], reverse=True)[0]
# print(f"Победило блюда {res[0]} и оно набрало: {res[1]} очков!")



#--------------------------------------------------------------------------------
"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
"""

# nums = [2,  7, 11, 15]
# target = 9 

# nums = [4, 11, 2, 5, 1, 6]
# target = 8 

# for i in range(0, len(nums)):
#     num = target - nums[i] 
#     if num in nums:
#         if num != nums[i]:
#             print(f"Otvet: {i}, {nums.index(num)}")
#             break 


# x1 = int(input()) 
# y1 = int(input()) 
# x2 = int(input()) 
# y2=int(input()) 
# if x2-x1 == y2-y1: 
#     print('YES') 
# else: print('NO')
