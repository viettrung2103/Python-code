# 1: December   Winter
# 2: January
# 3: February
# 4: March      Spring
# 5: April
# 6: May
# 7: June       Summer
# 8: July
# 9: August
# 10: September  Autumn
# 11: October
# 12: November

season = ("winter","spring","summer","autumn")
month = ("December","January","February","March","April","May","June","July","August","September","October","November")
def ask_month():
    try:
        number =int(input("Input month number(1-12, December is 1):"))
        return number
    except ValueError:
        print("You have input wrong")

def ask_season(number):
     season_index = (number -1) // 3
     print(f"The season is: {season[season_index]} ")

    # by using floor, we can find season that the month belong
    # (12 -1)/3 = 3 >> month[3] => Spring

def main():
    while True:
        number = ask_month()
        ask_season(number)

main()