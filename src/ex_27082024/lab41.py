#DECORATORS

#decorators in python are a way to modify the behaviour of a class or functions without changing its source code.
#powerful tool that allows you to wrap another functio and extend its functionality while keeping the original function's code unchanged

#def add_security(func):
#func is custom funcn where you want extra functionality
#two parts
# wrapper and call
#wrapper class  can be name anything


def my_decorator(func):
    # two parts
    # wrapper and call
    def wrapper():
        print("something is happening before function is called")
        print("Add Helmet, Dashcam, gloves,knee guards")
        func()
        #drive_bike is called in func
        print("something is happening after function is called")
        print("Safe driving")

    return wrapper #wrapper calling itself to return
#defination
@my_decorator
def drive_bike():
    print("i am driving")



#call to the function
drive_bike()

@my_decorator
def test_ui():
    print("i will test the UI")

test_ui()


