# It is nothing but a constructor. It is a special method in python class used to initialize the vriables..

class Student:
# init is method so using def to define it
    def __init__(self,name,age,branch):
     self.name = name
     self.age = age
     self.branch = branch
    def print_student(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Branch", self.branch)
student1 = Student("Swapnil",23,"IT")
#creating obj
student1.print_student()
#calling method


"""
Constructor : 
Constructor is executed when we create the object of this class. 
In Python the __init__() method is called the constructor and is always called when an object is created.
Each time an object is created a method is called. That methods is named the constructor.
"""
""" 
Types of constructors : 

default constructor: The default constructor is a simple constructor which doesn’t accept any arguments. 
Its definition has only one argument which is a reference to the instance being constructed.
parameterized constructor: constructor with parameters is known as parameterized constructor. 
The parameterized constructor takes its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.
"""
