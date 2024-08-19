#- Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.


num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

if(num1>num2):
    print("First number is greater than second")
elif(num1 == num2):
    print("First number is equal to second")
else:
    print("First number is less than second")