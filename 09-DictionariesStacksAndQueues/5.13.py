def RPN(exp):
    stack=[]
    elements=exp.split()
    for element in elements:
        if element.isdigit():
            stack.append(int(element))
        elif element=='=':return stack.pop()
        else:
            b=stack.pop()
            a=stack.pop()
            if element=='+':stack.append(a+b)
            elif element=='-':stack.append(a-b)
            elif element=='*':stack.append(a*b)
            elif element=='/':stack.append(a/b)
    return stack.pop()

print(RPN('8 3 1 + / 3 2 - 4 + * ='))
