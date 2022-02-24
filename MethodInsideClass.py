class Human:
# declaring variable inside class and not passing anything at this moment
    name = None
    age =None
# creating a menthod of Human class to get the name and age from the user
    def get_name(self):
        print("Enter your name")
        self.name = input()
    def get_age(self):
        print("Enter your age")
        self.age = input()
    def put_name(self):
        print("Your name is :",self.name)
    def put_age(self):
        print("Your age is :", self.age)
person1 = Human()
#obj name is person1 and creating instance of Human class
person1.get_name()
person1.get_age()
# calling the method by objects
person1.put_name(), person1.put_age()



"""
name = input("Enter Your name :")
age = int(input("Enter your age :"))
print("Your name is :" ,name)
print("Your age is : ", age)
"""