# Parent class
class Animal:

    def eat(self):
        print("Animal is eating")


# Child class
class Dog(Animal):

    def bark(self):
        print("Dog is barking")

# Creating object
d1 = Dog()

d1.eat()
d1.bark()