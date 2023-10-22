# class methods must take self as paramenter
class ExampleClass:
    def __init__(self, x=0, y=0):
        print("initialized")
        self.x = x
        self.y = y
    
    # __repr__ like the java's toString
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"heyyy"
    
    def __add__(self):
        print("yes")
        


class1 = ExampleClass(1, 2)
class2 = ExampleClass(2, 3)
print(class1)
+class1
print(class1)
ExampleClass.magicProperty = "Heyyy" # adds a static field in the class

print(class1.magicProperty)

noParameterClass = ExampleClass()
print(f"{noParameterClass.x=}")
print(f"{noParameterClass.y=}")

# fields and methods that start with '__' are considered private
# fields and methods that start with '_' are considered protected

print(isinstance(class1, ExampleClass))
print(dir(ExampleClass)) # all fileds and methods of the class

# ClassName (InheritClass1, InheritClass2, ...) -> Inheritance
# The order of Inherited classes matters!!!

class Base:
    def fun(self):
        print(1)

class Child(Base):
    def fun(self):
        print(5)

child = Child()
child.fun()
    
