from __future__ import annotations
from abc import ABC, abstractmethod


#  Factory method
# class Creator(ABC):
#     @abstractmethod
#     def factory_method(self):
#         pass
#
#     def some_operation(self) -> str:
#         # Вызываем фабричный метод, чтобы получить объект-продукт.
#         product = self.factory_method()
#
#         # Далее, работаем с этим продуктом.
#         result = f"Creator: The same creator's code has just worked with {product.operation()}"
#
#         return result
#
#
# class ConcreteCreator1(Creator):
#     def factory_method(self) -> Product:
#         return ConcreteProduct1()
#
#
# class ConcreteCreator2(Creator):
#     def factory_method(self) -> Product:
#         return ConcreteProduct2()
#
#
# class ConcreteCreator3(Creator):
#     def factory_method(self) -> Product:
#         return ConcreteProduct3()
#
# class Product(ABC):
#     @abstractmethod
#     def operation(self) -> str:
#         pass
#
#
# class ConcreteProduct1(Product):
#     def operation(self) -> str:
#         return "{Result of the ConcreteProduct1}"
#
#
# class ConcreteProduct2(Product):
#     def operation(self) -> str:
#         return "{Result of the ConcreteProduct2}"
#
#
# class ConcreteProduct3(Product):
#     def operation(self) -> str:
#         return "{Result of the ConcreteProduct3}"
#
#
# def client_code(creator: Creator) -> None:
#
#     print(f"Client: I'm not aware of the creator's class, but it still works.\n"
#           f"{creator.some_operation()}", end="")


# print("App: Launched with the ConcreteCreator1.")
# client_code(ConcreteCreator1())
# print("\n")
#
# print("App: Launched with the ConcreteCreator2.")
# client_code(ConcreteCreator2())

#
# client_code(ConcreteCreator3())

# ABStract factory
# class AbstractFactory(ABC):
#     @abstractmethod
#     def create_product_a(self) -> AbstractProductA:
#         pass
#
#     @abstractmethod
#     def create_product_b(self) -> AbstractProductB:
#         pass
#
#
# class ConcreteFactory1(AbstractFactory):
#     def create_product_a(self) -> AbstractProductA:
#         return ConcreteProductA1()
#
#     def create_product_b(self) -> AbstractProductB:
#         return ConcreteProductB1()
#
#
# class ConcreteFactory2(AbstractFactory):
#     def create_product_a(self) -> AbstractProductA:
#         return ConcreteProductA2()
#
#     def create_product_b(self) -> AbstractProductB:
#         return ConcreteProductB2()
#
#
# class AbstractProductA(ABC):
#     @abstractmethod
#     def useful_function_a(self) -> str:
#         pass
#
#
# class ConcreteProductA1(AbstractProductA):
#     def useful_function_a(self) -> str:
#         return "The result of the product A1."
#
#
# class ConcreteProductA2(AbstractProductA):
#     def useful_function_a(self) -> str:
#         return "The result of the product A2."
#
#
# class AbstractProductB(ABC):
#     @abstractmethod
#     def useful_function_b(self) -> None:
#         pass
#
#     @abstractmethod
#     def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
#         pass
#
#
# class ConcreteProductB1(AbstractProductB):
#     def useful_function_b(self) -> str:
#         return "The result of the product B1."
#
#     def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
#         result = collaborator.useful_function_a()
#         return f"The result of the B1 collaborating with the ({result})"
#
#
# class ConcreteProductB2(AbstractProductB):
#     def useful_function_b(self) -> str:
#         return "The result of the product B2."
#
#     def another_useful_function_b(self, collaborator: AbstractProductA):
#         result = collaborator.useful_function_a()
#         return f"The result of the B2 collaborating with the ({result})"
#
#
# def client_code(factory: AbstractFactory) -> None:
#     product_a = factory.create_product_a()
#     product_b = factory.create_product_b()
#
#     print(f"{product_b.useful_function_b()}")
#     print(f"{product_b.another_useful_function_b(product_a)}", end="")
#
#
# print("Client: Testing client code with the first factory type:")
# client_code(ConcreteFactory1())
#
# print("\n")
#
# print("Client: Testing the same client code with the second factory type:")
# client_code(ConcreteFactory2())

# Singleton
# class SingletonMeta(type):
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             instance = super().__call__(*args, **kwargs)
#             cls._instances[cls] = instance
#         return cls._instances[cls]
#
#
# class Singleton(metaclass=SingletonMeta):
#     def some_business_logic(self):
#         pass
#
#
# s1 = Singleton()
# s2 = Singleton()
#
# print(id(s1))
# print(id(s2))
# if id(s1) == id(s2):
#     print("Singleton works, both variables contain the same instance.")
# else:
#     print("Singleton failed, variables contain different instances.")


