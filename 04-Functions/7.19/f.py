'''
def f(number):
    sum=0
    for i in str(number):
        x=0
        for a in str(number):
            if i==a:
                x+=1
            if i==a and x>1:
                sum+=int(a)
    return sum
'''

def f(number):
    sum=0
    processed=''
    for i in str(number):
        if i not in processed:
            count=0
            for j in str(number):
                if i==j:
                    count+=1
            if count>1:
                sum+=int(i)*count
            processed+=i
    return sum
if __name__==__name__:
    print(f(1027) )
    print(f(230335) )
    print(f(513553007))