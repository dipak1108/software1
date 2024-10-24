#Extend the program by adding an accelerate method into the new class. The method should receive
# the change of speed (km/h) as a parameter. If the change is negative, the car reduces speed.
# The method must change the value of the speed property of the object. The speed of the car
# must stay below the set maximum and cannot be less than zero. Extend the main program so that
# the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h.
# Then print out the current speed of the car. Finally, use the emergency brake by forcing a
# -200 km/h change on the speed and then print out the final speed.
# The travelled distance does not have to be updated yet.

class Car:
    def __init__(self, registration_number,maximum_speed):
        self.registration_number =registration_number
        self.maximum_speed = maximum_speed
        self.current_speed  = 0
        self.travelled_distance = 0


    def set_transmission(self):
        pass

    def accelerate(self, speed):
        speed_new = self.current_speed + speed
        if speed_new > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif speed_new < 0:
            self.current_speed=0
        else:
            self.current_speed = speed_new




car = Car("ABC-123", 142)

print(f"Registration Number: {car.registration_number}")
print(f"Maximum Speed: {car.maximum_speed} km/h")
print(f"Current Speed: {car.current_speed} km/h")
print(f"Travelled Distance: {car.travelled_distance} km")
print("")

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"current speed: {car.current_speed} km/h")
car.accelerate(-200)
print(f"final speed: {car.current_speed} km/h")





