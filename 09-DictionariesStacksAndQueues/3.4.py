import queue

num=int(input("Enter number: "))

result=queue.LifoQueue()

while num>=1:
    if num%2==0:
        result.put(0)
        num//=2
    elif num%2!=0:
        result.put(1)
        num//=2
print('Binary number: ', end='')
while not result.empty():
    print(result.get(),end='')
