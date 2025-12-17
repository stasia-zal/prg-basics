import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

brac_op={'(','{','['}
brac_cl={')','}',']'}

def brackets_ok(expression):
    characters=queue.LifoQueue()
    for char in expression:
        if char in brac_op:
            characters.put(char)
        elif char in brac_cl:
            if characters.empty():
                return False
            last=characters.get()
            if last == '(' and char != ')':
                return False
            if last == '{' and char != '}':
                return False
            if last == '[' and char != ']':
                return False
    return characters.empty()#True if brackets in expression are ok of False otherwise

if brackets_ok(expression1):
    print('Everything allright')
else:
    print('this is bullshit')

if brackets_ok(expression2):
    print('Everything allright')
else:
    print('this is bullshit')

if brackets_ok(expression3):
    print('Everything allright')
else:
    print('this is bullshit')
