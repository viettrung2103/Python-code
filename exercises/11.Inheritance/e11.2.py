# Extend the previosly written Car class by adding two subclasses: ElectricCar and GasolineCar.
# Electric cars have the capacity of the battery in kilowatt-hours as their property.
# Gasoline cars have the volume of the tank in liters as their property.
# Write initializers for the subclasses. For example, the initializer of electric cars receives the registration number,
# maximum speed and battery capacity as its parameter. It calls the initializer of the base class to set the first two properties and then sets its capacity.
# Write a main program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l).
# Select speeds for both cars, make them drive for three hours and print out the values of their kilometer counters.

from Car import Car


# def __init__(self, registerNo, maxSpd):
CONSUME_RATE = 10 ## can be 10kh/100km or 10l/100km
class GasolineCar(Car):
    consume_rate = CONSUME_RATE
    def __init__(self,registerNo,maxSpd,battery):
        super().__init__(registerNo,maxSpd)
        self.battery = battery
        self.current_fuel = battery

    # consume fuel in 1 hour
    # def consume(self):





class EletricCar(Car):

    consume_rate = CONSUME_RATE

    def __init__(self,registerNo, maxSpd, tank):
        super().__init__(registerNo,maxSpd)
        self.tank = tank
        self.current_fuel = tank

#initialize
car1 = EletricCar("ABC-15",180,52.5)
car2 = GasolineCar("ACD-123",165,323)

#test
car1.speed(100)
car2.speed(120)

car1.drive(3)
car2.drive(3)

print(car1)
print(car2)