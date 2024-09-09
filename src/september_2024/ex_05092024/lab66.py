#INHERITANCE

class Father:
    key = "2BHK"

    def car(self):
        print("Father Car!!","ALTO")

#SElf is reference to current object, default parameter in class object, u can use instance variable using this
class Son(Father):
    key2 ="BHK"

    def truck(self):
        print("Truck")

father_obj = Father()
father_obj.car()

son_object = Son()
son_object.car()
print(son_object.key)


#father can't access any method or member variable from son


