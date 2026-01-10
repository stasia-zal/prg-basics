
class C:
    def __init__(self,cou):
        self.cou=cou
    def m1(self):
        return self.cou
    def m2(self):
        self.cou+=1
    def m3(self):
        self.cou-=1
    def m4(self,n):
        self.cou+=n
    def __str__(self):
        return str(self.cou)