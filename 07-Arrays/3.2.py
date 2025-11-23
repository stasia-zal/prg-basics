arr=[15, 8, 31, 47, 2,19 ]
for i in range(len(arr)//2):
    arr[i],arr[-i-1]=arr[-i-1],arr[i]

print(arr)