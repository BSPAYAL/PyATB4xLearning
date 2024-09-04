

def greet(name):
    print("Hello " ,name)

name = input("enter your name\n")# providing input from user to the parameter
greet(name)

#user defined -> 4 types
#1.they can't return anything.
#No return type and No parameter/argument -NRNP
#example of no return type:-
def greet():
    print("Hello")

result = greet()
print(result) #returns None

#2.No return type and  parameter:-
def greet(name):
    print("Hello " ,name)
    print("Hello ", name.upper())#print the string in upper
greet("Payal")

#3.No return type and with Default parameter:-
def say_hello_default_arg(name="pramod"):
    print("Hello ",name)

say_hello_default_arg("Payal")
say_hello_default_arg() # print Pramod if no argument is passed during function call
say_hello_default_arg(name="tushar")#print Tushar called as positional argument giving


#with multiple arguments
def multiple_args(name1,name2,name3):
    print("Multiple Arguments", name1, name2, name3)

#with default value
def multiple_args(name1 = "ram",name2 ="sumit",name3 = "rajesh"):
    print("Multiple Arguments", name1, name2, name3)

multiple_args(name1 ="laksham", name2 = "sita", name3 ="hanuman")

#when function is called if the parameter value is passed then it will print it else it will print the default value.
#you can pass one argument for other default value will be printed
#4. Argument + return type
def sum_of_two_number(num1,num2):
    return num1+num2

result = sum_of_two_number(10,20)
result = sum_of_two_number(num1=10,num2=20)#positional argument
print(result)

#with default value
def sum_of_two_number(num1=100,num2=200):
    return num1+num2

result = sum_of_two_number()
print(result)