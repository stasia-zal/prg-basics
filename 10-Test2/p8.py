import queue
def f(expressions):
    q=queue.LifoQueue()
    expr=expressions.split()
    for char in expr:
        if char.isdigit():
            q.put(char)
        elif char=='=':
            return q.get()
        else:
            b=int(q.get())
            a=int(q.get())
            if char=='+':
                q.put(a+b)
            if char=='-':
                q.put(a-b)
    return q.get()

print(f("2 3 +"))
print(f("2 6 + 4 5 - +"))
print(f("11 7 + 15 - 14 +"))