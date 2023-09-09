# Write a program that asks the user for the radius of a circle and the prints out the area of the circle.

PI = 3.14
radius_str = input("What is the radius size: ")
if radius_str == "" :
    print("The user has not provide the radius")
else:
    radius = float(radius_str);
    area = radius * radius * PI;
    print(f"Area of the circle: {area}")
