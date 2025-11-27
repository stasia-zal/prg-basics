arr=[[-38, 19], [5,40],[-7,11],[29,16]]
def f(arr):
    max=arr[0][0]
    min=arr[0][0]
    roww=1
    column=1
    for row in arr:
        for item in row:
            if item>=max:
                max=item
                maxrc=[roww,column]
            if item<=min:
                min=item
                minrc=[roww,column]
            column+=1
        column=1
        roww+=1
    print('Max: ',max, maxrc)
    print('Min: ',min, minrc)


f(arr)