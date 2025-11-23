def f(dice):
    mem=0
    max_count=0
    for i in dice:
        if i==mem:
            count+=1
            if count>max_count:
                max_count=count
                win=i
        else: 
            count=0
        mem=i
    return win

print(f("5233165554211"))
print(f("2133"))