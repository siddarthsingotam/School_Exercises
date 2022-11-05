class Elevator:
    def __init__(self, top_floor, bottom_floor=0):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.cur_floor = bottom_floor

    def floor_up(self):
        self.cur_floor = self.cur_floor + 1

    def floor_down(self):
        self.cur_floor = self.cur_floor - 1

    def go_to_floor(self, floor):
        if floor == self.cur_floor:
            print(f"Present on same floor: {self.cur_floor}. Moving elevator to bottom floor: {self.bottom_floor}")

        while floor != self.cur_floor and self.bottom_floor <= floor <= self.top_floor:
            if floor > self.cur_floor:
                self.floor_up()
                print(f"Going up, now on floor: {self.cur_floor}")

            if floor < self.cur_floor:
                self.floor_down()
                print(f"Going down, now on floor: {self.cur_floor}")
        print(f"Reached floor: {self.cur_floor} and moving to bottom floor: {self.bottom_floor} if needed.")


class Building:
    list_of_elevators = []

    def __init__(self, top_floor, bottom_floor, no_of_elevators):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.cur_floor = bottom_floor
        self.no_of_elevators = no_of_elevators

        for i in range(no_of_elevators):
            self.list_of_elevators.append(Elevator(top_floor, bottom_floor))

    def run_elevator(self, elevator_x, go_to_floor_x):
        if elevator_x <= 0:
            elevator_x = 1
        if elevator_x > self.no_of_elevators:
            elevator_x = self.no_of_elevators

        print(f"\nElevator: {elevator_x} is under operation")
        elevator_chosen = self.list_of_elevators[elevator_x-1]
        elevator_chosen.go_to_floor(go_to_floor_x)


# Main Program

# Elevator plan for a building 1 🏢🛗
building1 = Building(10, 0, 5)
building1.run_elevator(3, 6)
building1.run_elevator(5, 10)
building1.run_elevator(5, 4)

# Elevator plan for a building 2 🏨🛗

building2 = Building(5, -1, 2)
building2.run_elevator(1, 3)
building2.run_elevator(2, 1)







