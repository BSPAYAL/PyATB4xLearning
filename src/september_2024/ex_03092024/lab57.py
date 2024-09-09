#PARAMETERIZED CONSTRUCTOR

class Calc:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
    def mod(self):
        return self.a % self.b

object_ref = Calc(7,5)
output_sum = object_ref.sum()
output_sub = object_ref.sub()
output_mul = object_ref.mul()
output_div = object_ref.div()
output_mod = object_ref.mod()

print(output_sum)
print(output_sub)
print(output_mul)
print(output_div)
print(output_mod)

#python package can call each other whenever required
