class Person:
    #class variables
    #instance variables
    name = "Amit"


    def __init__(self,name):
        self.name = name
        #constructor is used to change the value of instance variables
    def walk(self, name):
        self.name = name
        print(self.name)


object_ref = Person("payal")
print(object_ref.name)


new_obj = Person("pallavi")
print(new_obj.name)


