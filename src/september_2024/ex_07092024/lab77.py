#ABSTRACTION-> incomplete hidden class

from abc import ABC,abstractmethod
class PyATB(ABC):

    @abstractmethod
    def payfee(self):
        pass

    def enrolled(self):
        print("enrolled")

class Amit(PyATB):
    def payfee(self):
        print("paid")

name = Amit()
name.enrolled()

#payfee has to be defined in the child class inherited from parent class