import random


# Car class
class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0

    # Accelerate method to randomly adjust the car's speed
    def accelerate(self):
        speed_change = random.randint(-10, 15)  # Random speed change between -10 and +15 km/h
        self.current_speed += speed_change
        # Ensuring that the current speed doesn't exceed the max speed or fall below 0
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    # Drive method to update the distance traveled in one hour
    def drive(self):
        self.distance_traveled += self.current_speed


# Main program
def race():
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)  # Random max speed between 100 and 200 km/h
        car = Car(f"ABC-{i}", max_speed)
        cars.append(car)

    winner = None
    hour = 0

    # Simulating the race
    while not winner:
        hour += 1
        for car in cars:
            car.accelerate()
            car.drive()
            if car.distance_traveled >= 10000:  # Check if any car has reached 10,000 km
                winner = car
                break

    # Displaying race results
    print(f"Race finished in {hour} hours!")
    print(f"{'Reg Number':<10}{'Max Speed (km/h)':<15}{'Current Speed (km/h)':<20}{'Distance Traveled (km)':<25}")
    print("=" * 70)
    for car in cars:
        print(f"{car.reg_number:<10}{car.max_speed:<15}{car.current_speed:<20}{car.distance_traveled:<25.2f}")


# Run the race
race()
