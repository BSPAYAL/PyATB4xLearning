#SINGLE INHERITANCE


class Parent:
    gold = "2kg"


    def BHK2(self):
        print("2BHK")

class Child(Parent):
    key2 = "diamond"
    def BHK3(self):
        print("3BHK")

child_object = Child()
print(child_object.gold)
child_object.BHK3()
child_object.BHK2()
print(child_object.key2)

father_obj = Parent()
father_obj.BHK2()
#father_obj.BHK3()#not possible error
print(father_obj.key2)




