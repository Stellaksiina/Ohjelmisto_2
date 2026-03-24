class Car:
    def __init__(self, license_plate, maximum_speed, current_speed=0, travelled_distance=0):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed_change):
        if self.current_speed + speed_change > 0 and self.current_speed + speed_change < self.maximum_speed:
            self.current_speed = self.current_speed + speed_change
        else:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance = self.travelled_distance + self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        for car in self.cars:
            print(f"{car.license_plate} | {car.current_speed} km/h | {car.travelled_distance} km")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False