def f(time1,time2):
    t1=''
    t2=''
    a=0
    if 'm' in time1:
        if time1[-2]=='a':
            for i in time1:
                if i!='a' and i!='m':
                    t1+=i
    if 'm' in time1:
        if time1[-2]=='p':
            for i in time1:
                if i!='p' and i!='m':
                    t1+=i
                    if i==':':
    if 'm' in time2:
        if time2[-2]=='a':
            for i in time2:
                if i!='a' and i!='m':
                    t2+=i
    if 'm' in time2:
        if time2[-2]=='p':
            for i in time2:
                if i!='p' and i!='m':
                    t2+=i
    if t1==t2 or time1==time2 or t1==time2 or time1==t2:
        return 






if __name__=="__main__":
    print( f('13:06','13:12') )
    print( f('1:38pm','13:31') )
    print( f('08:08','08:01am') )
    print( f('6:00pm','18:00') )