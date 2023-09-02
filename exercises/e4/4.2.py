# Write a program that converts inches to centimeters until
# the user inputs a negative value. Then the program ends.

inch = float(input("Type your measurement: "))

while inch >= 0:
    centimeter = inch * 2.54
    print(f"Result: {centimeter:5.2f} cm")
    inch = float(input("Type your measurement: "))
print(f"{inch} is a negative number")
print("Program stop.")

