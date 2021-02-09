from __future__ import annotations
from abc import ABC, abstractmethod


# Bridge
# class Abstraction:
#     def __init__(self, implementation: Implementation) -> None:
#         self.implementation = implementation
#
#     def operation(self) -> str:
#         return (f"Abstraction: Base operation with:\n"
#                 f"{self.implementation.operation_implementation()}")
#
#
# class ExtendedAbstraction(Abstraction):
#     def operation(self) -> str:
#         return (f"ExtendedAbstraction: Extended operation with:\n"
#                 f"{self.implementation.operation_implementation()}")
#
#
# class Implementation(ABC):
#     @abstractmethod
#     def operation_implementation(self) -> str:
#         pass
#
#
# class ConcreteImplementationA(Implementation):
#     def operation_implementation(self) -> str:
#         return "ConcreteImplementationA: Here's the result on the platform A."
#
#
# class ConcreteImplementationB(Implementation):
#     def operation_implementation(self) -> str:
#         return "ConcreteImplementationB: Here's the result on the platform B."
#
#
# def client_code(abstraction: Abstraction) -> None:
#     print(abstraction.operation(), end="")
#
#
# implementation = ConcreteImplementationA()
# abstraction = Abstraction(implementation)
# client_code(abstraction)
#
# print("\n")
#
# implementation = ConcreteImplementationB()
# abstraction = ExtendedAbstraction(implementation)
# client_code(abstraction)

# Facade
# class Facade:
#     def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
#         self._subsystem1 = subsystem1 or Subsystem1()
#         self._subsystem2 = subsystem2 or Subsystem2()
#
#     def operation(self) -> str:
#         results = []
#         results.append("Facade initializes subsystems:")
#         results.append(self._subsystem1.operation1())
#         results.append(self._subsystem2.operation1())
#         results.append("Facade orders subsystems to perform the action:")
#         results.append(self._subsystem1.operation_n())
#         results.append(self._subsystem2.operation_z())
#         return "\n".join(results)
#
#
# class Subsystem1:
#     def operation1(self) -> str:
#         return "Subsystem1: Ready!"
#
#     def operation_n(self) -> str:
#         return "Subsystem1: Go!"
#
#
# class Subsystem2:
#     def operation1(self) -> str:
#         return "Subsystem2: Get ready!"
#
#     def operation_z(self) -> str:
#         return "Subsystem2: Fire!"
#
#
# def client_code(facade: Facade) -> None:
#     print(facade.operation(), end="")
#
#
# subsystem1 = Subsystem1()
# subsystem2 = Subsystem2()
# facade = Facade(subsystem1, subsystem2)
# client_code(facade)

# Adapter
# class Target:
#     def request(self) -> str:
#         return "Target: The default target's behavior."
#
#
# class Adaptee:
#     def specific_request(self) -> str:
#         return ".eetpadA eht fo roivaheb laicepS"
#
#
# class Adapter(Target):
#     def __init__(self, adaptee: Adaptee) -> None:
#         self.adaptee = adaptee
#
#     def request(self) -> str:
#         return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"
#
#
# def client_code(target: Target) -> None:
#     print(target.request(), end="")
#
#
# print("Client: I can work just fine with the Target objects:")
# target = Target()
# client_code(target)
# print("\n")
#
# adaptee = Adaptee()
# print("Client: The Adaptee class has a weird interface. "
#           "See, I don't understand it:")
# print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")
#
# print("Client: But I can work with it via the Adapter:")
# adapter = Adapter(adaptee)
# client_code(adapter)


# Chain of responsibility
# from typing import Any, Optional
#
#
# class Handler(ABC):
#     @abstractmethod
#     def set_next(self, handler: Handler) -> Handler:
#         pass
#
#     @abstractmethod
#     def handle(self, request) -> Optional[str]:
#         pass
#
#
# class AbstractHandler(Handler):
#     _next_handler: Handler = None
#
#     def set_next(self, handler: Handler) -> Handler:
#         self._next_handler = handler
#         # Возврат обработчика отсюда позволит связать обработчики простым
#         # способом, вот так:
#         # monkey.set_next(squirrel).set_next(dog)
#         return handler
#
#     @abstractmethod
#     def handle(self, request: Any) -> str:
#         if self._next_handler:
#             return self._next_handler.handle(request)
#
#         return None
#
#
# class MonkeyHandler(AbstractHandler):
#     def handle(self, request: Any) -> str:
#         if request == "Banana":
#             return f"Monkey: I'll eat the {request}"
#         else:
#             return super().handle(request)
#
#
# class SquirrelHandler(AbstractHandler):
#     def handle(self, request: Any) -> str:
#         if request == "Nut":
#             return f"Squirrel: I'll eat the {request}"
#         else:
#             return super().handle(request)
#
#
# class DogHandler(AbstractHandler):
#     def handle(self, request: Any) -> str:
#         if request == "MeatBall":
#             return f"Dog: I'll eat the {request}"
#         else:
#             return super().handle(request)
#
#
# def client_code(handler: Handler) -> None:
#     for food in ["Nut", "Banana", "Cup of coffee"]:
#         print(f"\nClient: Who wants a {food}?")
#         result = handler.handle(food)
#         if result:
#             print(f"  {result}", end="")
#         else:
#             print(f"  {food} was left untouched.", end="")
#
#
# monkey = MonkeyHandler()
# squirrel = SquirrelHandler()
# dog = DogHandler()
#
# monkey.set_next(squirrel).set_next(dog)
#
# # Клиент должен иметь возможность отправлять запрос любому обработчику, а не
# # только первому в цепочке.
# print("Chain: Monkey > Squirrel > Dog")
# client_code(monkey)
# print("\n")
#
# print("Subchain: Squirrel > Dog")
# client_code(squirrel)

