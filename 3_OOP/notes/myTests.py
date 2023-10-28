import json


class Example:
    def __init__(self, value):
        self.value = value - 1
        self._value = value + 1
        self.__value = value

    def get_value(self):
        return self.__value

e = Example(5)
print(e.value)
print(e._value)
e._value = 42
print(e._value)
print(e.get_value())
print()

class Base:
    x = 32

    def __init__(self):
        self.x = 23

    def printInfo(self):
        print("I am called")

    def foo(self):
        print("foo")

class SubClass(Base):
    def __init__(self):
        super().printInfo()
        self.x = 999

    # Overriding
    def foo(self):
        print("foo child")


b = Base()
print(f"{b.x=}")

sub = SubClass()
print(f"{sub.x=}")
sub.foo()
print()

class JSONSerializableMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

class DebugMixin:
    def __repr__(self):
        arguments = ", ".join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({arguments})"


class Person(JSONSerializableMixin, DebugMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person, JSONSerializableMixin, DebugMixin): # Order of defining parents is crucial
    def __init__(self, name, age, salary):
        self.salary = salary
        super().__init__(name, age)

elon = Employee("Elon Musk", 51, 1_000_000_000)
print(f"{elon.to_json() = }")
print(f"{elon = }")

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __bool__(self):
        """Return `True` only for (0, 0)."""
        return not (not self.x and not self.y)
    
p = Point(2, 3)

print(f"{str(p) = }")
print(f"The `__str__` method is called when using string interpolation: {p}")
print(f"If we want to use the `__repr__` instead we should write it like this: {p!r}")

print(f"{bool(p) = }")

# `__bool__` is useful when building conditions

if p:
    print("p is truthy")

z = Point()

if not z:
    print("z is falsey")

# only immutable objects can be hashed
print(hash(1))
print(hash("a"))
print(hash((1, "a", False)))

array = [1] * 4
for i in array:
    print(i)


# Calling an object as a function - just override the __call__ method
class Double:
    def __call__(self, x):
        return x * 2
    
print(f"{Double()(4)=}")

func = Double()
print(f"{func(3)=}")


class Player:
    def __init__(self, name):
        self._name = name

    # Getter in Python 
    @property
    def name(self):
        return self._name

doncho = Player("Doncho")
print(doncho.name)


# By the way we can override classes haha
class Player:
    def __init__(self, xp):
        self._xp = xp

    @property
    def level(self):
        return self._xp // 1000 + 1
    
    @level.setter
    def level(self, value):  # has to have the same name!
        self._xp = (value - 1) * 1000
    
newb = Player(0)
print(f"{newb.level = }")

print("now the player buys something and advances some levels automatically...")
newb.level = 10  # ...cheater

print(f"{newb.level = }")
print(f"{newb._xp = }")


class A:
    @staticmethod
    def static_method():
        print("I am free")

a = A()
A.static_method()
a.static_method()


class User:
    def __init__(self, username, email, money):
        self.username = username
        self.email = email
        self.money = money

    @classmethod
    def from_json_dict(cls, json):
        username = json["username"]
        email = json["email"]
        money = json["money"]
        return cls(username, email, money)

    def __repr__(self):
        return f"User({self.username}, {self.email}, {self.money})"


json_data = {
    "username": "yalishanda",
    "email": "yalishanda@example.com",
    "money": 420
}

user = User.from_json_dict(json_data)
print(user)


from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def make_sound(self):
        pass

    def pet(self):
        print(f"Petting {self._name}...")
        self.make_sound()

class Dog(Animal):
    def make_sound(self):
        print("woof")

class Cat(Animal):
    def make_sound(self):
        print("purr")

class Snek(Animal):
    def make_sound(self):
        print("sss")

doge = Dog("Doge")
doge.pet()

catto = Cat("Мишо")
catto.pet()

snek = Snek("Съска")
snek.pet()