# Prototype
import copy


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class SomeComponent:
    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        """
        Поверхностное копирование. Этот метод будет вызываться когда кто-либо вызовет
        `copy.copy` с этим обьектом и возвращаемое значение будет поверхностным копированием.
        """

        # First, let's create copies of the nested objects.
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        # Then, let's clone the object itself, using the prepared clones of the
        # nested objects.
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo={}):
        """
        Глубокое копирование. Этот метод будет вызываться когда кто-либо вызовет
        `copy.deepcopy` с этим обьектом и возвращаемое значение будет глубоким копированием.
        """

        # First, let's create copies of the nested objects.
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        # Then, let's clone the object itself, using the prepared clones of the
        # nested objects.
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


if __name__ == "__main__":

    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    shallow_copied_component = copy.copy(component)

    # Let's change the list in shallow_copied_component and see if it changes in
    # component.
    # shallow_copied_component.some_list_of_objects.append("another object")
    # if component.some_list_of_objects[-1] == "another object":
    #     print(
    #         "Adding elements to `shallow_copied_component`'s "
    #         "some_list_of_objects adds it to `component`'s "
    #         "some_list_of_objects."
    #     )

    # #Let's change the set in the list of objects.
    # component.some_list_of_objects[1].add(4)
    # if 4 in shallow_copied_component.some_list_of_objects[1]:
    #     print(
    #         "Changing objects in the `component`'s some_list_of_objects "
    #         "changes that object in `shallow_copied_component`'s "
    #         "some_list_of_objects."
    #     )
    #
    deep_copied_component = copy.deepcopy(component)

    # Let's change the list in deep_copied_component and see if it changes in
    # component.
    deep_copied_component.some_list_of_objects.append("one more object")
    if component.some_list_of_objects[-1] != "one more object":
        print(
            "Adding elements to `deep_copied_component`'s "
            "some_list_of_objects doesn't add it to `component`'s "
            "some_list_of_objects."
        )

    # # Let's change the set in the list of objects.
    # component.some_list_of_objects[1].add(10)
    # if 10 not in deep_copied_component.some_list_of_objects[1]:
    #     print(
    #         "Changing objects in the `component`'s some_list_of_objects "
    #         "doesn't change that object in `deep_copied_component`'s "
    #         "some_list_of_objects."
    #     )
    #
    # print(
    #     f"id(deep_copied_component.some_circular_ref.parent): "
    #     f"{id(deep_copied_component.some_circular_ref.parent)}"
    # )
    # print(
    #     f"id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent): "
    #     f"{id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent)}"
    # )
    # print(
    #     "^^ This shows that deepcopied objects contain same reference, they "
    #     "are not cloned repeatedly."
    # )


# Proxy
# class Subject(ABC):
#     @abstractmethod
#     def request(self) -> None:
#         pass
#
#
# class RealSubject(Subject):
#     def request(self) -> None:
#         print("RealSubject: Handling request.")
#
#
# class Proxy(Subject):
#     def __init__(self, real_subject: RealSubject) -> None:
#         self._real_subject = real_subject
#
#     def request(self) -> None:
#         if self.check_access():
#             self._real_subject.request()
#             self.log_access()
#
#     def check_access(self) -> bool:
#         print("Proxy: Checking access prior to firing a real request.")
#         return True
#
#     def log_access(self) -> None:
#         print("Proxy: Logging the time of request.", end="")
#
#
# def client_code(subject: Subject) -> None:
#     subject.request()
#
#
# if __name__ == "__main__":
#     real_subject = RealSubject()
#     print("Client: Executing the same client code with a proxy:")
#     proxy = Proxy(real_subject)
#     client_code(proxy)


# Flyweight
import json
from typing import Dict


class Flyweight():
    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.", end="")


class FlyweightFactory():
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")

        return self._flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def add_car_to_police_database(
    factory: FlyweightFactory, plates: str, owner: str,
    brand: str, model: str, color: str) -> None:
    print("\n\nClient: Adding a car to database.")
    flyweight = factory.get_flyweight([brand, model, color])
    # Клиентский код либо сохраняет, либо вычисляет внешнее состояние и передает
    # его методам легковеса.
    flyweight.operation([plates, owner])


if __name__ == "__main__":
    """
    Клиентский код обычно создает кучу предварительно заполненных легковесов на
    этапе инициализации приложения.
    """

    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    factory.list_flyweights()

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "M5", "red")

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "X1", "red")

    print("\n")

    factory.list_flyweights()
