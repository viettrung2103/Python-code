# Write a Car class that has the following properties:
# registration number, maximum speed, current speed and travelled distance.
# Add a class initializer that sets the first two of the properties based on parameter values.
# The current speed and travelled distance of a new car must be automatically set to zero.
# Write a main program where you create a new car (registration number ABC-123, maximum speed 142 km/h).
# Finally, print out all the properties of the new car.
import random


# Extend the program by adding an accerelate method into the new class.
# The method should receive the change of speed (km/h) as a parameter.
# If the change is negative, the car reduces speed. The method must change the value of the speed property of the object.
# The speed of the car must stay below the set maximum and cannot be less than zero.
# Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h.
# Then print out the current speed of the car. Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed.
# The travelled distance does not have to be updated yet.

# Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
# The method increases the travelled distance by how much the car has travelled in constant speed in the given time.
# Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h.
# Method call car.drive(1.5) increases the travelled distance to 2090 km.

# write a Car class : registration number, maximum speed, current speed, travel distant

MIN_RAND_SPEED = -10
MAX_RAND_SPEED = 15
class Car():
# Add a class initializer that sets the first two of the properties based on parameter values.
# The current speed and travelled distance of a new car must be automatically set to zero.
    def __init__(self,registerNo,maxSpd):

        self.registerNo = registerNo
        self.maxSpeed = maxSpd
        self.currentSpd = 0
        self.distance = 0


    def __str__(self):
        return f"""Number: {self.registerNo} | Max Speed: {self.maxSpeed} | Current Speed: {self.currentSpd} | Travelled Distance: {self.distance}"""


    def speed(self,changeSpeed):

        self.currentSpd =  self.currentSpd + changeSpeed
        if self.currentSpd < 0:
             self.currentSpd = 0
        elif self.currentSpd >= self.maxSpeed:
            self.currentSpd = self.maxSpeed
        return

    def acceleration(self):
        randomChangeSpeed = random.randint(MIN_RAND_SPEED,MAX_RAND_SPEED)
        self.speed(randomChangeSpeed)


    def drive(self,time):
        self.distance = self.distance + self.currentSpd * time


# Write a main program where you create a new car (registration number ABC-123, maximum speed 142 km/h).

#instaniate car object
car1 = Car("ABC-123",142)
car1.speed(30)
car1.acceleration()

car1.speed(70)
car1.speed(50)
car1.speed(-200)
car1.speed(60)
car1.drive(1.5)
# print(car1)
car1.drive(1.5)
print(car1)
# #
# # # Finally, print out all the properties of the new car.
# MAX_RANDOM_SPEED = 200
