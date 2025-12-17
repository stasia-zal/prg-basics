import queue

q=queue.Queue()
ticket=1
while True:

    print('1.Add new customer')
    print('2.Serve a customer')
    print('0.Quit')
    choice=input('Select an option: ')
    if choice=='1':
        print('Your number is ',ticket)
        ticket+=1
        q.put(ticket)
    elif choice=='2':
        if q:
            served=q.get()
            print('Served customer number',served)
        else:
            print('Queue is empty...')
    elif choice=='0':
        break
        