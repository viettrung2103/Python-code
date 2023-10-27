from Car import Car
import random

MAX_RANDOM_SPEED = 200
MIN_RANDOM_SPEED = 100
ONE_HOUR = 1
RACE_DISTANCE = 10000
# STARTING_NUMBER = 0

class CarRace():
    def __init__(self,name,kilometer,num_car):
        ##car_list is number of car in a race
        self.name = name
        self.kilometer = kilometer
        # self.num_car = num_car
        self.duration = 0
        self.leadingCar: Car = None # check the leading car
        self.carList =[]
        self.createCarList(num_car)
        # self.isWin = False

    def createCar(self,number):
        registerNo = f"ABC - {number}"
        maxSpeed = random.randint(100,200)
        return Car(registerNo,maxSpeed)

    def createCarList(self,num_car):
        for i in range(1,num_car):
            car = self.createCar(i)
            self.carList.append(car)
            self.checkLeading(car) ## assign the first created car as the leading car

    def getCarList(self):
        for car in self.carList:
            print(car)
        # return self.carList

    def checkLeading(self,another: Car):
        if self.leadingCar == None:
            self.leadingCar = another
        elif self.leadingCar.distance < another.distance:
            self.leadingCar = another
        else:
            self.leadingCar = self.leadingCar



    def changeSpeedInOneHour(self):
        for car in self.carList:
            car.acceleration()
            car.drive(ONE_HOUR)
            self.checkLeading(car)

    def hour_passes(self):
        self.duration = self.duration + ONE_HOUR
        self.changeSpeedInOneHour()

    def print_status(self):
        print(f"At: {self.duration}h | Leading Car: {self.leadingCar}")
        for car in self.carList:
            print(car)

    def isWin(self):
        return self.leadingCar.distance > self.kilometer

    def annouceWin(self,car):
        print("Congratulation !!")
        print(f"THe winner is car: ${car.registerNo}")


    def race(self):

        while self.isWin() == False :
            if self.duration % 10 == 0:
                self.print_status()
            self.hour_passes()
            # self.showRaceInfo()
        print("_____________________________")
        print("Race is completed")
        print("Here is the information of our race:")
        self.print_status()
        self.annouceWin(self.leadingCar)

if __name__ == "__main__":
    carRace = CarRace("Grand Demolition Derby",8000,10)
    # carRace.createCarList()
    # carRace.print_status()
    carRace.race()