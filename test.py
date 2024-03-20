class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius**2 * Circle.pi
    
    def setRadius(self, new_radius):
        self.radius = new_radius


c = Circle(3)
c.setRadius(5)
print(c.area())