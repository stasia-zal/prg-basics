arr=[
[7 ,3 ,7, 9 ,0],
[2 ,9, 0 ,1, 5],
[3 ,8 ,6 ,4, 7],]

def f(arr):
    res=[row[:] for row in arr]
    res[0],res[-1]=res[-1],res[0]
    for row in res:
        for item in row:
            print(f"{item:1}", end=" ")  # aligned with width 2
        print()
f(arr)