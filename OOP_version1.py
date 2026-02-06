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
    
# l1=[6,7,8]
# l1.append(10) => append(l1,10)


p0=Point()
# 1) p0=Point.__new__()
# 2) p0.__init__() 
print(p0)
# 1) print(p0.__repr__())

p1=Point(2,3) # l1=list((3,5,6)) d1=dict()
# 1) p1=Point.__new__()
# 2) p1.__init__(2,3) <= Problem !

print(p1) # <2,3>
print("x of p1:", p1.x) # x of p1: 2
print("y of p1:", p1.y) # y of p1: 3
p1.x=5
p1.y=6
print(p1) # <5,6>

p2=Point()
print(p2) # <0,0>
p2.x=1
p2.y=3
print(p2) # <1,3>

p3=p1+p2 
# p3=p1.__add__(p2)

print(p3) # <6,9>

result=p1.distance(p2)
print(result)

p4=Point(6,9)

print(p3==p4) # print(p3.__eq__(p4))

# l1=[p1,p2,p3,p4]

# for e in l1:
#     print(e)