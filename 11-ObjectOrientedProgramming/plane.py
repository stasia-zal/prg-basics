class C:
    def __init__(self, arr):
        self.arr=arr
    def m(self,n):
        count=0
        for x,y in self.arr:
            if x>0 and y>0:
                count+=1
            if count>=n: return True
        return False
    
