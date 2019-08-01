class Animal:                                                               # Parent class
    def __init__(self):
        print(" - Animal, Initialized")

    def eat(self):
        print("Eating...")


class Dog(Animal):                                                          # Child class
    def __init__(self):
        print("Dog ", end="")
        super(Dog, self).__init__()                                         # Used to call the constructor of parent class

    def bark(self):
        print("Barking...")


class Cat(Animal):                                                          # Child class
    def __init__(self):
        print("Cat ", end="")
        super(Cat, self).__init__()

    def meow(self):
        print("Meowing...")


c1 = Cat()

c1.eat()                                                                    # Using parent class method from a child class instance
c1.meow()

d1 = Dog()

d1.eat()
d1.bark()