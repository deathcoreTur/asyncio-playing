# from os.path import join
#
#
# class FileObject:
#     '''Обёртка для файлового объекта, чтобы быть уверенным в том, что файл будет закрыт при удалении.'''
#
#     def __init__(self, filepath='.', filename='sample.txt'):
#         # открыть файл filename в filepath в режиме чтения и записи
#         self.file = open(join(filepath, filename), 'r+')
#         print('INIT')
#
#     def __del__(self):
#         self.file.close()
#         del self.file
#         print('CLOSE AND DELETE')
#
#
# a = FileObject()
# del a


# class unaryOp:
#     def __init__(self, value):
#         self._value = value
#
#     def __pos__(self):
#         print('__pos__ magic method')
#         return (+self._value)
#
#
# up = unaryOp(5)
# print(+up)
#
#
# class unaryOp:
#     def __init__(self, value):
#         self._value = value
#
#     def __neg__(self):
#         print('__neg__ magic method')
#         return (-self._value)
#
#
# up = unaryOp(5)
# print(-up)
#
#
# class invertClass:
#     def __init__(self, value):
#         self._value = value
#
#     def __invert__(self):
#         return self._value[::-1]
#
#     def __str__(self):
#         return self._value
#
#
# invrt = invertClass('Hello, George')
# invertedValue = ~invrt
# print(invertedValue)

# class Count:
#     def __init__(self, count):
#         self._count = count
#
#     def __add__(self, other):
#         total_count = self._count + other._count
#         return Count(total_count)
#
#     def __str__(self):
#         return 'Count: % i' % self._count
#
#
# c1 = Count(2)
# c2 = Count(5)
# c3 = c1 + c2
# print(c3)


# class Count:
#     def __init__(self, count):
#         self._count = count
#
#     def __add__(self, other):
#         total_count = self._count + other._count
#         return Count(total_count)
#
#     def __radd__(self, other):
#         if other == 0:
#             print('I am here')
#             return self
#         elif other == 1:
#             return other + self._count
#         else:
#             return self.__add__(other)
#
#     def __str__(self):
#         return 'Count:% i' % self._count
#
#
# c2 = Count(2)
# c1 = Count(4)
# c3 = 0 + c2
# print(c3)
# c4 = 1 + c2
# print(c4)
#
# print(c1 + c2)


# class inPlace:
#     def __init__(self, value):
#         self._value = value
#
#     def __iadd__(self, other):
#         self._value = self._value + other._value
#         return self._value
#
#     def __str__(object):
#         return self._value
#
#
# inP1 = inPlace(5)
# inP2 = inPlace(3)
# inP1 += inP2
# print(inP1)


# class Example:
#     def __init__(self, value: float):
#         self._value = value
#
#     def __int__(self):
#         print('test')
#         return int(self._value)
#
#
# a = Example(7.28)
# print(int(a))


# class Book():
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
#
#     # The __str__ function is used to return a user-friendly string
#     # representation of the object
#     def __str__(self):
#         print('str')
#         return f'{self.title} by {self.author}, costs {self.price}'
#
#     # The __str__ function is used to return a developer-friendly string
#     # representation of the object
#     def __repr__(self):
#         return f'title={self.title},author={self.author},price={self.price}'
#
#
# book1 = Book('Python Crash Course', 'Eric Matthes', 23.99)
# book2 = Book('Serious Python', 'Julien Danjou', 25.43)
#
# # print each object
# print(book1)
# print(book2)
#
# # use str() and repr()
# print(str(book1))
# print(repr(book2))


# class Dummy:
#     def __init__(self):
#         self._value = 25
#
#     def __getattr__(self, attr):
#         print (f'{attr} does not exist')
#
#
# d = Dummy()
# d.does_not_exist
# d.what_about_this_one
# print(d._value)


# class Dummy:
#     def __init__(self):
#         self._value = 25
#
#     def __getattribute__(self, attr):
#         return 2021
#
#
# d = Dummy()
# print(d.does_not_exist)
# print(d.what_about_this_one)
# print(d._value)


