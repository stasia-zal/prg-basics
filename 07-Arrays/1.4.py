a=[2, 3, 7, 5, 4]
print(a)
print(len(a))
print(a[0])
print(a[1])
print(a[len(a)-1])
print(a[len(a)-2])
print(a[0]+a[len(a)-1])
print(a[len(a)//2])
b=''
for i in a:
    b+=str(i)+' '
print(b)