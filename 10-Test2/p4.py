
def f(subjects):
    avg={}
    for key,values in subjects.items():
        sum=0
        for value in values:
            sum+=int(value)
        avg[key]=sum/len(values)
    m=min(avg.values())
    for key,value in avg.items():
        if avg[key]==m:
            return key
        

if __name__=='__main__':
    print(f({'bio':[3,3,4,4,3],'his':[3,3,4,3,3]}))
    print(f({'math':[3,4,4],'geo':[5,4,4,4],'comp':[5,4]}))
    