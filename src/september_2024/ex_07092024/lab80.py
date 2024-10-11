#Static Method and Variables

#a static method is a method that belongs to a class rather than a instance of class/object.


class MathOperations:

    def div(self,a,b):
        return a / b
    @staticmethod
    def sum(a,b):
        return a + b

o = MathOperations()
output = o.div(10,5)#gives float

print(MathOperations.sum(4,5)) #direct calling
print(output)

#static methods can be called directly called without the object