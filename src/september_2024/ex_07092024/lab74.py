#OOPS
#Class - Blueprint
#Object - Instance of class
#Encapsualtion(hiding internal functions) - Private ,__private,_protected
#Inheritance -single,multiple,multi level,hierarcial,hybrid
#Polymorphism - method overriding ,method overloading
#self,super,__init__
#ABSTRACTION -hide details(hiding class level) and show what is required

#Car - key which was marked as private
#car -created with multiple other classes


#from abc import ABC,abstractclassmethod

#abc -> means abstract
from abc import ABC,abstractmethod
class Animal(ABC):

    def __init__(self,name):
        self.name = name
    @abstractmethod  #this is a function marked #this is incomplete method
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Brak")

dog = Dog("PP")#this will call the latest sound function
dog.sound()