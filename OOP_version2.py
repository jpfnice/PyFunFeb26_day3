import math

class Point: # __new__(), __init__(), __eq__(), __repr__()
    def __init__(self, valx=0, valy=0):
        self.x=valx
        self.y=valy
    def __repr__(self):
        return f"<{self.x},{self.y}>"
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    def distance(self, other):
        return math.sqrt((other.x-self.x)**2 +(other.y-self.y)**2)
    def __eq__(self, other):
        return self.x==other.x and self.y == other.y
    def __setattr__(self, name, value):
        if name not in ["x", "y"]:
            raise Exception("Wrong attribute name!")
        if not isinstance(value, int) :
            raise TypeError ("Wrong attribute value")
        self.__dict__[name]=value
        
p0=Point()
print(p0)

p1=Point(2, 4.5) # => __init__(p1,2,True)
print(p1)
p1.x=23 # => p1.__setattr__("x", "abc")
p1.y=6
p1.x=100
print(p1.__dict__)

print(p1) # <5,6>

