class C:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        a=''
        if self.age<18:
            a=self.name[0].lower()+'-'+str(self.age)
            return str(a)
        else :
            a=self.name[0].upper()+'-'+str(self.age)
            return str(a)
        



if __name__=='__main__':
    print(C('John',18))
    print(C('Anna',17))