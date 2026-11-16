import math

class Circle:
    radius = 10

    def get_area(self):
        area = math.pi * (self.radius**2)
        print(f'Area is: {area}')


my_circle = Circle()
my_circle.get_area()