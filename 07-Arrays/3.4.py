arr=[ -15, 8, -31, 47, -2, 19]
a=len(arr)
max=arr[len(arr)-1]
min=arr[len(arr)-1]
for i in range(a):
    for j in range(1,a-i):
        if arr[i]>max:
            max=arr[i]
        elif arr[i]<min:
            min=arr[i]
print(max)
print(min)