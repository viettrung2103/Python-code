# Write a program that asks the user for the radius of a circle and the prints out the area of the circle.

radius_str = input("What is the radius size: ")
radius = float(radius_str);
PI = 3.14

if radius == None :
    print("The user has not provide the radius")
else:
    area = radius * radius * PI;
    print(f"Area of the circle: {area}")