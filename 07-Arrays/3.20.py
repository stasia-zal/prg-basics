arr = [7,9,2,4,5,6]
new=[]
for i in arr:
    if i%2==0:
        new.append(i)
for i in arr:
    if i%2!=0:
        new.append(i)
print(arr)
print(new)