#Visitor
# from typing import List
#
#
# class Component(ABC):
#     @abstractmethod
#     def accept(self, visitor: Visitor) -> None:
#         pass
#
#
# class ConcreteComponentA(Component):
#     def accept(self, visitor: Visitor) -> None:
#         visitor.visit_concrete_component_a(self)
#
#     def exclusive_method_of_concrete_component_a(self) -> str:
#         return "A"
#
#
# class ConcreteComponentB(Component):
#     def accept(self, visitor: Visitor):
#         visitor.visit_concrete_component_b(self)
#
#     def special_method_of_concrete_component_b(self) -> str:
#         return "B"
#
#
# class Visitor(ABC):
#     @abstractmethod
#     def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
#         pass
#
#     @abstractmethod
#     def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
#         pass
#
#
# class ConcreteVisitor1(Visitor):
#     def visit_concrete_component_a(self, element) -> None:
#         print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor1")
#
#     def visit_concrete_component_b(self, element) -> None:
#         print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor1")
#
#
# class ConcreteVisitor2(Visitor):
#     def visit_concrete_component_a(self, element) -> None:
#         print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor2")
#
#     def visit_concrete_component_b(self, element) -> None:
#         print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor2")
#
#
# def client_code(components: List[Component], visitor: Visitor) -> None:
#     for component in components:
#         print(component)
#         component.accept(visitor)
#
#
#
# components = [ConcreteComponentA(), ConcreteComponentB()]
#
# print("The client code works with all visitors via the base Visitor interface:")
# visitor1 = ConcreteVisitor1()
# client_code(components, visitor1)

# print("It allows the same client code to work with different types of visitors:")
# visitor2 = ConcreteVisitor2()
# client_code(components, visitor2)

#Memento
# from datetime import datetime
# from random import sample
# from string import ascii_letters, digits
#
#
# class Originator():
#     _state = None
#
#     def __init__(self, state: str) -> None:
#         self._state = state
#         print(f"Originator: My initial state is: {self._state}")
#
#     def do_something(self) -> None:
#         print("Originator: I'm doing something important.")
#         self._state = self._generate_random_string(30)
#         print(f"Originator: and my state has changed to: {self._state}")
#
#     def _generate_random_string(self, length: int = 10) -> None:
#         return "".join(sample(ascii_letters, length))
#
#     def save(self) -> Memento:
#         return ConcreteMemento(self._state)
#
#     def restore(self, memento: Memento) -> None:
#         self._state = memento.get_state()
#         print(f"Originator: My state has changed to: {self._state}")
#
#
# class Memento(ABC):
#     @abstractmethod
#     def get_name(self) -> str:
#         pass
#
#     @abstractmethod
#     def get_date(self) -> str:
#         pass
#
#
# class ConcreteMemento(Memento):
#     def __init__(self, state: str) -> None:
#         self._state = state
#         self._date = str(datetime.now())[:19]
#
#     def get_state(self) -> str:
#         return self._state
#
#     def get_name(self) -> str:
#         return f"{self._date} / ({self._state[0:9]}...)"
#
#     def get_date(self) -> str:
#         return self._date
#
#
# class Caretaker():
#     def __init__(self, originator: Originator) -> None:
#         self._mementos = []
#         self._originator = originator
#
#     def backup(self) -> None:
#         print("\nCaretaker: Saving Originator's state...")
#         self._mementos.append(self._originator.save())
#
#     def undo(self) -> None:
#         if not len(self._mementos):
#             return
#
#         memento = self._mementos.pop()
#         print(f"Caretaker: Restoring state to: {memento.get_name()}")
#         try:
#             self._originator.restore(memento)
#         except Exception:
#             self.undo()
#
#     def show_history(self) -> None:
#         print("Caretaker: Here's the list of mementos:")
#         for memento in self._mementos:
#             print(memento.get_name())
#
#
# if __name__ == "__main__":
#     originator = Originator("Super-duper-super-puper-super.")
#     caretaker = Caretaker(originator)
#
#     caretaker.backup()
#     originator.do_something()
#
#     caretaker.backup()
#     originator.do_something()
#
#     caretaker.backup()
#     originator.do_something()
#
#     print()
#     caretaker.show_history()
#
#     print("\nClient: Now, let's rollback!\n")
#     caretaker.undo()
#
#     print("\nClient: Once more!\n")
#     caretaker.undo()


# Mediator
class Mediator(ABC):
    def notify(self, sender: object, event: str) -> None:
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()


class BaseComponent:
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Component 1 does A.")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Component 1 does B.")
        self.mediator.notify(self, "B")


class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component 2 does C.")
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        print("Component 2 does D.")
        self.mediator.notify(self, "D")


if __name__ == "__main__":
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)

    print("Client triggers operation A.")
    c1.do_a()

    print("\n", end="")

    print("Client triggers operation D.")
    c2.do_d()

