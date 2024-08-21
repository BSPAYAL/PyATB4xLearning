#Problem to find max between three number

#as per requirement the data can be  int or float

num1 = int(input("enter the first number \n"))
num2 = int(input("enter the second num \n"))
num3 = int(input("enter the third num \n"))


if (num1 > num2 and num1 > num3):
    print("Maximum number is ", num1)
elif(num2 > num1 and num2 > num3):
    print("Maximum number is ", num2)
else:
    print("Maximum number is ", num3)
