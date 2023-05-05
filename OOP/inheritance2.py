# Множественное наследование - это когда класс наследуется от двух или более классов 

# class Auto:
#     def play_music_at_station(self):
#         print("Music is playing")

#     def ride(self):
#         print("We\'re riding or the ground")


# class Plane:
#     def play_music_at_station(self):
#         print("Listenind Ed Sheeran!")

#     def fly(self):
#         print("We\'re flying!")


# class FutureAuto(Plane, Auto):
#     pass

# obj = FutureAuto()
# obj.ride()
# obj.fly()
# obj.play_music_at_station()
# obj.play_music_at_station()

# print(dir(obj))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Проблема ромба - когда поиск шел в родительских класс прежде чем искать у соседнего общего предка (решена спомощью mro)
# MRO (Method Resolution Order) - это у нас специальный метод, механизм для корректного поиска родительских методов. 
# Был создан для решение проблемы ромба, которая появилась введение object в пайтон. 
# Поис идет такии образом что если у родительских клаассов есть общий предок, то идет поиск в ширину.



# class Zero:
#     def say(self):
#         print("class Zero")

# class Frist(Zero):
#     def say(self):
#         print("class First")

# class Second(Zero):
#     def say(self):
#         print("class Second")

# class MyClass(Frist, Second):
#     def say(self):
#         super().say()
#         print("class MyClass")

# obj = MyClass()
# obj.say()
# print(MyClass.mro())


# class Z: #3
#     pass

# class Y: #5
#     pass 

# class A(Z): #2
#     pass

# class B(Y): #4
#     pass

# class X(A, B): #1
#     pass

# print(X.mro())

# Проблема перекрестного наследование # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# class Y:
#     pass

# class X:
#     pass 

# class A(X, Y):
#     pass 

# class B(Y, X):
#     pass 

# class MyMro(type):
#     def mro(cls) -> list[type]:
#         return [cls, A, B, X, Y, object]
    
# class MyClass(A, B, metaclass=MyMro):
#     pass 


# print(MyClass.mro())



