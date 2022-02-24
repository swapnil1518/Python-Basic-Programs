# It is nothing but a constructor. It is a special method in python class used to initialize the vriables.

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
