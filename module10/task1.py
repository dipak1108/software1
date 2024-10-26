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



def main():

    elevator = Elevator(1, 10)

    print("\nMoving to floor 5:")
    elevator.go_to_floor(5)

    print("\nReturning to the bottom floor:")
    elevator.go_to_floor(elevator.bottom_floor)


main()
