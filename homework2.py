class Person:
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    def showName(self):
        print(self.name)

    def showAge(self):
        print(self.age)


class Student:
    def __init__(self, studentId):
        self.studentId = studentId

    def getId(self):
        return self.studentId


class Resident(Person, Student):  # extends both Person and Student class
    def __init__(self, name, age, id):
        Person.__init__(self, name, age)
        Student.__init__(self, id)

    # Create an object of the subclass


resident1 = Resident('John', 30, '102')
resident1.showName()
print(resident1.getId())


class HiMixin():
    def hi(self):
        print(f'Hello, my name is {self.name}')


class Employee(HiMixin):
    def __init__(self, id, name, address):
        self.employment_history = id
        self.name = name
        self.address = address


class Student(HiMixin):
    def __init__(self, id, name, address):
        self.student_id = id
        self.name = name
        self.registration = address


student = Student(1, 'John', 'Pushkina 13')
student.hi()
employee = Employee(101, 'Joe', 'Shevchenka 88b')
employee.hi()



# DESCRIPTORS CLASS
class Length:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if len(value.strip()) == 0:
            raise ValueError(f'{self.name} Cannot be empty.')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Employee:
    name = Length() # вызывается на имя name set_name
    surname = Length() # вызывается на имя surname set_name

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


employee = Employee('AAA', 'Smith')
employee.name = ' '
