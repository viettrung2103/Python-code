from Elevator import Elevator

class Building():

    def __init__(self, bottom_floor, top_floor,num_elevators):

        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevator_list = self.create_elevator_list(num_elevators)


    def create_elevator_list(self,num_elevators):

        elevator_list = []

        for index in range(num_elevators):
            elevator_name = f"Elevator {index+1}"
            elevator = Elevator(elevator_name,self.bottom_floor,self.top_floor)
            elevator_list.append(elevator)

        return elevator_list


    def get_elevator_list(self):
        print("___")
        print("Information on Elevator List:")
        for elevator in self.elevator_list:
            print(elevator)


    def run_elevator(self,index_elevator,to_floor):
        print("____________")
        if index_elevator <= 0 or index_elevator > len(self.elevator_list):
            print("Your request is invalid. There is no such elevator.")
        else:
            result_elevator= self.elevator_list[index_elevator-1]
            print(result_elevator)## asum starting number is 1
            result_elevator.go_to_floor(to_floor)
        print("____________")


    def fire_alarm(self):
        for elevator in self.elevator_list:
            elevator.go_to_floor(self.bottom_floor)

#test Elevator
if __name__ == "__main__":
    building = Building(1,10,5)
    building.get_elevator_list()
    # building.run_elevator(1,3)
    # building.get_elevator_list()
    # building.run_elevator(2,10)
    # building.get_elevator_list()
    # building.fire_alarm()
    # building.get_elevator_list()
