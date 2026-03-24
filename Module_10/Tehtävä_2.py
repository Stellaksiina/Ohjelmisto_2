class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, new_floor):
        while new_floor > self.current_floor:
            self.floor_up()
        while new_floor < self.current_floor:
            self.floor_down()

    def floor_up(self):
        self.current_floor += 1

    def floor_down(self):
        self.current_floor -= 1


class Building:
    def __init__(self, bottom_floor, top_floor, elevator_count):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []

        for _ in range(elevator_count):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)

    def run_elevator(self, elevator_number, target_floor):
        self.elevators[elevator_number].go_to_floor(target_floor)