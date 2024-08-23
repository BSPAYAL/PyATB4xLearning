#Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13
#RANGE function starts from 0 by default if  no start number is mentioned

a = 0
b = 1
num = int(input("enter the number : "))
print(a,b,end =" ")
for i in range(1,num+1):
    c = a + b
    a = b
    b = c
    print(c ,end =" ")
