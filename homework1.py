from abc import ABC, abstractmethod
from math import sqrt


# class Polygon(ABC):
#     @abstractmethod
#     def noofsides(self):
#         pass
#
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Triangle(Polygon):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 3 sides")
#
#     def area(self):
#         # calculate the semi-perimeter
#         s = (self.a + self.b + self.c) / 2
#
#         # calculate the area
#         area = sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
#         return area
#
#
# class Pentagon(Polygon):
#     def __init__(self, a):
#         self.a = a
#
#     def area(self):
#         # Formula to find area
#         area = (sqrt(5 * (5 + 2 *
#                           (sqrt(5)))) * self.a * self.a) / 4
#         return area
#
#         # overriding abstract method
#     def noofsides(self):
#         print("I have 5 sides")
#
#
# class Hexagon(Polygon):
#     def __init__(self, a):
#         self.a = a
#
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 6 sides")
#
#     def area(self):
#         # Formula to find area
#         area = ((3 * sqrt(3) *(self.a * self.a)) / 2)
#         return area
#
#
# class Quadrilateral(Polygon):
#
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 4 sides")
#
#     # Driver code
#
#
# R = Triangle(2,2,2)
# R.noofsides()
# print(R.area())
#
# R = Pentagon(4)
# R.noofsides()
# print(R.area())
#
# K = Hexagon(5)
# K.noofsides()
# print(K.area())


# class AttrMetaclass(type):
#     def __new__(cls, name, bases, dct):
#         attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
#         uppercase_attr = dict((name + '_' + n, value) for n, value in attrs)
#
#         return super().__new__(cls, name, bases, uppercase_attr)
#
#
# class NewClass(metaclass=AttrMetaclass):
#     test = 'THIS IS TEST MESSAGE'
#
#
# class Second(metaclass=AttrMetaclass):
#     one = 1
#
# a = Second()
# print(hasattr(a, 'one'))
# print(hasattr(a, 'Second_one'))
# print(a.Second_one)
# print(vars(Second))


# new_class = NewClass()
# print(hasattr(new_class, 'test'))
# print(new_class.NewClass_test)




