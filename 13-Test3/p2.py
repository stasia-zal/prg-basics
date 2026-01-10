
class C:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def m1(self):
        if self.x==0 or self.y==0: return 0
        elif self.x>0:
            if self.y>0:return 1
            if self.y<0: return 4
        elif self.x<0:
            if self.y>0:return 2
            if self.y<0: return 3
    def m2(self,a,b):
        cla=C(a,b)
        cla2=C(self.x,self.y)
        if cla2.m1()==cla.m1():
            return True
        else: return False
    def m3(self,a,b):
        import math
        dist=math.sqrt((self.x-a)**2+(self.y-b)**2)
        if dist>5: return True
        else: return False


if __name__=='__main__':
    p=C(2,3)
    print(p.m1())
    print(p.m2(7,4))
    print(p.m2(-3,1))
    print(p.m3(8,5))
    print(p.m3(4,7))
    p1=C(0,5)
    print(p1.m1())
    print(p1.m2(4,7))
    print(p1.m2(-7,0))

