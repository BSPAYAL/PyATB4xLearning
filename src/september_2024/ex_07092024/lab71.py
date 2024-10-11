#HIERARICAL INHERITANCE
#Method overriding says that child or subclass can have same name method as the parent or super class

class Shape:

    def area(self):
        print("Area of shape")


class Rectangle(Shape):  #is a single inheritance

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


s = Rectangle(7, 4)

print(s.area())  #first it will prefer the local and if its not present then it checks the parent area method

shape2 = Circle(10)
print(shape2.area())
