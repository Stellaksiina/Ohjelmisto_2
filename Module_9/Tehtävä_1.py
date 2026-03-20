class Car:
    def __init__(self, license_plate, maximum_speed, current_speed=0, travelled_distance=0):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance


car = Car("ABC-123", 142)
print(f"License plate: {car.license_plate}\n"
      f"Maximum speed: {car.maximum_speed} km/h\n"
      f"Current speed: {car.current_speed} km/h\n"
      f"Travelled distance: {car.travelled_distance} km")