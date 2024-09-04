#Functions with arguments and parameters

def greet_by_name(name):
    print("Hello" , name)

result = greet_by_name("Pramod")
print(result) #results None

greet_by_name("payal")# will print payal
#name->variable name or parameter or argument
greet_by_name(3.14)#will print 3.14
greet_by_name()# error missing 1 required positional argument
greet_by_name(True)#print True
greet_by_name(true)# error as true is not defined


#it wont check the statement once error is found.in the above code only first 2 prints statement is executed and after that a error occurs so the 4th statemnet is not executed.

#above function doesnot return anything

