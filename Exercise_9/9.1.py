class Car:
    def __init__(self, reg_no="nill", cur_spd=0,  max_spd=0, dist=0):
        self.reg_no = reg_no
        self.cur_spd = cur_spd
        self.max_spd = max_spd
        self.dist = dist

car = Car(reg_no= "Not selected")

print(f"\nVehicle Info:\n\nRegistration ID: {car.reg_no}\nSpeed: {car.max_spd} km/h\nCovered distance: {car.dist} km\n\n")

c1 = input("Enter vehicle registration number: ").upper()
c2 = input("Enter current speed(km/h): ")
c3 = input(f"Enter maximum speed(km/h): ")
c4 = input(f"Enter distance travelled(km): ")

car = Car(c1, int(c2), int(c3), int(4))

print(f"\nVehicle Info:\n\nRegistration ID: {c1}\nCurrent Speed: {c2} km/h\nMax speed: {c3} km/h\nCovered distance: {c4} km")




