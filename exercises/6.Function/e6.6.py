# Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in euros.
# The function calculates and returns the unit price of the pizza per square meter.
# The main program asks the user to enter the diameter and price of two pizzas
# and tells the user which pizza provides better value for money (which of them has a lower unit price).
# You must use the function you wrote for calculating the unit prices.

PI = 3.14

#get area from diameter
def circle_area(dia):
    area = 0.25 * PI * (dia * 0.01)**2 # convert dia in centimeter to meter
    return area

#get the unit price of pizze
def pizza_value(dia,price):
    area = circle_area(dia)
    unit_price = price/area
    print(area)
    return unit_price

##compare value of both pizza
def compareValue(price1,price2):
    if price1 > price2:
        print("You should buy pizza 2")
    elif price1 == price2:
        print("You can buy both piza")
    else:
        print("You should buy pizza 1")
def main():
    pizza1 = [] # dia and price of pizza 1
    pizza2 = [] # dia and price of pizza 2
    piz1_dia = float(input("Input the pizza 1 diameter: "))
    piz1_price = float(input("Input the pizza 1 price: "))
    pizza1.append(piz1_dia)
    pizza1.append(piz1_price)
    piz2_dia = float(input("Input the pizza 2 diameter: "))
    piz2_price = float(input("Input the pizza 2 price: "))
    pizza2.append(piz2_dia)
    pizza2.append(piz2_price)
    # print(f"info of pizza 1: {pizza1}")
    # print(f"info of pizza 2: {pizza2}")
    unitPrice1 = pizza_value(pizza1[0],pizza1[1])
    unitPrice2 = pizza_value(pizza2[0],pizza2[1])
    print(f"the unit value of pizza 1 is: {unitPrice1:5.2f} euro/meter square")
    print(f"the unit value of pizza 2 is: {unitPrice2:5.2f} euro/meter square")
    compareValue(unitPrice1,unitPrice2)

main()