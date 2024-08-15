#take user input and calculate the sum,sub,mul and division
num1 = input("Enter the first number : ")
num2 = input("enter the second number : ")
print("sum is ",num1+num2)

#if num1 is 4 and num2 is 7 then sum becomes 47 instead of 11.
#num1 and num2 are string so instead of sum it concatenates will results in 47
#so we need to convert the str before addition

num1 = int(input("Enter the first number : "))
num2 = int(input("enter the second number : "))

#-> here the number will be added since num1 and num2 are integers now
print("sum is ",num1+num2)

#output
"""Enter the first number : 4
enter the second number : 7
sum is  47
Enter the first number : 7
enter the second number : 7
sum is  14"""


print("division is", num1/num2)
#division always give floating number
"""Enter the first number : 7
enter the second number : 1
sum is  8
division is 7.0"""