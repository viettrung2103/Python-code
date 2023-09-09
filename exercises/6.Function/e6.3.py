# Write a function that gets the quantity of gasoline in American gallons
# and returns the number converted to litres.
# Write a main program that asks for a volume in gallons
# from the user and converts the value to liters.
# The conversion must be done by using the function.
# Conversions continue until the user inputs a negative value.

GALLON = 3.785 # 1 GALLON = 3.785 LITRE
#convert gallon to litre
def gallon_to_litre(value):
    litre = value * GALLON
    return litre

#get value from user in float data type
def get_value():
    value = float(input("How much gasoline do you want to convert to litre: "))
    return value

def main():
    while True:
        try:
            value = get_value()
            while value != "":
                converted = gallon_to_litre(value)
                print(converted)
                value = get_value()
        except ValueError: ## handle empty or string input
            print("Thank you for using the application")

main()