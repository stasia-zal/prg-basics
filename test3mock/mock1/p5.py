class C:
    def __init__(self,num):
        self.num=num
    def m1(self):
        return self.num
    def m2(self):
        self.num+=1
    def m3(self):
        self.num-=1
    def m4(self,n):
        self.num+=n
    def __str__(self):
        return str(self.num)
    

c = C(5)

print(c.m1())   # 5
c.m2()
print(c.m1())   # 6
c.m4(-8)
print(c.m1())   # -2
c.m3()
print(c.m1())   # -3
c.m4(10)
print(c.m1())   # 7
print(c.__str__())   # "7"
