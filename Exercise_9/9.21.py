list_of_changes_speed = [30, 70, 50, -200]

class Car:
    def __init__(self, reg_no="Not selected", cur_spd=0,  max_spd=0, dist=0):
        self.reg_no = reg_no
        self.cur_spd = cur_spd
        self.max_spd = max_spd
        self.dist = dist

    def accelerate(self, change_of_speed):
        self.cur_spd = self.cur_spd + change_of_speed
        return self.cur_spd



car = Car()

car = Car("ABC-123", 50, 240, car.dist)

print(f"\nVehicle Preset Info: Current speed = 50 km/h\n\nRegistration ID: {car.reg_no}\nCurrent Speed: {car.cur_spd} km/h\nMax speed: {car.max_spd} km/h"
      )

car = Car("ABC-123", 50, 240, car.dist)

number_info = 0

for i in list_of_changes_speed:
    number_info = number_info + 1
    car.accelerate(i)

    print(f"\n\nVehicle Status {number_info}:(The speed changes by {i} km/h)\n\nRegistration ID: {car.reg_no}\nCurrent Speed: {car.cur_spd} km/h\nMax speed: {car.max_spd} km/h"
          )