# class Tuple(tuple):
#     def __getattr__(self, name):
#         def _int(val):
#             try:
#                 return int(val)
#             except ValueError:
#                 return False
#
#         if not name.startswith('_') or not _int(name[1:]):
#             raise AttributeError("'tuple' object has no attribute '%s'" % name)
#         index = _int(name[1:]) - 1
#         return self[index]
#
#
# t = Tuple(['z', 3, 'Python', -1])
# print(t._1)  # 'z'
# print(t[0])  # 'z'
#
# print(t._2)  # 3
# print(t[1])  # 3
#
# print(t._3)  # 'Python'


# class Constants:
#     def __setattr__(self, name, value):
#         if name in self.__dict__:
#             raise Exception(f"Cannot change value of {name}.")
#         self.__dict__[name] = value
#
#
# a = Constants()
#
# a.b = 2
# print(a.b)
# a.b = 1
# print(a.b)

# class FunctionalList:
#     '''Класс-обёртка над списком с добавлением
#     некоторой функциональной магии: head,
#     tail, init, last, drop, take.'''
#
#     def __init__(self, values=None):
#         if values is None:
#             self.values = []
#         else:
#             self.values = values
#
#     def __len__(self):
#         return len(self.values)
#
#     def __getitem__(self, key):
#         # если значение или тип ключа некорректны,
#         # list выбросит исключение
#         return self.values[key]
#
#     def __setitem__(self, key, value):
#         self.values[key] = value
#
#     def __delitem__(self, key):
#         del self.values[key]
#
#     def __iter__(self):
#         return iter(self.values)
#
#     def __reversed__(self):
#         return FunctionalList(self.values[::-1])
#
#     def append(self, value):
#         self.values.append(value)
#     def head(self):
#         # получить первый элемент
#         return self.values[0]
#     def tail(self):
#         # получить все элементы после первого
#         return self.values[1:]
#     def init(self):
#         # получить все элементы кроме последнего
#         return self.values[:-1]
#     def last(self):
#         # получить последний элемент
#         return self.values[-1]
#     def drop(self, n):
#         # все элементы кроме первых n
#         return self.values[n:]
#     def take(self, n):
#         # первые n элементов
#         return self.values[:n]
#
#
# a = FunctionalList([2,4,6])
# print(a[0])
#
# b = reversed(a)
# print(b[0])


# class Word(str):
#     '''Класс для слов, определяющий сравнение по длине слов.'''

    # def __new__(cls, word):
    #     if ' ' in word:
    #         print("Value contains spaces. Truncating to first space.")
    #         word = word[:word.index(' ')] # Теперь Word это все символы до первого пробела
    #     return str.__new__(cls, word)

    # def __gt__(self, other):
    #     return len(self) > len(other)
    #
    # def __lt__(self, other):
    #     return len(self) < len(other)
    #
    # def __ge__(self, other):
    #     return len(self) >= len(other)
    #
    # def __le__(self, other):
    #     return len(self) <= len(other)


# a = Word('Bar ')
# b = Word('Far1')
#
# print(a > b)  # False
# print(a < b)  # True
#
# print(a==b)
# print(len(a))


# class Foo(object):
#     def __init__(self, item):
#         self.my_item = item
#
#     def __eq__(self, other):
#         print('eqqqqqqqq')
#         return self.my_item == other.my_item
#
#     def __ne__(self, other):
#         print('neeeeeeeeeeeeeeeeeee')
#         return self.my_item != other.my_item
#
#
# a = Foo(5)
# b = Foo(5)
# print(a == b)  # True
# print(a != b)  # False
# print(a is b)  # False


# Python 2.7
# class Box(object):
#     def __init__(self, ival):
#         self.value = ival
#
#     def __cmp__(self, other):
#         if self.value < other.value:
#             return -1
#         elif self.value > other.value:
#             return 1
#         else:
#             return 0
#
#
# print(Box(1) >= Box(2))
# print(Box(3) > Box(2))
# print(Box(0) == Box(1))


class Box(object):
    def __init__(self, ival):
        self.value = ival

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value


print(Box(1) > Box(2))
print(Box(3) > Box(2))
print(Box(0) == Box(1))