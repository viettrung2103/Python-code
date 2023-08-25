"""
a= "4"
print(a)
abc="3"
print(abc)
"""
# print(type("4"))
# print(type(4))
"""
import math

a= 1
b = 2
c =3

print(a+b+c)
print(a+b)
print(a+b)
print(a+b)
print(a+b)
print(a+b)
# print(b+d)

# print(math.pi)
print(f"{math.pi}")
print(f"{math.pi:15.6f}")

# ten = input("Nhap ten")
# year = input(" Nhap year")
# print(f"chao {ten}, toi sinh nam {year}")
"""



"""
DAY_IN_SECONDS = 86400

day_str= input("How many day(s): ")
day = int(day_str)
total = day * DAY_IN_SECONDS

print(f"Seconds in that many days: {total}")

"""

eat_time = int(input("How many times you eat in a cafeteria: "))
price_lunch = float(input("How much it costs for one lunch: "))
grocery_cost = float(input("how much you spend on groceries in a week: "))


total = eat_time * price_lunch + grocery_cost
total_day = total/7

print("Average food expenditure:")
print(f"Daily: {total_day:4.1f}")
print(f"Weekly: {total:4.1f}")


