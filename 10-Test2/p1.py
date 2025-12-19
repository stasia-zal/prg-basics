import queue

def f(rpn_exp):
    exp=rpn_exp.split()
    stack=queue.LifoQueue()
    for item in exp:
        if item.isdigit():
            stack.put(item)
        else:
            b=int(stack.get())
            a=int(stack.get())
            if item=='*':
                stack.put(a*b)
            if item=='%':
                stack.put(a%b)
    return stack.get()
            
if __name__=='__main__':
    print(f('5 4 *'))
    print(f('2 6 % 4 5 * *'))
    print(f('11 7 % 15 * 14 %'))
