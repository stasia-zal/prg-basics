arr1=[4,36,12,28,9,44,5]
arr2=[5,1,36]
res=''
for i in arr1:
    for j in arr2:
        if i==j:
            arr1.remove(i)

print(arr1) 
