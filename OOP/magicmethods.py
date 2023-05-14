# magic methods (Магические методы)
# dunder methods (double underscore) -> __int__

# Магия(фишка) заключается в том что эти методы запускаются без прямого обращение к ним, определеного методы могут отвечать за опредление операторы

# class A(int):
#     pass

# obj = A()
# print(dir(obj))

# Магические мотоды сравнение
# __eq__(self, other) -> 5 == 8
#                         5.__eq__(8)

# __ne__(self, other) -> != 

# __lt__ -> <

# __gt__ -> >

# __le__ -> <=

# __ge__ -> >=

# print("15" < "ABC")
# print(ord("1"), ord("A"))


# class Word(str):
#     def __new__(cls, obj):
#         # print(cls, "!!!")
#         # print(obj, "!!!")
#         obj = obj.replace(" ", "")
#         return super().__new__(cls, obj)

#     def __init__(self) -> None:
#         super().__init__()
#         self.obj = obj

#     def __gt__(self, other) -> bool:
#         print("gt сработал")
#         print(self)
#         print(other)
#         if len(self) > len(other):
#             return self
#         elif len(other) > len(self):
#             return other
#         else:
#             return "eq"
#         # return len(self) > len(other)
    
#     def __lt__(self, __value: str) -> bool:
#         return len(self) < len(__value)
    
#     def __eq__(self, __value: object) -> bool:
#         return len(self.obj) == len(__value.obj)
    


# obj = Word("  Hello John")
# obj1 = Word("   M ake    rs")

# print(obj > obj1) 
# print(obj1 < obj)
# print(obj == obj1)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# + - / * // % **

# + -> __add__
# - -> __sub__
# * -> __mul__
# // -> __floordiv__
# / -> __truediv__
# % -> __mod__
# ** -> __pow__

# class Cifra:
#     def __new__(cls, *args, **kwargs ):
#         number = abs(args[0])
#         instance = super().__new__(cls)
#         instance.number = number
#         return instance


#     def __sub__(self, other):
#         print("add была вызвана")
#         res = self.number - other.number
#         print(f"Result: {self.number} - {other.number} = {res}")

# value1 = Cifra(-117)
# value2 = Cifra(53)
# value1 - value2

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# from random import choice

# class Dog:
#     def sound(self):
#         print("Bark Bark!")

# class Cat:
#     def sound(self):
#         print("Meow Meow!")

# class Lion:
#     def sound(self):
#         print("Rou Rou!")



# class Pet:
#     def __new__(cls):
#         other = choice([Dog, Cat, Lion])
#         instance = super().__new__(other)
#         print(f"I\'m {type(instance).__name__}")
#         return instance
    
#     def __init__(self) -> None:
#         print("Pet never was called!")

    
# pet = Pet()
# pet.sound()
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# SINGLETON

# class Singleton:
#     _instance = None

#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance
        
#     def __str__(self) -> str:
#         return str(id(self))

# a = Singleton()
# b =Singleton()
# print(a)
# print(b)
# print(a is b)
# obj = Singleton()
# obj1 = Singleton()
# print(obj, obj1)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# дандер методы стокового отображение объекта 
# __str__
# __repr__

# class Bace:
#     def __init__(self, stroka) -> None:
#         self.string = stroka

#     def __str__(self) -> str:
#         return f"Объект: {self.string}"

#     def __repr__(self) -> str:
#         return f"Base('Example')"

# obj = Bace("Jasy")
# print(obj)
# print(repr(obj))
# obj2 = Bace("2pac")
# print(obj2)
# obj3 = eval(repr(obj2))
# print(obj3)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# class Kopilka:
#     def __init__(self) -> None:
#         self.total = 0
#         self.coins = []

#     def add_coin(self, coin):
#         self.total += coin
#         self.coins.append(coin)

#     def __len__(self):
#         return len(self.coins)

#     def __getitem__(self, index):
#         return self.coins[index - 1]

# obj = Kopilka()
# obj.add_coin(5)
# obj.add_coin(10)
# obj.add_coin(600)
# print(obj.total)
# print(obj.coins)
# print(len(obj))
# print(obj[1])
# print(obj[2])
# print(obj[3])

# for x in obj:
#     print(x)





