import math

class C:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def m1(self):
        if self.x==0 or self.y==0:
            return 0
        self.kwa=1+(self.x<0)+2*(self.y<0)
        return self.kwa
    def m2(self,a,b):
        cla=C(a,b)
        return cla.m1()==self.m1()
    def m3(self,a,b):
        dis=math.sqrt((self.x-a)**2+(self.y-b))
        return dis>5
    
p = C(2,3)
print(p.m1())
print(p.m2(7,4))
print(p.m2(-3,1))
print(p.m3(8,5))
print(p.m3(4,7))
p1 = C(0,5)
print(p1.m1())
print(p1.m2(4,7))
print(p1.m2(-7,0))