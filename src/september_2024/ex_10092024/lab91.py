#try,except and finally

print("start of the program")
try:
    a = int(input("enter the num1 "))
    b = int(input("enter the num2 "))
    c = a/b


except ValueError as ve:
    print("please check your inputs, u have entered a string ")
except ZeroDivisionError as zde:
    print("please check your inputs, u have entered zero ")
else:
    print("Result of div is ", c)
finally:
    print("this code will be always executed")

print("end of the program")