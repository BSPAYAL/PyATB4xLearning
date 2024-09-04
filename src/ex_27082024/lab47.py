import math
def give_me_power(num):
    return math.pow(num,2)

op = give_me_power(10)
print(op)

#pow always return floating number

op2 = lambda num : math.pow(num,2)
print(op2)