# Функция полиморфизм -> len(): __len__
# print(len("Makers"))
# print(len([1,2,3,4]))
# print(len({1:2, 3:4}))

# + (__add__) - метод полиморфизм

# print(5 + 5)
# print("hello" + "world")
# print([1,2,3] + [4,5,6])

# Полиморфизм - это способность фукций(метода) используется для разных типов(классов)
# Широко распрастраненное определение: "один интерфейс - много реализаций" 
# list.pop
# set.pop
# dict.pop

# class Cat:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
    
#     def info(self):
#         print(f"it\'s a cat. Cats name is {self.name}, age {self.age}")

#     def make_sound(self):
#         print("Meow, meow! \n Что за хрень броооооо")

    
# class Dog:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
    
#     def info(self):
#         print(f"it\'s a dog. Dogs name is {self.name}, age {self.age}")

#     def make_sound(self):
#         print("Bark, bark!")


# cat = Cat("Garfild", 5)
# dog = Dog("Pluto", 6)

# for obj in (cat, dog):
#     obj.info()
#     obj.make_sound()

# from math import pi

# class Shape:
#     def __init__(self, name) -> None:
#         self.name = name

#     def area(self):
#         pass

#     def fact(self):
#         return f"Я фигура в двумерной плоскости: {self.name}!"


# class Square(Shape):
#     def __init__(self, length) -> None:
#         super().__init__("Квадрат")
#         self.length = length

#     def area(self):
#         return self.length ** 2
    
#     def fact(self):
#         return super().fact() + "\nУ квадрата все сторны равны и углы равны 90 градусам!"
    

# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         super().__init__("Окружность")
#         self.radius = radius

#     def area(self):
#         return pi * self.radius ** 2
    

# a = Square(8)
# b = Circle(4)

# print(a.fact())
# print(a.area())

# print(b.fact())
# print(b.area())

# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. 
# Изначальный уровень заряда батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.

# class MobilePhone:
#     def __init__(self, imei, os_info):
#         self._imei = imei
#         self._battery_level = 100
#         self._os_info = os_info

#     def _decrease_battery_level(self, percentage):
#         if self._battery_level > 0:
#             self._battery_level -= percentage
#         if self._battery_level < 0:
#             self._battery_level = 0

#     def _check_battery_level(self):
#         if self._battery_level == 0:
#             raise RuntimeError("Телефон разряжен")

#     def listen_to_music(self):
#         self._check_battery_level()
#         self._decrease_battery_level(5)
#         print("Воспроизведение музыки")

#     def watch_video(self):
#         self._check_battery_level()
#         if self._battery_level <= 10:
#             print("Недостаточно заряда для просмотра видео")
#         else:
#             self._decrease_battery_level(10)
#             print("Просмотр видео")

#     def charge_battery(self, percentage):
#         if -100 <= percentage <= 100:
#             if self._battery_level + percentage < 0:
#                 self._battery_level = 0
#             elif self._battery_level + percentage > 100:
#                 self._battery_level = 100
#             else:
#                 self._battery_level += percentage
#         else:
#             raise ValueError("Некорректное значение заряда")

#     def get_battery_level(self):
#         return self._battery_level

# def charge_battery(self, sec):
#     from datetime import datetime, timedelta
#     from time import sleep

#     now = datetime.now
#     end_time = (now() + timedelta(seconds=sec))
#     print(end_time)

# phone = MobilePhone("AppleIphone 14pro", "ios 16")

# phone.listen_to_music() 
# print(phone.get_battery_level())

# phone.watch_video()
# print(phone.get_battery_level()) 

# phone.charge_battery()
# print(phone.get_battery_level()) 

# phone.watch_video() 
# print(phone.get_battery_level())

# phone.charge_battery(20)
# print(phone.get_battery_level()) 

# phone.listen_to_music()
# print(phone.get_battery_level()) 

# phone.charge_battery(-50)
# print(phone.get_battery_level())  # ValueError: Некорректное значение заряда

# phone.charge_battery(-35)
# print(phone.get_battery_level())

# phone.watch_video()
# print(phone.get_battery_level()) 
