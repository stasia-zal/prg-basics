class C:
        def __init__(self,dic):
            self.dic=dic
        def m1(self,s,n):
            self.dic[s.upper()]=n
        def m2(self,s):
            sum=0
            count=0
            for item in s:
                if item in self.dic:
                    sum+=self.dic[item]
                    count+=1
                else:
                    continue
            return round(sum/count)
        
        
        
        
if __name__=='__main__':
    stadium=C({"A":120,'D':150,'G':90,'K':110})
    stadium.m1('G',130)
    print(stadium.m2('GD'))
    print(stadium.m2('KEJ'))