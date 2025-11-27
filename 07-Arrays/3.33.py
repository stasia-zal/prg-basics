arr=[
[7 ,3 ,7, 9 ,0],
[2 ,9, 0 ,1, 5],
[3 ,8 ,6 ,4, 7],]
def f(arr):
    for row in arr:
        row[0],row[-1]=row[-1],row[0]
    for row in arr:
        for item in row:
            print(f"{item:1}", end=" ")  # aligned with width 2
        print()
f(arr)