import math
class line(object):
    def __init__(self,cor1,cor2):
        self.cor1=cor1
        self.cor2=cor2

    def distance(self):
        x1,y1=self.cor1
        x2,y2=self.cor2
        return ((x2-x1)**2+(y2-y1)**2)**0.5 

    def slope(self):
        x1,y1=self.cor1
        x2,y2=self.cor2
        return (y2-y1)/(x2-x1)
a=(3,2)
b=(8,10)
c=line(a,b)   
print(c.distance()) 
print(c.slope())