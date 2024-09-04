class Dog: #class Name will always start from the Capital letter
    name = None
    breed = None
    color = None

    def sleep(self):
        print("Sleeping")

    def bark(self):
        print("bark")

    def eat(self,food):
        print(food)

dog1 = Dog()
print(dog1.name)#print the default value None

dog1.name = "Chow"
print(dog1.name)#print the name Chow

print("-------------------------------------------------")
#creating second object dog2
dog2 = Dog()
dog2.name ="Mow"
print(dog2.name)