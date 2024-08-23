#Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

user_input =int(input("enter a number : "))
fact = 1
for i in range(1, user_input+1):
    fact = i * fact
print("Factorial of ", user_input ,"is",fact)