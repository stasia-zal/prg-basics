import time
num=int(input('Enter a number: '))
i=1
while i!=num+1:
    if i%3==0 and i%5==0:
        print("BINGO")
        i+=1
    elif i%3==0:
        print("THREE")
        i+=1
    elif i%5==0:
        print("FIVE")
        i+=1
    else:
        print(i)
        i+=1

