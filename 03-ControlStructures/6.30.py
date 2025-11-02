x=7
a=1
z=1
for i in range(1,x*x+1,7):
    for i in range (1,x*x+1,7):
        print(a, end=' ')
        a+=7
    print()
    z+=1
    a=z

## simpler version
x = 7

for row in range(1, x + 1):  # 1 to 7
    for col in range(1, x + 1):
        print(row + (col - 1) * x, end=' ')
    print()