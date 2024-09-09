#HIERARCHIAL INHERITANCE

class Father:

    def bhk1(self):
        print("1BHK")



class Pramod(Father):
    def bhk2(self):
        print("2BHK")


class Amit(Father):
    def bhk3(self):
        print("3BHK")

class Lucky(Father):
    def no_house(self):
        print("no house")

p = Pramod()
p.bhk1()
p.bhk2()

a = Amit()
a.bhk1()
a.bhk3()
a.bhk2()#belongs to Pramod


