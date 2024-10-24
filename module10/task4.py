import random

class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self):
        speed_change = random.randint(-10, 15)
        self.current_speed += speed_change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self):
        self.distance_traveled += self.current_speed

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate()
            car.drive()


    def print_status(self):
        print(f"\n{'Reg Number':<10}{'Max Speed (km/h)':<15}{'Current Speed (km/h)':<20}{'Distance Traveled (km)':<25}")
        print("=" * 70)
        for car in self.cars:
            print(f"{car.reg_number:<10}{car.max_speed:<15}{car.current_speed:<20}{car.distance_traveled:<25.2f}")

    def race_finished(self):
        for car in self.cars:
            if car.distance_traveled >= self.distance:
                return True
        return False



def main():
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        car = Car(f"ABC-{i}", max_speed)
        cars.append(car)

    # Create the race
    race = Race("Grand Demolition Derby", 8000, cars)

    hour = 0

    while not race.race_finished():
        race.hour_passes()
        hour += 1
        if hour % 10 == 0:
            print(f"\n--- Race status after {hour} hours ---")
            race.print_status()


    print(f"\n--- Race finished after {hour} hours ---")
    race.print_status()

main()
