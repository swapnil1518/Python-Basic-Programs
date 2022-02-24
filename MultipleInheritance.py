class Animal:
    def speak(self):
        print("dog speaking")


class Dog:
    def bark(self):
        print("dog barking")


class Puppy(Animal,Dog):
    def eat(self):
        print("child eating")


d = Puppy()
# d=dog  # error because in dog class we have  not passes animal class so no inheritance is working here
d.speak()
d.bark()
d.eat()

# This is an example of multiple inheritance
# here we inherit properties of both animal and dog class 
