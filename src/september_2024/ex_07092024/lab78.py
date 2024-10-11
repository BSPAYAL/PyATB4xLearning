#abstarction is used to hide the internal details and architectures


from abc import ABC,abstractmethod

class Gearbox(ABC):

    @abstractmethod
    def setGear(self):
        pass



class Engine:

    @abstractmethod
    def start(self):
        pass


    @abstractmethod
    def stop(self):
        pass

class Car(Engine):

    def start(self):
        print("Starting")

    def stop(self):
        print("Stop")

    def setGear(self):
        print("Gearbox is ready")

    def drive(self):
        self.start()
        self.setGear()
        self.stop()




c = Car()
c.drive()

