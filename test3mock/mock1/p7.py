def f(arr2d):
    sett=set()
    for i in range(len(arr2d[0])):
        sum=0
        for listik in arr2d:
            sum+=listik[i]
        sett.add(sum)
    return len(sett)!=len(arr2d[0])

print(f([[3,4,2],[5,1,6]]))      # True
print(f([[3,4,2],[5,1,7]]))      # False
print(f([[3,4],[5,1],[4,7]]))    # True
print(f([[3,4],[5,9],[4,7]]))    # False