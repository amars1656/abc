class cylinder:
    def __init__(self,radius=1,height=1):
        self.radius=radius
        self.height=height

    def volume(self):
        return (3.14*((self.radius)**2)*(self.height))

    def area(self):
        return ((2*3.14*self.radius*self.height)+(3.14*2*((self.radius)**2)))       

c=cylinder(3,2)
print(c.volume())     
print(c.area())   