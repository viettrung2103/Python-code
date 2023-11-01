# Now we will program a car race. The travelled distance of a new car is initialized as zero.
# At the beginning of the main program, create a list that consists of 10 car objects created using a loop.
# The maximum speed of each new car is a random value between 100 km/h and 200 km/h.
# The registration numbers are created as follows: "ABC-1", "ABC-2" and so on. Now the race begins.
# One per every hour of the race, the following operations are performed:
#
# The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. This is done using the accerelate method.
# Each car is made to drive for one hour. This is done with the drive method.

from Car import Car
import random

ONE_HOUR = 1
RACE_LENGHT = 5000


def create_random_max_speed():
    return random.randint(100,200)

def create_car(number):
    registerNo = f"ABC -  {number}"
    max_speed = create_random_max_speed()
    return Car(registerNo,max_speed)

def checking_car_lead(leading_car: Car, another_car: Car):
    if leading_car == None:
        leading_car = another_car
    elif leading_car.distance < another_car.distance:
        leading_car = another_car

    return leading_car

def initialize_race(num_car):
    timestamp = 0
    leading_car = None
    car_list = []
    for i in range(1,num_car+1):
        car = create_car(i)
        car_list.append(car)
        leading_car =  checking_car_lead(leading_car,car)

    return [car_list, leading_car,timestamp]

def get_car_list_info(car_list):
    for car in car_list:
        print(car)

def one_hour_pass(car_list,leading_car: Car, time_stamp):
    time_stamp += 1
    for current_car in car_list:
        current_car.acceleration()
        current_car.drive(ONE_HOUR)
        leading_car = checking_car_lead(leading_car,current_car)

    return [car_list,leading_car, time_stamp]

def get_race_status(car_list, leading_car, timestamp):
    print(f"At: {timestamp}h | Leading Car: {leading_car}")
    for car in car_list:
        print(car)

def is_win(leading_car):
    return leading_car.distance >= RACE_LENGHT

def get_race_info_every_ten_hour(car_list,leading_car, timestamp):
    if timestamp % 10  == 0:
        get_race_status(car_list, leading_car, timestamp)
        print("___________")

def annouce_winner(leading_car: Car):
    print("Congratulation !!")
    print(f"THe winner is car: ${leading_car.registerNo}")

def win_race(car_list, leading_car, time_stamp, is_win_status):
    if is_win_status:
        print("The Race is completed")
        print("Here is the information of our race:")
        get_race_status(car_list, leading_car, time_stamp)
        annouce_winner(leading_car)

def race(car_list, leading_car: Car, time_stamp, is_win_status):
    while is_win_status != True:
        get_race_info_every_ten_hour(car_list,leading_car,time_stamp)
        car_list,leading_car,time_stamp = one_hour_pass(car_list,leading_car,time_stamp)
        is_win_status = is_win(leading_car)
    win_race(car_list, leading_car, time_stamp, is_win_status)


def main():
    #initialize_race
    car_list, leading_car, timestamp = initialize_race(5)
    is_win_status = is_win(leading_car)

    #race
    race(car_list, leading_car, timestamp, is_win_status)




if __name__ == "__main__":
    main()

