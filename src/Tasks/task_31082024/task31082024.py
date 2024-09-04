class Employee:
    name = None # not needed if input is taken from user

    def __init__(self):
        self.name = input("enter the employee name :")
        self.age = input("enter the employee age :")
        self.phone = input("enter the employee phone_number :")
        self.eid = input("enter the employee eid :")
        self.address = input("enter the employee address :")

    def walk(self):
        print(f"{self.name} is walking.")
    def talk(self):
        print(f"{self.name} is talking")

    def print_details(self):
        print("employee ID :", self.eid)
        print("Name : ", self.name)
        print("Age :", self.age)
        print("phone :", self.phone)
        print("Address :", self.address)

#create a object
e1 = Employee()
print("printing Employee1 details")
#call the function
e1.print_details()

e2 = Employee()
print("printing Employee2 details")
e2.print_details()





