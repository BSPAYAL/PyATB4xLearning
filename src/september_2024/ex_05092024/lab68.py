#MULTILEVEL INHERITANCE

class Grandfather:
    gold = "2kg"


    def bhk1(self):
        print("1bhk")
class Father(Grandfather):
    diamond ="22 karat"

    def bhk2(self):
        print("2bhk")

class Son(Father):
    btc = "1BTC"

    def bhk3(self):
        print("3bhk")

son_obj = Son()
son_obj.bhk2()
son_obj.bhk3()
son_obj.bhk1()

f = Father()

g = Grandfather()
