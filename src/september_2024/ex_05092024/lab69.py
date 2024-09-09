#MULTIPLE INHERITANCE

class Father:

    def father_money(self):
        return 5
    def home(self):
        return "this is from father"

class Mother:

    def mother_money(self):
        return 2
    def home(self):
        return "this is from mother"


class Son(Mother,Father):
    pass


class Son2(Father,Mother):#MRO-Method Resolution Order
    pass

s = Son()
print(s.father_money())
print(s.mother_money())
print(s.home())#incase the function name is same then the priority is given to the class which is inherited first.


s2 = Son2()
print(s2.home())

