#CONSTRUCTOR

#Special Function in Class,__init__()
#It will be automatically called when you craete an Object
#class Name will always start from the Capital letter
class Dog:
    name = None

#automatically whenever a object is called
    def __init__(self,name):
        print("I am a default constructor and will be automatically called")
        self.name = name

    def sleep(self):
        print("Sleeping")



dog1 = Dog("Chow")
print(dog1.name)  # print the name Chow

dog2 = Dog("Mow")
print(dog2.name)

#2 types of constructor
#default
#parameterized
#they doesn't have any RETURN type
#name of constructor is __init__
#self is current object
#we can have unlimited number of constructor
#constructor purpose is to assign value to the instance variables declared in the class