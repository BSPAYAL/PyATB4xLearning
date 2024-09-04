def sum_of_three_number(a,b,c):
    return a + b + c

result = sum_of_three_number(10,20,30)
print(result)




#with default passed values
def sum_of_three_number(a,b,c=15):
    return a + b + c

result = sum_of_three_number(10,20)
result = sum_of_three_number()# in this case the default value should be passed
print(result)

#default value of c used is 15

#if want to pass only a and c value
result = sum_of_three_number(a=10,c=20)