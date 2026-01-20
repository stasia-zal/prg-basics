def f(x,y,digit):
    count=0
    digit=str(digit)
    for number in range(x,y+1):
        number=str(number)
        for dig in number:
            if dig==digit:
                count+=1
    return count

print(f(10,15,1) )
print(f(28,32,2) )
print(f(100,105,6))
print(f(100,101,0) )