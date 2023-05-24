# Абстракция 
# Абстракция (Абстрактный класс) - принцип ООП, в котором создаются абстрактный класс (класс - пустышка), в котором зодаются название атрибутов 
# и методов для того чтобы мы могли их определить в дочерних классах переопредлеить их нужным образом. (у нас есть название но нет логики).

# from abc import ABC, abstractclassmethod, abstractproperty

# class AbstractAnimal(ABC):

#     @abstractclassmethod
#     def voice(self):
#         pass

#     @abstractproperty
#     def legs(self):
#         pass

# abstractclassmethod - декоратор который требует переопределение метода в наследуемом классе

# abstractproperty - декоратор который требует переопределение аттрибута класса 

# obj = AbstractAnimal() #TypeError: Can't instantiate abstract class AbstractAnimal with abstract methods legs, voice

# class Dog(AbstractAnimal):
#     legs = 4
#     def voice(self):
#         print("Гав гав")

# class Cat(AbstractAnimal):
#     legs = 4

#     def voice(self):
#         print("Meow")

# dog = Dog()
# cat = Cat()
# arr = [dog, cat]
# for i in arr:
#     i.voice()
#     print(i.legs)


# class Shape(ABC):

#     @abstractclassmethod
#     def area(self):
#         pass

# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

#     def area(self):
#         return self.length ** 2
    
# obj = Square(12)
# print(obj.name)
# print(obj.area())


