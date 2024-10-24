#Again, extend the program by adding a new drive method that receives the number of hours as
# a parameter. The method increases the travelled distance by how much the car has travelled in
# constant speed in the given time. Example: The travelled distance of car object is 2000 km.
# The current speed is 60 km/h. Method call car.drive(1.5) increases the travelled distance to
# 2090 km.

class Car:
    def __init__(self, registration_number,maximum_speed):
        self.registration_number =registration_number
        self.maximum_speed = maximum_speed
        self.current_speed  = 0
        self.travelled_distance = 0


    def sey_transmission(self):
        pass

    def accelerate(self, speed):
        speed_new = self.current_speed + speed
        if speed_new > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif speed_new < 0:
            self.current_speed=0
        else:
            self.current_speed = speed_new

    def drive(self, hours):
        self.travelled_distance = 2000
        self.travelled_distance += self.current_speed * hours



car = Car("ABC-123", 142)


print(f"Registration Number: {car.registration_number}")
print(f"Maximum Speed: {car.maximum_speed} km/h")
print(f"Current Speed: {car.current_speed} km/h")
print(f"Travelled Distance: {car.travelled_distance} km")
print("")

# car.accelerate(30)
# car.accelerate(70)
# car.accelerate(50)
# print(f"current speed: {car.current_speed} km/h")
car.accelerate(60)
print(f"final speed: {car.current_speed} km/h")

car.drive(1.5)
print(f"Travelled Distance : {car.travelled_distance} km")