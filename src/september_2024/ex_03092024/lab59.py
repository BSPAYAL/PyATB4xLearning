#we should always create python packages instead of normal directory
#python interpreter can recognize them easily

#VARIABLES

#1.local (within the function/block)
#2.Global
#3.Instance variables| attributes(within the class)
#4.static variable

a = 10
class Person():
    b = 11 #instance  variable hardcoded inside the class

    def print_info(self):
        print(a)
#        print(b) #gives error as b is not defined
        print(self.b) # this is how we can use

object_ref = Person()
object_ref.print_info()

print(a)
#print(b) #gives error as b is not defined
#print(self.b) #can not be used outside class
#self is used only for instance variables


