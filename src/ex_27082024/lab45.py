def add_10(n):
    return n + 10
o = add_10(100)
print(o)

#convert to lambda
o = lambda n : n + 10
print(o(100))



def mul(a,b):
    return(a*b)

oo = lambda a,b : a*b
print(oo(5,6))

new = lambda a,b,c : a+b+c
print(new(7,7,8))#calling and print

