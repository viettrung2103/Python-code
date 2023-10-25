from Car import Car
import random

MAX_RANDOM_SPEED = 200
MIN_RANDOM_SPEED = 100
ONE_HOUR = 1
RACE_DISTANCE = 10000
# STARTING_NUMBER = 0

class CarRace():
    def __init__(self):
        self.duration = 0
        self.carList = []
        # self.isWin = False
        self.leadingCar: Car = None # check the leading car

    def createCar(self,number):
        registerNo = f"ABC - {number}"
        maxSpeed = random.randint(100,200)
        return Car(registerNo,maxSpeed)

    def createCarList(self):
        for i in range(1,11):
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

    def advanceOneHour(self):
        self.duration = self.duration + ONE_HOUR
        self.changeSpeedInOneHour()

    def showRaceInfo(self):
        print(f"At: {self.duration}h | Leading Car: {self.leadingCar}")
        for car in self.carList:
            print(car)

    def isWin(self):
        return self.leadingCar.distance > RACE_DISTANCE

    def annouceWin(self,car):
        print("Congratulation !!")
        print(f"THe winner is car: ${car.registerNo}")


    def race(self):

        while self.isWin() == False :
            self.advanceOneHour()
            # self.showRaceInfo()
        print("_____________________________")
        print("Race is completed")
        print("Here is the information of our race:")
        self.showRaceInfo()
        self.annouceWin(self.leadingCar)

carRace = CarRace()
carRace.createCarList()
carRace.showRaceInfo()
carRace.race()