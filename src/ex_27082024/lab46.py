def find_odd_even(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

#find_odd_even(5)


#in lambda

find_odd_even = lambda num : "Even" if num%2 == 0 else "odd"
print(find_odd_even(5))
