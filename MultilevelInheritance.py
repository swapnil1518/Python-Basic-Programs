# Inheritance
class Animal:
    # function. By using the “self” keyword we can access the attributes and methods of the class
    def speak(self):
        print("Animal speak")


# passing base class inside derived  so that it can access both class features
class Dog(Animal):

    def bark(self):
        print("dog barks")


class Puppy(Dog):
    def eat(self):
        print("child eat")


d = Puppy()
# creating obj of class puppy
d.speak()
# puppy class has animal class method
d.bark()
# puppy class has dog classmethod
d.eat()
# puppy class has its own method

# this is example of multi level inheritance.
# Here puppy class is eligible to inherit the properties of both Animal and Dog class.
