class C:
    def __init__(self,dic):
        self.dic=dic
    def m1(self,s,n):
        self.dic[s]=n
    def m2(self,s):
        summ=0
        for item in s:
            if item in self.dic:
                summ+=self.dic[item]
        return summ


stadium = C({"A": 120, "D": 150, "G": 90, "K": 110})

stadium.m1("G", 130)

print(stadium.m2("GD"))   # 280
print(stadium.m2("KEJ"))  # 110