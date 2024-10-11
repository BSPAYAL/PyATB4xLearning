class XYZ:
    def f1(self):
        try:
            a = int(input("enter a number "))
        except Exception as e:
            print("Enter int only value of a ")
        else:
            print(a)
        finally:
            print("finally block is excuted")


x = XYZ()
x.f1()