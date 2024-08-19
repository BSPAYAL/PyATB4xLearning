#Write a Python program to calculate the area of a circle given its radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)

radius = int(input("enter the radius :"))

area = 3.14 * pow(radius,2)
print("Area of a circle is", area)
print(f"Area of a circle is -> {area:.2f}")