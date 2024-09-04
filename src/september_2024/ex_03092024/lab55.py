#take input and create a class in python
class Person:
    def __init__(self):
        self.name = input("enter the name")
        self.age = input("enter the age")
        self.phone = input("enter the phone number")

    def display_info(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"Phone is {self.phone}")


#Create a object
person1 = Person()

#Call display
person1.display_info()

#no need to define the instance variables if input is taken from user