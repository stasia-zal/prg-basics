def f(d):
    sum=0
    for amm in d.values():
        sum+=amm
    avg=sum/len(d)
    count=0
    for amm in d.values():
        if amm>avg:
            count+=1
    return count

print(f({"LO231": 150, "BA787": 120, "NZ15": 30}))
print(f({"LO231": 150, "BA787": 20, "NZ15": 30}))