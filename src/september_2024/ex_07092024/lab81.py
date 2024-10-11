class MathOperations:

    def div(self,a,b): #non static variable
        return a / b
    @staticmethod
    def sum(a,b):
        return a + b

    @staticmethod
    def sub(a,b):
        return a - b

o = MathOperations()
output = o.div(10,5)#gives float
print(MathOperations.sum(4,5))
print(MathOperations.sub(30,15))

 #direct calling
print(output)

#static methods can be called directly called without the object
#static belongs to class not a object