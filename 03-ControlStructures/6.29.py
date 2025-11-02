n=int(input('Enter the number: '))
x=0
for i in range (2,n+1): # for every number
    for a in range (2,i+1): #for every number check for division
        if i>a and i%a==0:
            y=i
            y/=a
            if y>=a and y%a==0:
                print(f"divides by {a*a}")
            else:
                print(f"divides by {a}")
            break
        else:
            x+=1
    if x>i-2:
        print(i)
        x=0
