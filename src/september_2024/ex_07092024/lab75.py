from abc import ABC,abstractmethod
class Animal(ABC):

    def __init__(self,name):
        self.name = name
    @abstractmethod  #this is incomplete method
    def sound(self):
        pass


class Dog(Animal):
    pass



dog = Dog("PP")#this will call the latest sound function
dog.sound()

#ERROR ->Can't instantiate abstract class Dog without an implementation for abstract method 'sound' in child class
#we need to complete the function before creating a child object if we have inherited the parent class
