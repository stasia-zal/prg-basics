class Statistics:
    def __init__(self):
        self.numbers=[]
    def add_numbers(self):
        while True:
            a=int(input('Enter number (0 to end):'))
            if a!=0:
                self.numbers.append(a)
            else:
                break
    def display(self):
        print()
        print('--------------')
        print('Numbers: ',end='')
        for num in self.numbers:
            print(num,end=' ')
        print()
    def greatest(self):
        return  max(self.numbers)
    def smallest(self):
        return min(self.numbers)
    def avg(self):
        return round(sum(self.numbers)/len(self.numbers),2)
    def median(self):
        sorte=sorted(self.numbers)
        n=len(sorte)
        if n%2==1:
            return sorte[n//2]
        else:
            return round((sorte[n//2-1]+sorte[n//2])/2,2)
    def print_sta(self):
        print('----------STATISTICS----------')
        self.display()
        print('The greatest number: ',self.greatest())
        print('The smallest: ',self.smallest())
        print('The arithmetic mean of numbers: ',self.avg())
        print('Median: ',self.median())

