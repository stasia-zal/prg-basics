class Co:
    def __init__(self,name,surname,age,seniority):
        self.name=name
        self.surname=surname
        self.age=age
        self.seniority=seniority
    def __str__(self):
        text=self.surname+self.name[0]+str(self.seniority)
        return text.upper() if self.age>=18 else text.lower()