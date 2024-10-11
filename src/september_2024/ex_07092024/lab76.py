from abc import ABC,abstractmethod
class Father(ABC):

    def __init__(self,name):
        self.name = name

#ABC ->which is abstract class which we have to inherit to create a incomplete method

    @abstractmethod
    def loan(self):
        pass #means skip


class Pramod(Father):

    def loan(self):
        print("Paid the loan")

pr = Pramod("100")
pr.loan()

#pramod has to create the loan function else his object cannot be created
