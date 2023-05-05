#Mixins
# Миксины - классы которые используются для наследование и передачи дочерним классам определенных методов, но от них не создаются объекты
# Для чего :
# 1. Вы хотите предоставить множество доп методов для классов 
# 2. Вы хотите использовать один конкретный метод во множестве разных классов 


# class EngineMixin:
#     def start_engine(self):
#         print("Started engine")

# class RadioMixin:
#     def play_radio(self):
#         print("music is playing")

# class Auto(EngineMixin, RadioMixin):
#     pass

# class Plane(EngineMixin):
#     pass

# class SmartPhone(RadioMixin):
#     pass

# class Train(EngineMixin, RadioMixin):
#     pass


# class FlyMixin():
#     def fly(self):
#         print("I can fly!")

# class WalkMixin():
#     def walk(self):
#         print("I can walk!")

# class SwimMixin():
#     def swim(self):
#         print("I can swim!")

# class Human(WalkMixin, SwimMixin):
#     name = "human"

#     def talk():
#         print("I can talk!")

# class Fish(SwimMixin):
#     name = "fish"

# class Exocoetidae(SwimMixin, FlyMixin):
#     name = "fly fisn"

# class Duck(FlyMixin, SwimMixin, WalkMixin):
#     name = "duck"

# # obj = Human()
# # obj.walk()
# # obj.swim()

# obj = Duck()
# obj.fly()
# obj.swim()
# obj.walk()

