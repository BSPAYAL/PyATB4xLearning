#PyATB Students

#Attributes (by which u can recognize yourself)- name, age ,gender,id,address
#Behaviour(what you do)

class Person:
    #Attributes
    id = None
    name = None
    age = None
    email = None
    gender = None

    #behaviour

    def talk(self): #self -this is the first argument in every behaviour
        print("i can talk")

    def sleep(self,name): #arg with No Return
        print("I am a Method!!")
        print("Sleep",name)

    def sleep2(self,name): #Arg with Return
        print("I am a Method!!")
        return None

    def walk(self):
        print("I am walking")

    def walk_return(self): #No Arg with Return
        return "I am walking"

#create an object of the Class
#ObjectRef = ClassName() -> Object
tushar = Person()
tushar.name = "tushar"
print(tushar.name)
tushar.talk() #calling the function

rajyalaxmi = Person()
rajyalaxmi.name = "rajyalaksmi"
print(rajyalaxmi.name)
