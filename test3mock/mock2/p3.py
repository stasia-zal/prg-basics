def f(dic):
    summ=sum(map(lambda x:x,dic.values()))
    avg=summ/len(dic)
    return len(list(filter(lambda x: x>avg,dic.values())))







print(f({"LO231":150,"BA787":120,"NZ15":30}))
print(f({"LO231":150,"BA787":20,"NZ15":30}))