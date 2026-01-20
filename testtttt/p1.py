import queue

def f(expression):
    sta=queue.LifoQueue()
    exp=expression.split(' ')
    for it in exp:
        if it .isdigit():
            sta.put(it)
        else:
            b=sta.get()
            a=sta.get()
            if it=='+':
                sta.put(int(b)+int(a))
            elif it=='-':
                sta.put(int(a)-int(b))
    return sta.get()


if __name__=='__main__':
    print(f('2 3 4 5 + - +'))
    print(f('11 7 + 15 - 14 +'))