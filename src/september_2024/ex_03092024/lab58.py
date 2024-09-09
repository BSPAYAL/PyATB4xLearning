a = 10
class Person():
    b = 11 #instance  variable hardcoded inside the class

    def print_info(self):
        global a    #declare as Global
        a = "Hello"
        print(a)

object_ref = Person()
object_ref.print_info()

print(a)