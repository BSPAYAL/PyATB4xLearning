#CALCULATOR

class Calc:

    def __init__(self):
        print("DC")

    def sum(self,a,b):
        return a + b
    def sub(self,a,b):
        return a - b
    def mul(self,a,b):
        return a * b
    def div(self,a,b):
        return a / b
    def mod(self,a,b):
        return a % b

object_ref = Calc()
output_sum = object_ref.sum(7,5)
output_sub = object_ref.sub(7,5)
output_mul = object_ref.mul(7,5)
output_div = object_ref.div(7,5)
a = int(input("enter the value of a :"))
b = int(input("enter the value of b: "))
output_mod = object_ref.mod(a,b)

print(output_sum)
print(output_sub)
print(output_mul)
print(output_div)
print(output_mod)

