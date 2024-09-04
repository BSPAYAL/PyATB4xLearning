#wap to sum of three number from the user input

num1 = int(input("enter num 1 :"))
num2 = int(input("enter num 2 :"))
num3 = int(input("enter num 3 :"))



def sum_of_three_number(n1,n2,n3):
    print(n1 + n2 + n3)# here the return type is None

result = sum_of_three_number(num1,num2,num3)#600
print(result)#none
result = sum_of_three_number(n1=num1,n2=num2,n3=num3)#600
print(result)#none

def sum_of_three_number(n1,n2,n3):
    return n1 + n2 + n3 #here it will return the value of line 22 and 24

result = sum_of_three_number(num1,num2,num3)#600
print(result)#900
result = sum_of_three_number(n1=num1,n2=num2,n3=num3)#600
print(result)#900


#practice more



