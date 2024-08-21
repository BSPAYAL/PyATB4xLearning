#Write a program that classifies a triangle based on its side lengths.

"""Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle."""
l1 = int(input("enter side1\n"))
l2 = int(input("enter side2\n"))
l3 = int(input("enter side3\n"))

if l1 == l2 and l2 == l3 and l3 == l1:
    print("Triangle is equilateral")
if l1 == l2 and l2 != l3 and l3 != l1 or l2 == l3 and l3 != l1 and l2 != l1 or l3 == l1 and l3 != l2 and l2 != l3:
    print("Triangle is isoceles")
if l1 != l2 and l2 != l3 and l3 != l1:
    print("Triangle is scalene")
