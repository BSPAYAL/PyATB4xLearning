#CUSTOM EXCEPTION
class MyCustomException(Exception):

    def __init__(self,message):
        self.message = message
        super().__init__(message) #calling parent's constructor

balance = 100
withdraw = int(input("enter the amt"))
if withdraw > balance:
    raise MyCustomException("balance is low")
else:
    print("remaning amt")