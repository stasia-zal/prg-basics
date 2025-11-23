def f(n):
    count=0
    num=2
    while True:
        prime=True
        for i in range(2,num):
            if num%i==0:
                prime=False
                break
        if prime:
            count+=1
            if count==n:
                return num
        num+=1

print(f(3))
print(f(5))