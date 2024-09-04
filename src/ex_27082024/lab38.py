#Function Scope
#EXAMPLE OF LOCAL SCOPE
def my_function():
    a = 10
    print(a)# print a = 10 because a is declared inside the function scope,  local variable within the function

my_function()

#print(a)#gives error a is not defined


#EXAMPLE OF GLOABL SCOPE
a = 20
def my_function():
    a = 10
    print(a)# print a = 10 because a is declared inside the function scope

my_function()

print(a)# print a = 20 as value of a declared outside known as global scope

def my_function1():
    print(a)# prints a = 20

my_function1()

pa = 20
def f1():
    pa = 30
    print(pa)#prints 30
    pa = 40
    print(pa)#print 40

f1()
print(pa)#prints 20


#local variable have more preferences as compare to public variable

