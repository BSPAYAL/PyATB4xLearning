#Method overriding - Same name in the parent and child
#child always override the parent functions
#super means call my parent function

class GrandFather:
    x =10

    def home(self):
        print("Old home")

class Father(GrandFather):
    a = 10
    def home(self):
        print("1BHK")
        print(self.a)
        print(super().x)


class Son(Father):
    b = 10

    def home(self):
        super().home() #want to call father function
        print("no house")
        print(self.b)

p = Son()
p.home() #will call his home
print(p.x) #son object can access granfather instance variable


#super  -> parent ,Super class,Father
#self -> me
#Father behaviour and attributes can be accessed by using super keyword
#we can't access grandfather directly from son using super keyword