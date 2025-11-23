arr=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
a=0
b=0
for row in arr:
    for item in row:
        if a==b:
            arr[a][b]='1'
        print(arr[a][b], end=' ')
        b+=1
    print()
    b=0
    a+=1