def f(subjects):
    avg={}
    for keys,values in subjects.items():
        sum=0
        for value in values:
            sum+=value
        avg[keys]=sum/len(values)
    a=max(avg.values())
    for keys in avg.keys():
        if avg[keys]==a:
            return keys
print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))