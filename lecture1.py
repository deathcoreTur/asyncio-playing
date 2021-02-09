from __future__ import annotations
from abc import ABC, abstractmethod
#
#Abastract classes
## +++++++++++++++++++++++++++++++++++++++++++
# class Image(ABC):
#     @abstractmethod
#     def load_image(self, filename):
#         pass
#
#     @abstractmethod
#     def save_image(self, filename):
#         pass
#
#     @abstractmethod
#     def function_one(self):
#         print('function one')
#
#
# class Bitmap(Image):
#     def load_image(self, text, dr):
#         print('loading bitmap')
#
#     def save_image(self, filename):
#         print('save bitmap')
#
#     def function_one(self):
#         print('i am child ')
#
# class Jpeg(Image):
#     def load_image(self, filename):
#         print('loading jpeg')
#
#     def save_image(self, filename):
#         print('saving jpeg')
#
#
# bitmap = Bitmap()
# bitmap.load_image('picture-1', '/home')
# bitmap.function_one()
# jpeg = Jpeg()
# jpeg.load_image('picture-2')


# +++++++++++++++++++++++++++++++++++++++++++
# class ChessPiece(ABC):
#     # общий метод, который будут использовать все наследники этого класса
#     def draw(self):
#         print("Drew a chess piece")
#
#     # абстрактный метод, который будет необходимо переопределять для каждого подкласса
#     @abstractmethod
#     def move(self):
#         pass
#
#
# class Queen(ChessPiece):
#     def move(self):
#         print("Moved Queen to e2e4")

# class Pawn(ChessPiece):  # пешка
#     def move(self):
#         print("Moved Pawn to e2e4")
#
#
# # Мы можем создать экземпляр класса
# q = Queen()
# # И нам доступны все методы класса
# q.draw()
# q.move()

# +++++++++++++++++++++++++++++++++++++++++++
# class Basic(ABC):
#     @abstractmethod
#     def hello(self):
#         print("Hello from Basic class")
#
#
# class Advanced(Basic):
#     def hello(self):
#         super().hello()
#         print("Enriched functionality")
#
#
# a = Advanced()
# a.hello()

class Class1():
    def test(self, x):     # Абстрактный метод
        # Возбуждаем исключение с помощью raise
        raise NotImplementedError("Необходимо переопределить метод")

class Class2(Class1):
    pass# Наследуем абстрактный метод
    # def test(self, x):     # Переопределяем метод
    #     print(x)

class Class3(Class1):      # Класс не переопределяет метод
    pass

c2 = Class2()
# c2.test(50)                # Выведет: 50
# c3 = Class3()
# try:                       # Перехватываем исключения
#     c3.test(50)            # Ошибка. Метод test() не переопределен
# except NotImplementedError as msg:
#     print(msg)              # Выведет: Необходимо переопределить метод


# +++++++++++++++++++++++++++++++++++++++++++
# Metaclasses

# def choose_class(name):
#     if name == 'foo':
#         class Foo(object):
#             pass
#         return Foo # возвращает класс, а не экземпляр
#     else:
#         class Bar(object):
#             pass
#         return Bar
#
# MyClass = choose_class('foo')
# print (MyClass) # функция возвращает класс, а не экземпляр

# +++++++++++++++++++++++++++++++++++++++++++
# class ObjectCreator():
#     pass
#
# print(type(1))
# print(type("1"))
#
# print(type(ObjectCreator))
# print(type(ObjectCreator()))

# +++++++++++++++++++++++++++++++++++++++++++
# class TestClass():
#     pass
#
# print(TestClass.__class__)
#
#
# # Classes
# print(TestClass)
# test_class2 = type('TestClass2', (), {})
# print(test_class2)
#
# # Instances
# test_class = TestClass()
# print(test_class)
# instance_of_test_class2 = test_class2()
# print(instance_of_test_class2)

# +++++++++++++++++++++++++++++++++++++++++++
# def show_message(self):
#     print(self.message)
#
#
# Foo = type('Foo', (), {'message': 'Hello'})
# FooChild = type('FooChild', (Foo,), {'show_message': show_message})
# my_foo = FooChild()
# my_foo.show_message()

# +++++++++++++++++++++++++++++++++++++++++++
# class MyMeta(type):
#     pass
#
#
# class MyClass(metaclass=MyMeta):
#     pass
#
#
# class MySubclass(MyClass):
#     pass
#
#
# print(type(MyMeta))
# print(type(MyClass))
# print(type(MySubclass))

# +++++++++++++++++++++++++++++++++++++++++++
# class UpperAttrMetaclass(type):
#     def __new__(cls, name, bases, dct):
#
#         attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
#         uppercase_attr = dict((name.upper(), value) for name, value in attrs)
#
#         return super().__new__(cls, name, bases, uppercase_attr)
#
#
# class NewClass(metaclass=UpperAttrMetaclass):
#     test = 'THIS IS TEST MESSAGE'
#
#
# new_class = NewClass()
# print(hasattr(new_class, 'test'))
# print(hasattr(new_class, 'TEST'))
# print(new_class.TEST)

# +++++++++++++++++++++++++++++++++++++++++++
# def upper_attr(future_class_name, future_class_parents, future_class_attr):
#     """
#         Возвращает объект-класс, имена атрибутов которого
#         переведены в верхний регистр
#     """
#     attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
#     uppercase_attr = dict((name.upper(), value) for name, value in attrs)
#
#     # создаём класс с помощью `type`
#     return type(future_class_name, future_class_parents, uppercase_attr)
#
#
# __metaclass__ = upper_attr # это сработает для всех классов в модуле
#
#
# class Foo(object):
#     bar = 'bip'
#
# print (hasattr(Foo, 'bar'))
# print (hasattr(Foo, 'BAR'))



