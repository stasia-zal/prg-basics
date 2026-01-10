class C:
    def __init__(self,name,lame,age):
        self.name=name
        self.lame=lame
        self.age=age
    def __str__(self):
        if self.age<18:
            res=self.name[0].lower()+self.lame[0].lower()+str(self.age)
        else:
            res=self.name[0].upper()+self.lame[0].upper()+str(self.age)
        return res