class C:
        def __init__(self,count):
            self.count=count
        def m1(self):
             return self.count
        def m2(self):
             self.count+=10
        def m3(self):
             self.count-=10
        def m4(self,n):
             self.count+=n
        def __str__(self):
             return str(self.count)



if __name__=='__main__':
    c=C(5)
    print(c.m1())
    c.m2()
    print(c.m1())
    c.m4(-8)
    print(c.m1())
    c.m3()
    print(c.m1())
    c.m4(25)
    print(c.m1())
    print(c.__str__())