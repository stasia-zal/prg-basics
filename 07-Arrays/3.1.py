arr=[34,7,19,4,21,8]
i=0
res=0
while i!=len(arr):
    if arr[i]%2==0:
        res+=1
    i+=1
print(res)