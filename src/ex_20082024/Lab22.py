#Grade Calculator

#WAP that calculates and displays the letter grade
mark = float(input("enter the mark\n"))
if(mark >= 90 and mark <= 100):
    print("Grade is A")
elif(mark >= 80 and mark <= 89):
    print("Grade is B")
elif(mark >= 70 and mark <= 79):
    print("Grade is C")
elif(mark >= 60 and mark <= 69):
    print("Grade is D")
else:
    print("Grade is F")
