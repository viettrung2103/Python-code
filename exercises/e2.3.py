# Write a program that asks the user for the length and width of a rectangle.
# The program then prints out the perimeter and area of the rectangle.
# The perimeter of a rectangle is the sum of the lengths of each four sides

length_str = input("Type lenght: ")
width_str = input("Type width: ")
if length_str == "" or width_str == "":
    print("Measurement is missing")
else:
    lenght = float(length_str)
    width  = float(width_str)
    perimeter = lenght*2 + width*2
    area = lenght* width
    print(f'the perimeter of the rectangle is: {perimeter}')
    print(f'the area of the rectangle is: {area}')