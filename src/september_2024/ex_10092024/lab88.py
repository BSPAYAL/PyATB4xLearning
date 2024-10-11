

#ValueError and Zero division  error will get if value of a and b is not proper
#in case a = 1 and b = a it throws value error
#if a = 1 and b =0 it gives zero division error


#if u enter a value which is not integer then it gives Value Error
print("start of the program")
try:
    a = int(input("enter the num1 "))
    b = int(input("enter the num2 "))
    c = a/b
    print("Result of div is ", c)

except Exception as e:
    print(e)
    print("please check your inputs, it shouldn't be a string or zero")


print("end of the program")