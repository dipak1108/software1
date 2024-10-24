#Extend the previous program by creating a Building class. The initializer parameters for the
# class are the numbers of the bottom and top floors and the number of elevators in the building.
# When a building is created, the building creates the required number of elevators. The list of
# elevators is stored as a property of the building. Write a method called run_elevator that
# accepts the number of the elevator and the destination floor as its parameters.
# In the main program, write the statements for creating a new building and running the elevators
# of the building.


class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, target_floor):
        if target_floor > self.top_floor or target_floor < self.bottom_floor:
            print(
                f"Invalid floor: {target_floor}. Please choose a floor between {self.bottom_floor} and {self.top_floor}.")
            return

        while self.current_floor < target_floor:
            self.floor_up()

        while self.current_floor > target_floor:
            self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")
        else:
            print(f"Elevator is already at the top floor {self.top_floor}.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")
        else:
            print(f"Elevator is already at the bottom floor {self.bottom_floor}.")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]


    def run_elevator(self, elevator_number, target_floor):
        if elevator_number < 1 or elevator_number > len(self.elevators):
            print(
                f"Invalid elevator number: {elevator_number}. There are {len(self.elevators)} elevators in the building.")
            return
        print(f"\nRunning elevator {elevator_number} to floor {target_floor}:")
        self.elevators[elevator_number - 1].go_to_floor(target_floor)



def main():
    building = Building(1, 10, 3)

    building.run_elevator(1, 5)

    building.run_elevator(2, 8)

    building.run_elevator(3, 3)


    building.run_elevator(1, building.bottom_floor)

main()
