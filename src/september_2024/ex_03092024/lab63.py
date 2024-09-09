#ENCAPSULATION

#bind the data variables and methods

#data members / Class variables
#Wrapping up data and methods within the methods


class Car:
    name = None
    password = 123


    def __init__(self):
        print("DC")

    def change_password(self):
        self.password = "pramod"

obj_ref = Car()
print(obj_ref.password)
