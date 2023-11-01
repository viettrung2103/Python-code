class Elevator():
    def __init__(self,name, bottom_floor, top_floor):
        self.name = name
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def __str__(self):
        return f"NAME: {self.name} | CURRENT FLOOR: {self.current_floor} / ({self.bottom_floor} -- {self.top_floor}) "

    def report_current_floor(self):
        print(f"You are current at floor {self.current_floor}")

# to prevent user from intentionally use the floor_up, floor_down outside the go_to_floor method
# and cause the current_floor go beyond the floor range
    def floor_up(self):
        if self.current_floor < self.top_floor:
            print("--Moving Up--")
            self.current_floor += 1


    def floor_down(self):
        if self.bottom_floor < self.current_floor:
            print("--Moving Down--")
            self.current_floor -= 1

    def go_to_floor(self, to_floor):
        print(self)
        if to_floor > self.top_floor or to_floor < self.bottom_floor:
            print("The request is invalid. The requested floor is not exist.")
        elif to_floor == self.current_floor:
            print("You are already the requested floor")
            self.report_current_floor()
        elif self.current_floor < to_floor:
            while self.current_floor < to_floor:
                self.floor_up()
                self.report_current_floor()
            print(f"Welcome! You are at your requested Floor. Floor {self.current_floor}")
            print(self)

        else:
            while self.current_floor > to_floor:
                self.floor_down()
                self.report_current_floor()
            print(f"Welcome! You are at your requested Floor. Floor {self.current_floor}")

#Test the Elevator
if __name__ == "__main__":
    BOTTOM_FLOOR = 1
    TOP_FLOOR = 10

    elevator = Elevator("Elevator-1",BOTTOM_FLOOR,TOP_FLOOR)
    print(elevator)
    elevator.report_current_floor()
    # elevator.go_to_floor(10)
    # elevator.go_to_floor(1)
    # elevator.go_to_floor(1)
    # elevator.go_to_floor(4)

# if __name__ == "__main__":
# BOTTOM_FLOOR = 1
# TOP_FLOOR = 10

# elevator = Elevator("Elevator-1",BOTTOM_FLOOR,TOP_FLOOR)
# print(elevator)
# elevator.report_current_floor()