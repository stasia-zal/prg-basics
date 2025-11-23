arr=[2, 3 ,2, 5, 8 ,1 ,9, 8]
unique=[]
for i in arr:
    if arr.count(i)==1:
        unique.append(i)
print (*arr)
print(*unique)