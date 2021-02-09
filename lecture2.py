# class Auto:
#     def ride(self):
#         print("Riding on a ground")
#
#
# class Boat:
#     def swim(self):
#         print("Sailing in the ocean")
#
#
# class Amphibian(Auto, Boat):
#     pass
#
#
# a = Amphibian()
# a.ride()
# a.swim()
#
#
# print(isinstance(a, Auto))
# print(isinstance(a, Boat))
# print(isinstance(a, Amphibian))

# +++++++++++++++++++++++++++++++++++

# class A:
#     def hi(self):
#         print("A")
#
#
# class B(A):
#     # def hi(self):
#     #     print("B")
#     pass
#
#
# class C(A):
#     def hi(self):
#         print("C")
#
#
# class D(B, C):
#     pass
#
#
# d = D()
# d.hi()
# print(D.mro())

# +++++++++++++++++++++++++++++++++++

# class A:
#     def __init__(self):
#         self.name = 'John'
#         self.age = 23
#
#     def getName(self):
#         return self.name
#
#
# class B:
#     def __init__(self):
#         self.name = 'Richard'
#         self.id = '32'
#
#     def getName(self):
#         return self.name
#
#
# class C(A, B):
#     def __init__(self):
#         # A.__init__(self)
#         B.__init__(self)
#
#     def getName(self):
#         return self.name
#
#
# C1 = C()
# C1.age = 222
# print(C1.age)
# print(C1.getName())
# print(C.__mro__)

# +++++++++++++++++++++++++++++++++++

# class First:
#     def __init__(self):
#         super().__init__()
#         print("first")
#
#
# class Second:
#     def __init__(self):
#         super().__init__()
#         print("second")
#
#
# class Third(First, Second):
#     def __init__(self):
#         super().__init__()
#         print("third")
#
#
# a = Third()
# print(Third.__mro__)

# +++++++++++++++++++++++++++++++++++
# class X: ...
# class Y: ...
# class A(X, Y): ...
# class B(Y, X): ...
# class G(A, B): ...

# class X: ...
# class Y(X): ...
# class A(X, Y): ...

# +++++++++++++++++++++++++++++++++++

# class X: ...
# class Y: ...
# class A(X, Y): ...
# class B(Y, X): ...
#
#
# class MyMRO(type):  # наследование type = это метакласс
#     def mro(cls):
#         return (cls, A, B, X, Y, object)  # явно задаем порядок!
#
#
# class G(A, B, metaclass=MyMRO):
#     ...
#
# print(G.mro())

# +++++++++++++++++++++++++++++++++++

# class MusicPlayerMixin:
#     def play_music(self, song):
#         print(f"Now playing: {song}")
#
#
# class Smartphone(MusicPlayerMixin):
#     pass
#
#
# class Radio(MusicPlayerMixin):
#     pass
#
#
# class Auto:
#     def ride(self):
#         print("Riding on a ground")
#
#
# class Boat:
#     def swim(self):
#         print("Sailing in the ocean")
#
#
# class Amphibian(Auto, Boat):
#     pass
#
#
# class Amphibian(Auto, Boat, MusicPlayerMixin):
#     pass
#
#
# a = Amphibian()
# a.play_music('Elvis presley falling in love')

# +++++++++++++++++++++++++++++++++++

# from werkzeug.wrappers import (
#     BaseRequest,
#     AcceptMixin,
#     ETagRequestMixin,
#     UserAgentMixin)
#
#
# class Request(AcceptMixin,
#               ETagRequestMixin,
#               UserAgentMixin,
#               BaseRequest):
#     pass

# +++++++++++++++++++++++++++++++++++

# DESCRIPTORS +++++++++++++++++++++++ getattr and set attr
# class Order:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total(self):
#         return self.price * self.quantity
#
#     # Отработает лишь для несуществующих атрибутов
#     def __getattr__(self, item):
#         return f'Attr {item} not exists'
#
#     def __getattribute__(self, item):
#         value = super().__getattribute__(item)
#         print(value)
#         if not isinstance(value, str) and not callable(value) and value <= 0:
#             raise ValueError(f'Pay attention! Object has negative {item}.')
#
#         return value

    # def __setattr__(self, key, value):
    #     if key in ('price', 'quantity'):
    #         if value <= 0:
    #             raise ValueError(f'{key} Cannot be negative.')
    #     return super().__setattr__(key, value)



# apple_order = Order('apple', -2, 10)
# print(apple_order.total())
# apple_order.price = -2

# +++++++++++++++++++++++++++++++++++

#  DESCRIPTORS THEME WITH PROPERTY
# class Order:
#     def __init__(self, name, price, quantity):
#         self._name = name
#         self.price = price
#         self._quantity = None # избегаем RecursionError
#         self.quantity = quantity
#
#     @property
#     def quantity(self):
#         return self._quantity
#
#     @quantity.setter
#     def quantity(self, value):
#         if value < 0:
#             raise ValueError('Cannot be negative.')
#         self._quantity = value
#
#     def total(self):
#         return self.price * self.quantity
#
#
# apple_order = Order('apple', -1, 10)
# print(apple_order.total())

# +++++++++++++++++++++++++++++++++++

# DESCRIPTORS CLASS
# class NonNegative:
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError(f'{self.name} Cannot be negative.')
#         instance.__dict__[self.name] = value
#
#     def __set_name__(self, owner, name):
#         self.name = name
#
#
# class Order:
#     price = NonNegative() # вызывается на имя price set_name
#     quantity = NonNegative() # вызывается на имя quantity set_name
#
#     def __init__(self, name, price, quantity):
#         self._name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total(self):
#         return self.price * self.quantity
#
#
# apple_order = Order('apple', 13, 10)
# print(apple_order.total())
# apple_order.price = -10
# apple_order.quantity = -10


class A:
    def calc(self):
        pass


class B:
    a = A()
# ENUMS ++++++++++++++++
# from enum import Enum
#
#
# class Num(Enum):
#     one = 1
#     two = 2
#     three = 3
#
#
# for n in Num:
#     print(n.value)

# from enum import Enum
#
#
# class Color(Enum):
#     BLUE = 1
#     BLACK = 2
#     BROWN = 3
#
# apples = {}
# apples[Color.BLUE] = 'blue'
# apples[Color.BLACK] = 'black'
# print(apples)

# from enum import Enum
#
#
# class Students(Enum):
#     IGOR = 1
#     SERGEY = 2
#     VASYA = 3
#
#     def info(self):
#         print("Имя - %s, значение - %s"%(self.name, self.value))
#
# Students.IGOR.info()

# import enum
#
#
# class Days(enum.Enum):
#    Sun = 1
#    Mon = 2
#
#
# print('enum member accessed by name: ')
# print(Days['Mon'])
# print('enum member accessed by Value: ')
# print (Days(1))


# import enum
#
#
# class Days(enum.Enum):
#    Sun = 1
#    Mon = 2
#    Tue = 1
#
#
# if Days.Sun == Days.Tue:
#    print('Match')
# if Days.Mon != Days.Tue:
#    print('No Match')

