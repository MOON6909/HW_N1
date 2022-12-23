# class Parents:
#     classmethods and attrs
# class Child(Parents):
#     classmethods and attrs
# class Human:
#     height=170
#
# class Student(Human):
#     pass
# class Worker(Human):
#     pass
# nick=Student()
# ann=Worker()
# print(nick.height)
# print(ann.height)
#
#
# class Rec:
#     def area(self, a, b):
#         return a*b
# rect=Rec()
# print(rect.area(4, 5))
#
# class Rec:
#     def area(self, a, b):
#         return a*b
# rect=Rec()
# print(rect.area(4, 5))
#

class Day:
    a=19
    b=3
    c=2009
#B-day
Dayyy=Day
print(f'Моє день народження {Dayyy.a} числа.')
Month=Day()
print(f'Місяць мого народження {Month.b}.')
Year=Day()
print(f'Рік мого народження {Year.c}.')
# Hello
# class Hello:
#     def __init__(self):
#         print('Hello')
# class Hello_World(Hello):
#     def __init__(self):
#         super().__init__()
#         print('World!')
# hello_world=Hello_World()
#
# class Class1:
#     var=20
#     def __init__(self):
#         self.var=10
#
# class Class2(Class1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#         print(super().var)
# clas=Class2()
#
# class C1:
#     pass
# class C2:
#     pass
#
# class CA(C1, C2):
#     pass
print('-------------------------------------- \n')

# class Computer:
#     def calculate(self):
#         super().__init__()
#         self.memory=128
# class Display:
#     def __init__(self):
#         super().__init__()
#         self.resolution='4K'
# class SmartPhone(Display, Computer):
#     def print_info(self):
#         print(self.resolution)
#         print(self.memory)

# iphone=SmartPhone()
# iphone.print_info()

class Kvadrat:
    def calcul(self, a):
        return a*a
ploshcha=Kvadrat()
print(f'Площа квадрата — {ploshcha.calcul(4)}')