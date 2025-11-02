n=int(input('Enter the number: '))
x=0
for i in range (2,n+1): # for every number
    x=0
    z=[]
    for a in range (2,i+1): #for every number check for division
        if i>a and i%a==0:
            z.append(a)
        else:
            x+=1
    if x>i-2:
        print(i)
    elif z:
        print(f"{i} divides by {z}")
