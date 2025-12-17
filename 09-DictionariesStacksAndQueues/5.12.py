import queue
stri=input('Enter text: ')

stack=queue.LifoQueue()

for char in stri:
    stack.put(char)

while not stack.empty():
    print(stack.get(),end='')