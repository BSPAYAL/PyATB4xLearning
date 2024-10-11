#Method Overloading
#Python doesnot support method overloading
#same function name but work is different

class MathUtils(object): #every class is a object class and has single inheritance
    def add(self,a,b):
        return a + b
    def add(self,a,b,c=0):
        return a + b + c

math = MathUtils()
op1 = math.add(2,4)#gives Error
print(op1)

#python doesnot support method overloading except for default parameters
#method overloading(Same name within class) is concept in class with same name and different parameters but not supported in Python

#method overrriding- is within one or more class.father and son have same function

#method overloading - is within the class, son has 2 same function