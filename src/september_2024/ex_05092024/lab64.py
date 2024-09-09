class Myclass:

    #public instance var
    public_var = ("I am PUBLIC")

#private variable
    __private_var = "I am private"
    __password ="1234"

#protected variable
    _protected_var = "i am protected"


object = Myclass()
print(object.public_var)

#print(object.__private_var)
#print(object.__password)
#private var can be accessed outside the class

print(object._protected_var)
#protected is available within the same package

