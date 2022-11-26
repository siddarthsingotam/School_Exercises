class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def scale(self, factor):
        self.width = self.width * factor
        self.height = self.height * factor

    def print_info(self):
        print(f"{self.width} x {self.height}")
class Display:
    def __init__(self, x_pixels, y_pixels):
        self.x_pixels = x_pixels
        self.y_pixels = y_pixels

    def print_info(self):
        print(f"Resolution: {self.x_pixels} x {self.y_pixels}")

class DisplayRectangle(Rectangle):
    def __init__(self, width, height, x, y, display):
        self.x = x
        self.y = y
        self.display = display
        super().__init__(width, height)

    def move(self, x_displacement, y_displacement):
        self.x = self.x + x_displacement
        self.y = self.y + y_displacement

    def print_info(self):
        print(f"({self.x},{self.y})")
        super().print_info()
        self.display.print_info()


s = Rectangle(3,1)
n = Display(1280,720)
ns = DisplayRectangle(12,5,100,400, n)
n.print_info() # Statement A
s.print_info() # Statement B
ns.print_info() # Statement C
ns.move(50,20)
ns.scale(2)
ns.print_info() # Statement D